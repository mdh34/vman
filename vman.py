#!/usr/bin/python

import os
import signal
from gi.repository import Gtk, Gio
#import os.path

#from ux.Window import Window
from ux.Indicator import Indicator
from ux.MainMenu import MainMenu
from src.Box import Box

class Vman():
	"""docstring for Vman"""
	def __init__(self):
		#super(Vman, self).__init__()
		#self.arg = arg

		#get home folder
		home = os.path.expanduser("~")
		#get if boxes file exists
		boxes = os.path.isfile(home + '/.vman/boxes')

		if not boxes:
			print "Needs Configs!"
		else:
			print "Does not need Config"

		
		"""
		reads the locations of the boxes,
		returns a list with the locations
		Will be replaced by vagrant global-status
		"""
		def readBoxes(self):
			file = open('data/boxes')
			print "reading config file..."
			with open('data/boxes') as file:
				content = file.readlines()
			print "processing list of boxes..."
			boxesList = []
			for path in content:
					boxesList.append(path[:-1])
			print "boxes list is : "
			print boxesList
			return boxesList
			print file.read()

		#readBoxes()

app=Vman()
		


#ind = MainMenu()
#win = Window()
#
#win.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()

###########################################################################
#manual tests :P
#
box1 = Box()
box1.setId('caixa1')
box1.setName('caixa1')
box1.setProvider('virtualbox')
box1.setState('running')
box1.setDirectory('~/projects/caixa1')

print box1.getId()
print box1.getName()
print box1.getProvider()
print box1.getState()
print box1.getDirectory()

print "---------------------------------------"

box1.openDirectory()
box1.halt()
box1.upOrSuspend()
box1.ssh()


print "---------------------------------------"
print "---------------------------------------"

box2 = Box()
box2.setId('caixa2')
box2.setName('caixa2')
box2.setProvider('virtualbox')
box2.setState('stoped')
box2.setDirectory('~/projects/caixa2')

print box2.getId()
print box2.getName()
print box2.getProvider()
print box2.getState()
print box2.getDirectory()

print "---------------------------------------"
box2.openDirectory()
box2.halt()
box2.upOrSuspend()
box2.ssh()
###########################################################################

#This is the main script should just call windows and indicators :)

#I will need the following:

#REFERENCE ONLY
#
#class Indicator():
#	def __init__(self):
#		pass
#
#	"""
#	reads the locations of the boxes,
#	returns a list with the locations
#
#	Will be replaced by vagrant global-status
#	"""
#	def readBoxes(self):
#		#file = open('data/boxes')
#		print "reading file..."
#		with open('../data/boxes') as file:
#			content = file.readlines()
#
#		print "processing list of boxes..."
#		boxesList = []
#		for path in content:
#				boxesList.append(path[:-1])
#		print "boxes list is : "
#		print boxesList
#		return boxesList
#		print file.read()