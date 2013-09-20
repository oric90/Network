#!/usr/bin/python
# -*- coding: utf-8 -*-
""" DOCSTRING: """

import numpy as np
import conedy as co


class Network(co.network):
    """ DOCSTRING: """

# public
    def updateNetworkParams(self,paramsDict):
        """ DOCSTRING: """
        self.__networkParams.update(paramsDict)

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
        # Node-Defaults
        self.__defaultDict_pcoIntegrateFire = {  # Defaults for pcoIntegrateFire Nodes
                                'timeDelay': 0.002,
                                'refractoryPeriod': 0.025,
                                'alpha': 0.9,
                                }



    def __del__(self):
        """ DOCSTRING: """
        self.removeObserver()
        self.clear()

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

#    def __initRandomGraph():

#    def __initScaleFree():
