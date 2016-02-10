#!/usr/bin/python

from gi.repository import Gtk, Gio
from ux.Window import Window

win = Window()

win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


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