# Copyright (C) 
# 
# File: helloWorld.py
#
# Author: Autodesk Developer Network

# Python script to execute to test the sample in the Maya Script Editor
# import maya
# maya.cmds.loadPlugin("helloWorldCmd.py")
# maya.cmds.spHelloWorld()

#- Import all the necessary modules here
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "spHelloWorld"

# class implementation for custom command
class scriptedCommand(OpenMayaMPx.MPxCommand):
	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)
	def doIt(self,argList):
		print "Hello World!"

# Creator
def cmdCreator():
	return OpenMayaMPx.asMPxPtr( scriptedCommand() )
	
# Initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerCommand( kPluginCmdName, cmdCreator )
	except:
		sys.stderr.write( "Failed to register command: %s\n" % kPluginCmdName )
		raise

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand( kPluginCmdName )
	except:
		sys.stderr.write( "Failed to unregister command: %s\n" % kPluginCmdName )
		raise
