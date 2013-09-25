#!/usr/bin/python
# -*- coding: utf-8 -*-
""" DOCSTRING: """

import conedy as co
import NodeDefaults as ND

class Network(co.network,ND.NodeDefaults):
    """ DOCSTRING: """

# public
    def updateNetworkParams(self,paramsDict):
        """ DOCSTRING: """
        self.__networkParams.update(paramsDict)

    def initNodes(self):
        """ DOCSTRING: """
        if (type(self.__networkParams['nodeType']) == type(co.pcoIntegrateFire())):
            self.__initNode_pcoIntegrateFire()
        else: 
            raise LookupError ('initNetworkNodes: nodeType invalid or not yet defined')

    def initNetwork(self):
        """ DOCSTRING: """
        if (self.__networkParams['networkType'] == 'SmallWorld'):
            self.__initSmallWorld()

        elif (self.__networkParams['networkType'] == 'ScaleFree'):
            print 'not yet defined'

        elif (self.__networkParams['networkType'] == 'RandomGraph'):
            print 'not yet defined'

        else: print 'Error: networkType invalid or not set'

# private
    def __init__(self):
        """ DOCSTRING: """
        co.network.__init__(self)  # Calls the init of Conedy's network class
        ND.NodeDefaults.__init__(self)  # Calls the init of NodeDefaults to implement the defaultDict
        self.__networkParams = {'networkType': '',  # e.g. smallWorld
                                'nodeType': None,  # e.g. pcoIntegrateFire
                                'couplingStrength': 0.01,
                                'nodeCount': 10000,  
                                }
        # Network-Defaults
        self.__defaultDict_smallWorld = {  # Defaults for smallWorld generation
                                'rewiringProbability': 0.5,    
                                'nearestNeighbours': 25,
                                'edgeType': None,
                                'distributionType': co.uniform(0.0,1.0),
                                }
  
        self.__defaultDict_randomGraph = {}  # Defaults for RandomGraph generation
        self.__defaultDict_scaleFree = {}  # Defaults for ScaleFree generation

    def __del__(self):
        """ DOCSTRING: """
        self.removeObserver()
        self.clear()

    def __initNode_pcoIntegrateFire(self):
        """ DOCSTRING: """
        paramsToUpdate = {}
        for nodeParam in self.getNodeDefaults():
            if self.getNodeDefaults()[nodeParam] != self.getParam(0,'pcoIntegrateFire_'+nodeParam):
                paramsToUpdate.update({nodeParam:self.getNodeDefaults()[nodeParam]})            
        for nodeParam in paramsToUpdate:
            print nodeParam
            for nodeNumber in range(0,self.__networkParams['nodeCount']):
                self.setParam(nodeNumber,'pcoIntegrateFire_'+nodeParam,paramsToUpdate[nodeParam])        
    
    def __initSmallWorld(self):
        """ DOCSTRING: """
        self.__defaultDict_smallWorld.update(self.__networkParams)

        self.cycle(self.__defaultDict_smallWorld['nodeCount'],
                   self.__defaultDict_smallWorld['nearestNeighbours'],
                   self.__defaultDict_smallWorld['nodeType'],  
                   self.__defaultDict_smallWorld['edgeType']
                  )
        self.rewire(self.__defaultDict_smallWorld['rewiringProbability'],
                    self.__defaultDict_smallWorld['nodeType']
                   )
        self.randomizeStates(self.__defaultDict_smallWorld['nodeType'],
                             self.__defaultDict_smallWorld['distributionType']   
                            )

newNet = Network()
newNet.updateNetworkParams({'networkType': 'SmallWorld', 'edgeType': co.weightedEdge(0.01), 'nodeType': co.pcoIntegrateFire()})
newNet.initNetwork()
newNet.initNodes()
#for i in range(0,10000):
#    print newNet.getParam(i,'pcoIntegrateFire_t_ref')

#    def __initRandomGraph():

#    def __initScaleFree():
