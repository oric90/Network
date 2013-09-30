#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This class holds the default creation parameters for the different network-topologies """

import conedy as co

class NetworkDefaults(object):
    """ DOCSTRING: """
    def __init__(self):
        """ DOCSTRING: """
        self.defaultDict_NetworkType = {}
#Topologie-Defaults
        self.__defaultDict_smallWorld = {  # Defaults for smallWorld generation
                                'rewiringProbability': 0.5,    
                                'nearestNeighbours': 25,
                                'edgeType': None,
                                'distributionType': co.uniform(0.0,1.0),
                                }
        self.__defaultDict_randomGraph = {}
        self.__defaultDict_scaleFree = {}


    def setNetworkDefaults(self,networkTypeString):
        """ DOCSTRING: """
        if (networkTypeString == "smallWorld"):
            self.defaultDict_NetworkType.update(self.__defaultDict_smallWorld)
        elif (networkTypeString == "scaleFree"):
            self.defaultDict_NetworkType.update(self.__defaultDict_scaleFree)
        elif (networkTypeString == "randomGraph"):
            self.defaultDict_NetworkType.update(self.__defaultDict_randomGraph)
        else: raise KeyError ('networkTypeString invalid or not yet defined')

