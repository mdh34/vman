#!/usr/bin/python

import os
import signal
from gi.repository import Gtk, Gio
#import os.path

#from ux.Window import Window
from ux.Indicator import Indicator
from ux.MainMenu import MainMenu
from src.Box import Box
from subprocess import call

class Vman():
	"""docstring for Vman"""
	def __init__(self):
		#super(Vman, self).__init__()
		#self.arg = arg

		ind = MainMenu()
		#Gtk.main()

		#get home folder
		home = os.path.expanduser("~")
		#get if boxes file exists
		boxes = os.path.isfile(home + '/.vman/boxes')

		if not boxes:
			print "Needs Configs!"

			#test Data
			#boxlist = ['asd','qwe']
			boxlist = [
					{'BoxName':"Box1",'Provider':"VirtualBox",'ID':1,'State':"on",'Directory':"/home/glink/Projects/test1"},
					{'BoxName':"Box2",'Provider':"VirtualBox",'ID':2,'State':"on",'Directory':"/home/glink/Projects/test2"}
				]

			objs = [Box() for i in boxlist]

			y = 0
			for x in objs:
				print 'hey ' + str(y)

				#print x['Provider']
				#print x['BoxName']
				#print x['State']
				#print x['Directory']
				#print "-----------||-----------"

				print "Creating box object"
				#vBoxMenu = Box()
				x.setId(boxlist[y]['ID'])
				x.setName(boxlist[y]['BoxName'])
				x.setProvider(boxlist[y]['Provider'])
				x.setState(boxlist[y]['State'])
				x.setDirectory(boxlist[y]['Directory'])
				#print vars(x)
				#indy = Indicator(x)

				y +=1

				pass
			indys = [Indicator(i) for i in objs]
			#for x in indys:
			#	x.live()
			#	pass

			for  x in boxlist:
				os.system("python tray.py &")
				pass

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
#Gtk.main()


#ind = MainMenu()
#win = Window()
#
#win.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()

###########################################################################
#manual tests :P
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
