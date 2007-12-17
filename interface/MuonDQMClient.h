#ifndef MuonDQMClient_H
#define MuonDQMClient_H

/** \class MuonDQMClient
 * *
 *  State machine DQM Client for Muons. Owns a web interface.
 *
 *  $Date: 2007/12/17 17:10:54 $
 *  $Revision: 1.4 $
 *  \author Ilaria Segoni
  */


#include "DQMServices/XdaqCollector/interface/DQMBaseClient.h"
#include "DQMServices/XdaqCollector/interface/Updater.h"
#include "DQMServices/XdaqCollector/interface/UpdateObserver.h"

#include "DQMServices/Core/interface/MonitorUserInterface.h"

#include "DQM/RPCMonitorClient/interface/MuonWebInterface.h"

#include <vector>
#include <string>
#include <iostream>
#include <fstream>

// class SubscriptionHandle;
class QTestHandle;

class MuonDQMClient : public DQMBaseClient, 
			       public dqm::UpdateObserver
{
public:
  
  /// You always need to have this line! Do not remove:
  XDAQ_INSTANTIATOR();

  ///Constructor:  
  MuonDQMClient(xdaq::ApplicationStub *s);

  /// Override DQMBaseClient::general, which outputs the web interface page:
  void general(xgi::Input * in, xgi::Output * out ) throw (xgi::exception::Exception);

  /// Handles all HTTP requests
  void handleWebRequest(xgi::Input * in, xgi::Output * out);

  /// this obligatory method is called whenever the client enters the "Configured" state:
  void configure();

  /// this obligatory method is called whenever the client enters the "Enabled" state:
  void newRun();

  /// this obligatory method is called whenever the client enters the "Halted" state:
  void endRun();

  // this obligatory method is called by the Updater component, whenever there is an update 
  void onUpdate() const;
  

private:

  void checkGolbalQTStatus() const;   
  void checkDetailedQTStatus() const; 

private:

  

  /// MuonDQMClient has a web interface:  
  MuonWebInterface * webInterface_p;

  //  SubscriptionHandle *subscriber;
  QTestHandle * qtHandler;
  
  bool qtestsConfigured;
  bool meListConfigured;
 
  mutable std::ofstream logFile;    
  mutable unsigned int QTFailed;    
  mutable unsigned int QTCritical;    

};

// You always need to have this line! Do not remove:
XDAQ_INSTANTIATOR_IMPL(MuonDQMClient)

#endif
