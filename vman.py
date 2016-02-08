#!/usr/bin/python

#import important stuff
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

class Vman():
	def __init__(self):
		pass

	"""
	reads the locations of the boxes,
	returns a list with the locations

	Will be replaced by vagrant global-status
	"""
	def readBoxes(self):
		#file = open('data/boxes')
		print "reading file..."
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


	def open_location(self):
		print "open_location"

	def halt(self):
		print "halt"

	def up_suspend(self):
		print "up_suspend"

	def ssh(self):
		print "ssh"

	def quit(source):
		gtk.main_quit()

lol = Vman()
lol.readBoxes()