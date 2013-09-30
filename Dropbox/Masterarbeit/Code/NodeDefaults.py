#!/usr/bin/python
# -*- coding: utf-8 -*-
""" This class holds the default Parameters for the different Node Types, such as 
pcoIntegrateFire, Lorenz ... """


class NodeDefaults(object):
    """ DOCSTRING: """
    def __init__(self):
        """ DOCSTRING: """
        self.defaultDict_NodeDefaults = {}        
#Nodes
        self.__defaultDict_pcoIntegrateFire = {  # Defaults for pcoIntegrateFire Nodes
                    'timeDelay': 0.002,
                    't_ref': 0.025,  # refractory time
                    'alpha': 0.9,  # leakage current
                    }



    def setNodeDefaults(self,nodeTypeString):
        """ DOCSTRING: """ 
        if (nodeTypeString == 'pcoIntegrateFire'):
            self.defaultDict_NodeDefaults.update(self.__defaultDict_pcoIntegrateFire)
        else: raise KeyError ('nodeTypeString invalid or not yet defined')
