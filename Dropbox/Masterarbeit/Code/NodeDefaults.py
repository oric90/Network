#!/usr/bin/python
# -*- coding: utf-8 -*-
""" DOCSTRING: """

import numpy as np

class NodeDefaults(object):
    """ DOCSTRING: """
    def __init__(self):
        self.__defaultDict_pcoIntegrateFire = {  # Defaults for pcoIntegrateFire Nodes
                    'timeDelay': 0.002,
                    't_ref': 0.025,  # refractory time
                    'alpha': 0.9,  # leakage current
                    }

    def getNodeDefaults(self):
        return self.__defaultDict_pcoIntegrateFire
