#!/usr/bin/python
from subprocess import call
import pprint
import os
import sqlite3 as lite


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
	def setById(self, id):
		#pprint.pprint(self)
		home = os.path.expanduser("~")
		con = lite.connect(home + '/.vman/boxes')
		with con:

			cur = con.cursor()
			#"UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
			cur.execute("SELECT * FROM vman_config WHERE box_id = ?",(id,) )

			rows = cur.fetchone()

			self.box_id 	= rows[0]
			self.name		= rows[1]
			self.provider 	= rows[2]
			self.state    	= rows[3]
			self.directory 	= rows[4]
			self.location   = rows[5]
		#set Properties
		pass

	def updateDataBase(self):

		home = os.path.expanduser("~")
		con = lite.connect(home + '/.vman/boxes')
		with con:
			cur = con.cursor()
			cur.execute("UPDATE vman_config SET name=?, provider=?, state=?, directory=?, project_dir=? WHERE box_id = ?",
						(self.name, self.provider, self.state, self.directory, self.location, self.box_id)
						)
			con.commit()
		pass

	def updateStatus(self, cmd):

		if cmd == "suspend":
			self.state = 'suspended'
		elif cmd == 'halt':
			self.state = 'halt'
		else:
			self.state = 'running'
			pass
		self.updateDataBase()

	## Functionality
	def openDirectory(self):
		dir = self.directory
		print "calling: cd " + dir
		#get default file manager
		#call file manafer on dir locations
		os.popen("xdg-open " +dir)

	def halt(self):
		print "vagrant halt " + self.box_id
		call(["vagrant", "halt", self.box_id])
		self.updateStatus('halt')

	def upOrSuspend(self):
		dir = self.directory
		#need to check the status of the machine on vagrant, in vman

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
		os.popen("cd " + dir + " && vagrant " + cmd)
		self.updateStatus(cmd)
		#change icon in order to have some feedback


	def ssh(self):
		print "calling: vagrant ssh " + self.box_id + "..."
		os.popen("/usr/bin/x-terminal-emulator -e vagrant ssh "+ self.box_id + " &" )
