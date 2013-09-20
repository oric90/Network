#!/usr/bin/python

import numpy as np
import conedy as co

class Network(co.network):
	#Variables
		#private
		#public

	#Functions
		
	def __init__(self):
		co.network.__init__(self)
		self.networkParams = {"networkType" : ""}
		self.__oscillatorType = ""
		self.__nodeCount = 0


		#public

	def initNetwork(self,paramsDict = {'networkType' : 'SmallWorld', 'couplingStrength' : 0.01}):
		#append paramsDict to networkParams
		self.__appendParamsToNetwork(paramsDict)
		#choose network Topology
		if self.networkParams["networkType"] == "SmallWorld":
			self.__initSmallWorld()
		elif self.networkParams["networkType"] == "RandomGraph":
			self.__initRandomGraph()
		elif self.networkParams["networkType"] == "ScaleFree":
			self.__initScaleFree()
		else: print "Error: networkType invalid or not yet defined" 

	def printNetworkType(self,networkType):
		return self.networkParams["networkType"]
	def setOscillatorType(self,oscillatorType):
		self.__oscillatorType = oscillatorType
	def printOscillatorType(self):
		return self.__oscillatorType
	def setNodeCount(self,nodeCount):
		self.__NodeCount = nodeCount
	def printNodeCount(self):
		return self.__nodeCount

	def __del__(self):
		self.removeObserver()
		self.clear()

		#private
	def __appendParamsToNetwork(self,paramsDict):	
		for key in paramsDict:
			self.networkParams[key] = paramsDict[key]

	def __appendParamsToDefault(self,defaultDict):
		for key in self.networkParams:
			defaultDict[key] = self.networkParams[key] 

	def __initSmallWorld(self):
		defaultDict = {'rewiringProbability' : 0.5, 'delayTime' : 0.002, 'refractoryPeriod' : 0.021, 'nearestNeighbours': 25, 'nodeType': co.pcoIntegrateFireDelay()}
		print "Initializing SmallWorld Network"
		self.__appendParamsToDefault(defaultDict)

		self.cycle(self.__nodeCount, defaultDict['nearestNeighbours'], defaultDict['nodeType'], co.weightedEdge(defaultDict['couplingStrength']))
	        self.rewire(defaultDict['rewiringProbability'], defaultDict['nodeType'])
		self.randomizeStates(defaultDict['nodeType'], co.uniform(0.0, 1.0));		
	
	def __initScaleFree(self):
		defaultDict = {}
		print "Initializing ScaleFree Network"
		self.__appendParamsToDefault(defaultDict)

	def __initRandomGraph(self):
		defaultDict = {}
		print "Initializing RandomGraph Network"
		self.__appendParamsToDefault(defaultDict)
