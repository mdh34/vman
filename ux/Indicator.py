#!/usr/bin/python

#import important stuff
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

class Indicator():
	ID = 'Indicator-Vman'
	def __init__(self):
		indicator = appindicator.Indicator.new(self.ID, os.path.abspath('../sample_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
		indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		indicator.set_menu(self.build_menu())
		gtk.main()

	def build_menu(self):
		menu = gtk.Menu()

		item_quit = gtk.MenuItem('open_location')
		item_quit.connect('activate', self.open_location)
		menu.append(item_quit)

		item_quit = gtk.MenuItem('halt')
		item_quit.connect('activate', self.halt)
		menu.append(item_quit)

		item_quit = gtk.MenuItem('SSH Connect')
		item_quit.connect('activate', self.ssh)
		menu.append(item_quit)

		item_quit = gtk.MenuItem('Play/pause')
		item_quit.connect('activate', self.up_suspend)
		menu.append(item_quit)

		separator =  gtk.SeparatorMenuItem()
		menu.append(separator)

		item_quit = gtk.MenuItem('Quit')
		item_quit.connect('activate', self.quit)
		menu.append(item_quit)

		menu.show_all()
		return menu

	def open_location(self,s):
		print "open_location"

	def halt(self,s):
		print "halt"

	def up_suspend(self,s):
		print "up_suspend"

	def ssh(self,s):
		print "ssh"

	def quit(self,s):
		gtk.main_quit()

#ind = Indicator()##kinda works... amanha vejo isto