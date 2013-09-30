#!/usr/bin/python
# -*- coding: utf-8 -*-
""" DOCSTRING: """

import conedy as co
import NodeDefaults as ND  # NodeType
import NetworkDefaults as NT  # NetworkTopologie
import NetworkLogfile as NL  # NetworkLogfile to log parameters and stuff

class Network(co.network, ND.NodeDefaults, NT.NetworkDefaults):
    """ DOCSTRING: """

# public
    def updateNetworkParams(self,paramsDict):
        """ DOCSTRING: """
        self.__networkParams.update(paramsDict)

    def initNodes(self):
        """ DOCSTRING: """
        if (type(self.__networkParams['nodeType']) == type(co.pcoIntegrateFire())):
            self.__initNode_pcoIntegrateFire()
            self.__nodesInitialized = True
        else: 
            raise LookupError ('initNetworkNodes: nodeType invalid or not yet defined')

    def initNetwork(self):
        """ DOCSTRING: """
        self.setNetworkDefaults(self.__networkParams['networkType'])
        self.__supportedNetworkTypes[self.__networkParams['networkType']]()
    
# private
    def __init__(self):
        """ DOCSTRING: """
        co.network.__init__(self)  # Calls the init of Conedy's network class
        ND.NodeDefaults.__init__(self)  # Calls the init of NodeDefaults to prepare the defaultDict
        NT.NetworkDefaults.__init__(self)  # Calls the init of NetworkDefaults to prepare the defaultDict
        self.__networkParams = {'networkType': '',  # e.g. smallWorld
                                'nodeType': None,  # e.g. pcoIntegrateFire
                                'couplingStrength': 0.01,
                                'nodeCount': 10000,  
                                }
#Supported Topologies
        self.__supportedNetworkTypes = {'smallWorld':self.__initSmallWorld,
                                        'scaleFree':self.__initScaleFree,               
                                        'randomGraph':self.__initRandomGraph,                                    
                                        }
        self.__networkInitialized = False
        self.__nodesInitialized = False    

    def __del__(self):
        """ DOCSTRING: """
        self.__networkInitialized = False
        self.__nodesInitialized = False
        self.removeObserver()
        self.clear()

    def __initNode_pcoIntegrateFire(self):  # ALLGEMEINER FASSEN, vllt via nodeString gegeben von initNodes() 
        """ DOCSTRING: """
        paramsToUpdate = {}
        for nodeParam in self.getNodeDefaults():
            if self.getNodeDefaults()[nodeParam] != self.getParam(0,'pcoIntegrateFire_'+nodeParam):
                paramsToUpdate.update({nodeParam:self.getNodeDefaults()[nodeParam]})            
        for nodeParam in paramsToUpdate:
            for nodeNumber in range(0,self.__networkParams['nodeCount']):
                self.setParam(nodeNumber,'pcoIntegrateFire_'+nodeParam,paramsToUpdate[nodeParam])  
      
#Topology-Functions    
    def __initSmallWorld(self):
        """ DOCSTRING: """
        self.defaultDict_NetworkType.update(self.__networkParams)

        self.cycle(self.defaultDict_NetworkType['nodeCount'],
                   self.defaultDict_NetworkType['nearestNeighbours'],
                   self.defaultDict_NetworkType['nodeType'],  
                   self.defaultDict_NetworkType['edgeType']
                  )
        self.rewire(self.defaultDict_NetworkType['rewiringProbability'],
                    self.defaultDict_NetworkType['nodeType']
                   )
        self.randomizeStates(self.defaultDict_NetworkType['nodeType'],
                             self.defaultDict_NetworkType['distributionType']   
                            )
        self.__networkInitialized = True

    def __initScaleFree(self):
        raise IOError ('scaleFree creation not yet defined')
    
    def __initRandomGraph(self):
        raise IOError ('randomGraph creation not yet defined')        

newNet = Network()
newNet.updateNetworkParams({'networkType': 'smallWorld', 'edgeType': co.weightedEdge(0.01), 'nodeType': co.pcoIntegrateFire()})
newNet.initNetwork()
#newNet.initNodes()
#for i in range(0,10000):
#    print newNet.getParam(i,'pcoIntegrateFire_t_ref')


