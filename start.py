def initilize():
    #navigation between systems
    galaxy = {  "sol" : ["eta helion", "agromega", "pi abbidon"]
               ,"eta helion" : ["agromega", "sol"]
               ,"agromega" : ["eta helion", "euridian", "sol"]
               ,"pi abbidon" : ["sol", "devolin"]
               ,"devolin" : ["pi abbidon", "euridian", "ross"]
               ,"euridian" : ["agromega", "acrux", "carina", "devolin"]
               ,"acrux" : ["euridian"]
               ,"carina" : ["euridian", "ross"]
               ,"ross" : ["devolin", "carina"]
        }
    #navigation within systems
    systems = {   "sol" : [ "mercury", "venus", "earth", "mars"
                            , "the asteroid belt", "jupiter", "saturn"
                            , "uranus", "neptune" ]
                , "eta helion" : [ "eta helion 1", "eta helion 2"
                                    , "eta helion3" ]
                , "agromega" : [ "the asteroid belt", "agromega 1" ]
                , "pi abbidon" : [ "pi abbidon 1", "pi abbidon 2", "pi abbidon3"
                                   , "pi abbidon 4", "pi abbidon 5" ]
                , "devolin" : []
                , "euridian" : [ "euridian 1", "euridian 2", "euridian 3"
                                 , "euridian 4", "euridian 4", "euridian 5"
                                 , "euridian 6", "euridian 7" ]
                , "acrux" : [ "acrux 1", "acrux 2" ]
                , "carina" : [ "carina 1" ]
                , "ross" : [ "ross 1", "ross 2", "ross 3", "ross 4" ]
        }
    gamestate = { "galaxy" : galaxy , "systems" : systems
                  , "location" : [ "sol", "" ]
        }
    return gamestate
