/** \file
 *
 *  Implementation of QTestStatusChecker
 *
 *  $Date: 2006/03/13 15:51:52 $
 *  $Revision: 1.3 $
 *  \author Ilaria Segoni
 */

#include "DQM/RPCMonitorClient/interface/QTestStatusChecker.h"
#include "DQM/RPCMonitorClient/interface/DQMClientDefineDebug.h"
#include <iostream>

QTestStatusChecker::QTestStatusChecker(){
}

QTestStatusChecker::~QTestStatusChecker(){
}

std::pair<std::string,std::string> QTestStatusChecker::checkGlobalStatus(MonitorUserInterface * mui){
        #ifdef DEBUG
		std::cout << "In QTestStatusChecker::checkGlobalStatus" << std::endl;
		std::cout <<"Possible states: successful "<< dqm::qstatus::STATUS_OK<<", error:  " 
		<< dqm::qstatus::ERROR<<", warning:  "<< dqm::qstatus::WARNING<<
		", Other: "<< dqm::qstatus::OTHER<<std::endl;
	#endif
	
	std::pair<std::string,std::string> statement;
	int status= mui->getSystemStatus();
	switch(status){
		case dqm::qstatus::ERROR:
			statement.first ="Errors detected in quality tests";
			statement.second="red";
			break;
	  	case dqm::qstatus::WARNING:
			statement.first ="Warnings detected in quality tests";
			statement.second="orange";
			break;
	 	case dqm::qstatus::OTHER:
	    		statement.first="Some tests did not run";
	    		statement.second="black";
	    		break; 
	  	default:
	    		statement.first="No problems detected in quality tests ";
	    		statement.second="green";
	}

        #ifdef DEBUG
		std::cout << "In QTestStatusChecker::checkGlobalStatus" << std::endl;
		std::cout <<"Possible states: successful "<< dqm::qstatus::STATUS_OK<<", error:  " 
		<< dqm::qstatus::ERROR<<", warning:  "<< dqm::qstatus::WARNING<<
		", Other: "<< dqm::qstatus::OTHER<<std::endl;
		std::cout << "Current Status: " << status<< std::endl;
	#endif
	

	return statement;
}

std::map< std::string, std::vector<std::string> > QTestStatusChecker::checkDetailedStatus(MonitorUserInterface * mui){ 
        #ifdef DEBUG
		std::cout << "In QTestStatusChecker::checkDetailedStatus" << std::endl;
	#endif
	detailedWarnings.clear();
	this->searchDirectories(mui);
	return detailedWarnings;
} 


void QTestStatusChecker::searchDirectories(MonitorUserInterface * mui) {
	std::vector<std::string> meNames=mui->getMEs();   
	std::vector<std::string> dirNames=mui->getSubdirs();
	int numberOfME=meNames.size();
	int numberOfDir=dirNames.size();
        
	#ifdef DEBUG
		std::string currentDir=mui->pwd();
		std::cout << "Searching ME's with quality tests in " << currentDir<<"\n"
		      << "There are " << numberOfME <<" monitoring elements and "
		      << numberOfDir<<" directories\n"<< std::endl;
	#endif
	
	if(numberOfME) {
		this->processAlarms(meNames, currentDir, mui);
	}
 
 	 if(numberOfDir){
		for(std::vector<std::string>::iterator it = dirNames.begin();it != dirNames.end();++it){
			mui->cd(*it);
      			this->searchDirectories(mui);
    		}   
	}   	
	
	mui->goUp();
  
	return;
}



void QTestStatusChecker::processAlarms(std::vector<std::string> meNames, std::string currentDir, MonitorUserInterface * mui){

	for(std::vector<std::string>::iterator nameItr= meNames.begin(); nameItr!= meNames.end(); ++nameItr){
      
		std::string colour;
		char text[128];
        
		MonitorElement * me =0;
		char fullPath[128];
		sprintf(fullPath,"%s/%s",currentDir.c_str(),(*nameItr).c_str());
		me= mui->get(fullPath);
		std::vector<QReport *> report;
		if(me){
		 	if (me->hasError()){
		 		colour="red";
				report= me->getQErrors();
        			std::cout<<"sonoqui1 "<<std::endl;
		 	} 
		 	if( me->hasWarning()){ 
		 		colour="orange";
				report= me->getQWarnings();
        			std::cout<<"sonoqui2 "<< std::endl;
		 	}
		 	if(me->hasOtherReport()){
		 		colour="black";
 				report= me->getQOthers();
       				std::cout<<"sonoqui3 "<<std::endl;
		 	}
	
		 	for(std::vector<QReport *>::iterator itr=report.begin(); itr!=report.end();++itr ){
				sprintf(text,"%s:%s",(*nameItr).c_str(),((*itr)->getMessage()).c_str());
				
				#ifdef DEBUG
					std::cout<<"MonitorElement "<<fullPath<<" has message: "<<(*itr)->getMessage()<<std::endl;
				#endif
	    		
				std::vector<std::string> messageList;
	    			if( detailedWarnings.find(colour) == detailedWarnings.end()){
 	      				messageList.push_back(text);
	      				detailedWarnings[colour]=messageList;
	    			}else{
	      				messageList=detailedWarnings[colour];
	      				messageList.push_back(text);
	    			}	    
		 	}	
		}
	}

}