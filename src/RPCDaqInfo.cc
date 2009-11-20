#include "DQM/RPCMonitorClient/interface/RPCDaqInfo.h"
#include <DQM/RPCMonitorClient/interface/RPCRawDataCountsHistoMaker.h>
#include "DataFormats/FEDRawData/interface/FEDNumbering.h"
#include "CondFormats/RunInfo/interface/RunInfo.h"
#include "CondFormats/RunInfo/interface/RunSummary.h"
#include "CondFormats/DataRecord/interface/RunSummaryRcd.h"
#include "EventFilter/RPCRawToDigi/interface/RPCRawDataCounts.h"
#include "EventFilter/RPCRawToDigi/interface/DataRecord.h"
#include "EventFilter/RPCRawToDigi/interface/ReadoutError.h"

using namespace std;
using namespace edm;
RPCDaqInfo::RPCDaqInfo(const edm::ParameterSet& ps) {
 
  FEDRange_.first  = ps.getUntrackedParameter<unsigned int>("MinimumRPCFEDId", 790);
  FEDRange_.second = ps.getUntrackedParameter<unsigned int>("MaximumRPCFEDId", 792);
  
  NumberOfFeds_ =FEDRange_.second -  FEDRange_.first +1;

  numberOfDisks_ = ps.getUntrackedParameter<int>("NumberOfEndcapDisks", 3);

  FATAL_LIMIT = 5;

}

RPCDaqInfo::~RPCDaqInfo(){}

void RPCDaqInfo::beginLuminosityBlock(const LuminosityBlock& lumiBlock, const  EventSetup& iSetup){}

void RPCDaqInfo::endLuminosityBlock(const edm::LuminosityBlock&  lumiBlock, const  edm::EventSetup& iSetup){}

void RPCDaqInfo::beginJob(const EventSetup& iSetup){
 LogVerbatim ("rpcdaqinfo") << "[RPCDaqInfo]: Begin job ";
 dbe_ = Service<DQMStore>().operator->();
}

void RPCDaqInfo::beginRun(const Run& r, const EventSetup& iSetup){
  
  LogVerbatim ("rpcdaqinfo") << "[RPCDaqInfo]: Begin run";
   
  dbe_->setCurrentFolder("RPC/EventInfo/DAQContents");
   
   //  int limit = numberOfDisks_;
  //  if(numberOfDisks_ < 2) limit = 2;
    

  for (int w = -2; w<= 2;w++ ){//loop on wheels and disks
    stringstream streams;
    streams << "RPC_Wheel" << w;
    daqWheelFractions_[w+2] = dbe_->bookFloat(streams.str());
    daqWheelFractions_[w+2]->Fill(1);
  }
   
  for (int d = 0; d< numberOfDisks_; d++ ){
    stringstream streams;
    streams << "RPC_Disk" << (d-numberOfDisks_);
    daqDiskFractions_[d] = dbe_->bookFloat(streams.str());
    daqDiskFractions_[d]->Fill(1);

    streams.str("");
    streams << "RPC_Disk" << (numberOfDisks_-d);
    daqDiskFractions_[2*numberOfDisks_-1-d] = dbe_->bookFloat(streams.str());
    daqDiskFractions_[2*numberOfDisks_-1-d]->Fill(1);
  }

  
  //daq ummary for RPCs
  dbe_->setCurrentFolder("RPC/EventInfo");
     
  DaqFraction_ = dbe_->bookFloat("DAQSummary");
  DaqFraction_->Fill(1);
    

  DaqMap_ = dbe_->book2D( "DAQSummaryMap","RPC DAQ Summary Map", 1, 0.0, 1.0,  NumberOfFeds_, FEDRange_.first ,FEDRange_.second+1);
  //aesthetic features 
  DaqMap_ ->setBinLabel(1,"",1);
  DaqMap_->setAxisTitle("",1);
  DaqMap_->setAxisTitle("FED",2);
  
  stringstream label;
  for (int y = 0; y<DaqMap_->getNbinsY(); y++){
    label.str("");
    label << FEDRange_.first + y;
    DaqMap_->setBinLabel(y+1,label.str(), 2);
    DaqMap_->setBinContent(1, y+1, 1);
  }
  
  //Check if RPCs are in the READOUT
  edm::eventsetup::EventSetupRecordKey recordKey(edm::eventsetup::EventSetupRecordKey::TypeTag::findType("RunInfoRcd"));
  FedCount_ = 0;
  if(0 != iSetup.find( recordKey ) ) {
  
    
    //get fed summary information
    ESHandle<RunInfo> sumFED;
    try{
      iSetup.get<RunInfoRcd>().get(sumFED);    
    }catch(...) { return;  }   

    vector<int> FedsInIds= sumFED->m_fed_in;   

    //loop on all active feds
    for(unsigned int fedItr=0;fedItr<FedsInIds.size(); ++fedItr) {
      int fedID=FedsInIds[fedItr];
      //make sure fed id is in allowed range  
      if(fedID>=FEDRange_.first && fedID<=FEDRange_.second) {
	++FedCount_;
	DaqMap_->setBinContent(1,fedID, 1);
      }   
    }   
  }   
  
  if(FedCount_ > 0 ) {
 
    DaqFraction_->Fill(1);
    
    for (int i = -2; i<= 2;i++ ){//loop on wheels and disks
      daqWheelFractions_[i+2]->Fill(1);
    }
      
    for (int i = 0; i<2*numberOfDisks_;i++ ){    
      daqDiskFractions_[i]->Fill(1);
    }
  }
  
}


void RPCDaqInfo::endJob() {}


void RPCDaqInfo::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup){


  //get hold of raw data counts
  Handle<RPCRawDataCounts> rawCounts;

  try{
    iEvent.getByType (rawCounts);
  }catch(...) { return;  } 


  const RPCRawDataCounts  theCounts = (*rawCounts.product());

  RPCRawDataCountsHistoMaker histoMaker(theCounts);

  map< pair<int,int>, int > myReadoutErrors = histoMaker.readoutErrors();
  vector<int> fatalFEDs;


 if ( myReadoutErrors != readoutErrors_ ){
   map< pair<int,int>, int >::const_iterator itr;
   map< pair<int,int>, int >::const_iterator  itr2;
   for(itr = myReadoutErrors.begin(); itr!= myReadoutErrors.end(); itr++ ){
     itr2= readoutErrors_.find((*itr).first);
     if( itr2 !=readoutErrors_.end() ||  readoutErrors_.size()!=0 || (*itr2).second !=(*itr).second) {
       if((*itr2).first.second <= FATAL_LIMIT ) fatalFEDs.push_back((*itr2).first.first);
     }
   }

  

   sort(fatalFEDs.begin(),fatalFEDs.end() );
   fatalFEDs.resize(  unique(fatalFEDs.begin(),fatalFEDs.end())-fatalFEDs.begin());

 
   for(unsigned int fed =  0 ; fed<fatalFEDs.size(); fed++){
     if(fatalFEDs[fed] <  FEDRange_.first  || fatalFEDs[fed] >  FEDRange_.second) continue;
     DaqMap_->setBinContent(1,(fatalFEDs[fed]- FEDRange_.first +1),0);

     }



   float goodFraction  = 0;
   if(FedCount_ != 0)
     goodFraction = (FedCount_- fatalFEDs.size())/FedCount_;

   
   DaqFraction_->Fill(goodFraction);

   
   for (int w = -2; w<= 2;w++ ){//loop on wheels
     	daqWheelFractions_[w+2]->Fill(goodFraction);
   }
   

   for (int d = 0; d< (2*numberOfDisks_) ;d++ ){//loop on wheels
      if(daqDiskFractions_[d]) daqDiskFractions_[d]->Fill(goodFraction);
   }
 } 

 
 readoutErrors_ = myReadoutErrors;
}

