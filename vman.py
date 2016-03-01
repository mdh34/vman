#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, inspect, signal, sys
from gi.repository import Gtk, Gio
#import os.path

#from ux.Window import Window
#from ux.Indicator import Indicator
#from ux.MainMenu import MainMenu
from src.Box import Box
from subprocess import call
import sqlite3 as lite
import sys

class Vman():
	"""docstring for Vman"""
	def __init__(self):
		#super(Vman, self).__init__()
		#self.arg = arg

		pwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/ux/"
		command = "python " + pwd + "MainMenu.py &"
		print command
		os.system(command)

		#get home folder
		home = os.path.expanduser("~")
		#get if boxes file exists
		boxes = os.path.isfile(home + '/.vman/boxes')

		if not boxes:
			print "Needs Configs!"

			#list to insert into the config db
			boxlist = (
			    (1, 'Audi', 52642),
			    (2, 'Mercedes', 57127),
			    (3, 'Skoda', 9000),
			    (4, 'Volvo', 29000),
			    (5, 'Bentley', 350000),
			    (6, 'Hummer', 41400),
			    (7, 'Volkswagen', 21600)
			)

			#DB config
			con = lite.connect(home + '/.vman/boxes')
			with con:
			    cur = con.cursor()
			    cur.execute("CREATE TABLE vman_config (box_id text, name text, provider text, state int, directory text, project_dir text)")
				cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
				cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

			#test Data
			#boxlist = ['asd','qwe'] -->database/vagrant global-status  retriven stuff
			boxlist = [
					{'BoxName':"default",'Provider':"VirtualBox",'ID':'3698b9a','State':'running', 'Directory':'/home/glink/Projects/php'}
					#{'BoxName':"Box1",,'ID':1,'State':"on",'Directory':"/home/glink/Projects/test1"},
					#{'BoxName':"Box2",'Provider':"VirtualBox",'ID':2,'State':"on",'Directory':"/home/glink/Projects/test2"}
				]

			objs = [Box() for i in boxlist]

			y = 0
			for x in objs:

				print "Creating box object"
				x.box_id	= boxlist[y]['ID']
				x.name		= boxlist[y]['BoxName']
				x.provider	= boxlist[y]['Provider']
				x.state		= boxlist[y]['State']
				x.directory	= boxlist[y]['Directory']

				y +=1
				pass

			for x in objs:
				pwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
				command = "python tray.py " + x.name + " " + pwd + " &"
				print command
				os.system(command)
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

arg1, arg2, arg3 = [ False, False, False ]
if sys.argv[1:]:   # test if there are atleast 1 argument (beyond [0])
    arg1 = sys.argv[1]
    if sys.argv[2:]:
        arg2 = sys.argv[2]  # careful 'True' is a string, not a boolean
        #arg3 = sys.argv[3:]

if arg1 != False and arg2 != False:
	targetBox 	= arg1
	vmanCommand = arg2
	vbox = Box()
	vbox.box_id		= '3698b9a'
	vbox.name		= "default"
	vbox.provider	= "VirtualBox"
	vbox.state		= 'running'
	vbox.directory	= '/home/glink/Projects/php'
	print targetBox + " - " + vmanCommand + " " + vbox.box_id
	vbox.halt()
	pass
else:
	app=Vman()
