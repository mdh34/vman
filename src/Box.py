#!/usr/bin/python
from subprocess import call

class Box():

	box_id 		= ''
	name		= ''
	provider 	= ''
	state    	= ''
	directory 	= ''
	location    = ''

	def __init__(self):
		pass

	# I'm thinking if it really is necessary to create a db with this info
	# Or if files are everything I need
	def setById(id):
		#connect to db
		#get row
		#set Properties
		pass

	## Functionality
	def openDirectory(self):
		dir = self.directory
		print "calling: cd " + dir
		#get default file manager
		#call file manafer on dir locations
		call(["xdg-open", "dir"])

	def halt(self):
		print "vagrant halt " + self.box_id
		call(["vagrant", "halt", self.box_id])

	def upOrSuspend(self):
		dir = self.directory

		print "changing directory..."
		cmd = "cd " + dir + " && "
		status = self.state

		if (status == 'running'):
			print "status on, suspending"
			cmd = "suspend"

		else:
			print "status off or suspended, turning on"
			cmd = "up"

		print "calling: cd " + dir + " && vagrant " + cmd
		call(["cd", dir, "&&", "vagrant", cmd])
		#run cmd

	def ssh(self):
		print "calling: vagrant ssh " + self.box_id + "..."
		call(["vagrant", "ssh", self.box_id])

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
