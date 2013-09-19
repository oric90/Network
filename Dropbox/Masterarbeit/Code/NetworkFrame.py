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

	def initNetwork(self,paramsDict = {'couplingStrength' : }):
		#append paramsDict to networkParams
		for key in paramsDict:
			networkParams[key] = paramsDict[key]
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
	def __initSmallWorld(self):
		print "Initializing SmallWorld Network"

	def __initScaleFree(self):
		print "Initializing ScaleFree Network"

	def __initRandomGraph(self):
		print "Initializing RandomGraph Network"
