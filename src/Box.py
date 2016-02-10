#!/usr/bin/python

class Box():

	box_id 		= ''
	name		= ''
	provider 	= ''  
	state    	= ''
	directory 	= ''

	def __init__(self):
		pass

	# I'm thinking if it really is necessary to create a db with this info
	# Or if files are everything I need

	## Class Getters:
	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getProvider(self):
		return self.provider

	def getState(self):
		return self.state

	def getDirectory(self):
		return self.directory

	## Class Getters:
	def setId(self, boxId):
		self.id = boxId

	def setName(self, boxName):
		self.name = boxName

	def setProvider(self, boxProvider):
		self.provider = boxProvider

	def setState(self, boxState):
		self.state = boxState

	def setDirectory(self, boxDirectory):
		self.directory = boxDirectory

	## Functionality
	def openDirectory(self):
		dir = self.getDirectory()
		print "cd " + dir

	def halt(self):
		print "vagrant halt " + self.getId()

	def upOrSuspend(self):
		dir = self.getDirectory()

		print "changing directory..."

		cmd = "cd " + dir + " && "
		status = self.getState()

		if (status == 'running'):
			print "status on, suspending"
			cmd += "vagrant suspend"

		else:
			print "status off or suspended, turning on"
			cmd += "vagrant up"

		print cmd
		#run cmd

	def ssh(self):
		print "vagrant ssh " + self.getId()

#manual tests :P
#
#box1 = Box()
#box1.setId('caixa1')
#box1.setName('caixa1')
#box1.setProvider('virtualbox')
#box1.setState('running')
#box1.setDirectory('~/projects/caixa1')
#
#print box1.getId()
#print box1.getName()
#print box1.getProvider()
#print box1.getState()
#print box1.getDirectory()
#
#print "---------------------------------------"
#
#box1.openDirectory()
#box1.halt()
#box1.upOrSuspend()
#box1.ssh()
#
#
#print "---------------------------------------"
#print "---------------------------------------"
#
#box2 = Box()
#box2.setId('caixa2')
#box2.setName('caixa2')
#box2.setProvider('virtualbox')
#box2.setState('stoped')
#box2.setDirectory('~/projects/caixa2')
#
#print box2.getId()
#print box2.getName()
#print box2.getProvider()
#print box2.getState()
#print box2.getDirectory()
#
#print "---------------------------------------"
#box2.openDirectory()
#box2.halt()
#box2.upOrSuspend()
#box2.ssh()