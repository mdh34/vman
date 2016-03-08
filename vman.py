#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, inspect, signal, sys, subprocess
from gi.repository import Gtk, Gio
import os.path

#from ux.Window import Window
#from ux.Indicator import Indicator
#from ux.MainMenu import MainMenu
from src.Box import Box
from subprocess import call
from subprocess import Popen
from subprocess import PIPE
import sqlite3 as lite
import sys

class Vman():
	"""docstring for Vman"""
	def __init__(self):
		#super(Vman, self).__init__()
		#self.arg = arg
		# create main menu Indicator
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
			#test Datade
			#boxlist = ['asd','qwe'] -->database/vagrant global-status  retriven stuff
			boxlist = (
					{'BoxName':"default",'Provider':"VirtualBox",'ID':'3698b9a','State':'running', 'Directory':'/home/glink/Projects/php'},
					#{'BoxName':"Box1",,'ID':1,'State':"on",'Directory':"/home/glink/Projects/test1"},
					{'BoxName':"Box2",'Provider':"VirtualBox",'ID':2,'State':"on",'Directory':"/home/glink/Projects/test2"},
				)
			print boxlist[0]['BoxName']

			tmp = os.popen("vagrant global-status --prune | grep '/'").read()

			tmp = tmp.split('\n')
			boxlist = []
			for string in tmp:
				notempty = string.rstrip()
				if notempty != '':
					notempty = notempty.split(' ')
					data=[]
					for item in notempty:
						if item != '':
							data.append(item)
					data.append('toset')
					boxlist.append(data)
			#print boxlist
			os.system('mkdir ' + home + '/.vman/')
			#sys.exit(home + '/.vman/boxes')

			#DB config
			call(["touch",home + '/.vman/boxes'])
			con = lite.connect(home + '/.vman/boxes')
			with con:
				cur = con.cursor()
				cur.execute("CREATE TABLE vman_config (box_id text, name text, provider text, state int, directory text, project_dir text)")
				cur.executemany("INSERT INTO vman_config VALUES(?, ?, ?, ?, ?, ?)", boxlist)

			## This needs to be inside a funcion
			objs = [Box() for i in boxlist]
			#print boxlist
			#sys.exit(home + '/.vman/boxes')
			y = 0
			for x in objs:
				# To do: refactor this no need for the object creation at this stage or ever probably
				print "Creating box object"
				x.box_id	= boxlist[y][0]
				x.name		= boxlist[y][1]
				x.provider	= boxlist[y][2]
				x.state		= boxlist[y][3]
				x.directory	= boxlist[y][4]
				x.location  = boxlist[y][5]

				y +=1
				pass

			for x in objs:
				pwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
				command = "python tray.py " + x.name + " " + pwd + " &"
				print command
				os.system(command)
				pass
			##This needs to be inside a funcion

		else:
			print "Does not need Config"
			print boxes
			#sys.exit()
			con = lite.connect(home + '/.vman/boxes')

			with con:

			    cur = con.cursor()
			    cur.execute("SELECT * FROM vman_config")

			    rows = cur.fetchall()

			    for row in rows:
			        print row

#			## This needs to be inside a funcion
#			objs = [Box() for i in rows]
#			#print boxlist
#			#sys.exit(home + '/.vman/boxes')
#			y = 0
#			for row in rows:
#				# To do: refactor this no need for the object creation at this stage or ever probably
#				print "Creating box object"
#				x.box_id	= rows[y][0]
#				x.name		= rows[y][1]
#				x.provider	= rows[y][2]
#				x.state		= rows[y][3]
#				x.directory	= rows[y][4]
#				x.location  = rows[y][5]
#
#				y +=1
#				pass
#
#			for x in objs:
#				pwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#				command = "python tray.py " + x.name + " " + pwd + " &"
#				print command
#				os.system(command)
#				pass
			##This needs to be inside a funcion
			#sys.exit(boxes)
#		"""
#		reads the locations of the boxes,
#		returns a list with the locations
#		Will be replaced by vagrant global-status
#		"""
#		def readBoxes(self):
#			file = open('data/boxes')
#			print "reading config file..."
#			with open('data/boxes') as file:
#				content = file.readlines()
#			print "processing list of boxes..."
#			boxesList = []
#			for path in content:
#					boxesList.append(path[:-1])
#			print "boxes list is : "
#			print boxesList
#			return boxesList
#			print file.read()

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

	if vmanCommand == 'open_location':
		vbox.openDirectory()
	if vmanCommand == 'halt':
		vbox.halt()
	if vmanCommand == 'up_suspend':
		vbox.upOrSuspend()
	if vmanCommand == 'ssh':
		vbox.ssh()
	pass
else:
	app=Vman()
