def rpclayout(i, p, *rows): i["Layouts/RPC Layouts/" + p] = DQMItem(layout=rows)

rpclayout(dqmitems, "RPC_Summary",

          ["RPC/RecHits/GlobalHistograms/GlobalRecHitsXYCoordinates_Wheel_0_0",
           "RPC/RecHits/GlobalHistograms/GlobalRecHitsXYCoordinates_Wheel_0_1",
           "RPC/RecHits/GlobalHistograms/GlobalRecHitsXYCoordinates_Wheel_0_2"],
           ["RPC/RecHits/GlobalHistograms/ClusterSize_for_Barrel"]);

                   
