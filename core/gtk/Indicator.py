#!/usr/bin/python

#import important stuff
import os, gi
import signal
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

class IndicatorClass:

	indicatorId = ''
	iconPath    = 'sample_icon.svg'
	menuItems   = []
	dependency  = []
	def __init__(self, indicatorID):
		#print vars(BoxObject)
		#print BoxObject.name
		self.ID = indicatorID

	def setDependency(self, dependency):
		self.dependency = dependency
		#self.dependency.append(dependency)
		#print dependency

	def setIcon(self, path = None):
		if path != None:
			self.iconPath = path
		print path
		return self

	def menuItem(self, itemName = None, funtionName = None):
		item = {}
		if itemName == None or funtionName == None:
			print "name and function needed"
			return false

		item['name'] = itemName
		item['function'] = funtionName

		self.menuItems.append(item)
		print item
		return self

	def separator(self):
		self.menuItems.append('separator')
		print 'separator added'
		return self

	def buildMenu(self):
		self.menu = gtk.Menu()
		print self.menuItems
		#exit()
		for item in self.menuItems:
			print item
			if item != 'separator':

				methodToCall = getattr(self.dependency, item['function'])
				#result = methodToCall()

				item = gtk.MenuItem(item['name'])
				item.connect('activate', methodToCall)
				self.menu.append(item)
			else:
				separator =  gtk.SeparatorMenuItem()
				self.menu.append(separator)

		item_quit = gtk.MenuItem('Quit')
		item_quit.connect('activate', self.quit)
		self.menu.append(item_quit)

		self.menu.show_all()
		return self.menu

	def quit(self,s):
		gtk.main_quit()

	def show(self):
		print "show the menu"
		indicator = appindicator.Indicator.new(self.ID, os.path.abspath(self.iconPath), appindicator.IndicatorCategory.SYSTEM_SERVICES)

		indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

		indicator.set_menu(self.buildMenu())
		gtk.main()
