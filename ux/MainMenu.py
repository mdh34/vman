#!/usr/bin/python

#import important stuff
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

class MainMenu():
	ID = 'VmanMenu'
	def __init__(self):
		indicator = appindicator.Indicator.new(self.ID, os.path.abspath('sample_icon1.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
		indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		indicator.set_menu(self.build_menu())
		#gtk.main()

	def build_menu(self):
		menu = gtk.Menu()

		item_quit = gtk.MenuItem('Add Box')
		item_quit.connect('activate', self.add_box)
		menu.append(item_quit)

		item_quit = gtk.MenuItem('Configuration')
		item_quit.connect('activate', self.configuration)
		menu.append(item_quit)

		item_quit = gtk.MenuItem('About')
		item_quit.connect('activate', self.about)
		menu.append(item_quit)

		#item_quit = gtk.MenuItem('Play/pause')
		#item_quit.connect('activate', self.up_suspend)
		#menu.append(item_quit)
		#
		#separator =  gtk.SeparatorMenuItem()
		#menu.append(separator)

		item_quit = gtk.MenuItem('Exit')
		item_quit.connect('activate', self.quit)
		menu.append(item_quit)

		menu.show_all()
		return menu

	def add_box(self,s):
		print "add_box"

	def configuration(self,s):
		print "configuration"

	def about(self,s):
		print "about"

	def quit(self,s):
		gtk.main_quit()
