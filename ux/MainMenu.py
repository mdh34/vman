#!/usr/bin/python

#import important stuff
import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

ID = 'VmanMenu'
def main():
	indicator = appindicator.Indicator.new(ID, os.path.abspath('drawing.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	gtk.main()

def build_menu():
	menu = gtk.Menu()

	item_quit = gtk.MenuItem('Add Box')
	item_quit.connect('activate', add_box)
	menu.append(item_quit)

	item_quit = gtk.MenuItem('Configuration')
	item_quit.connect('activate', configuration)
	menu.append(item_quit)

	item_quit = gtk.MenuItem('About')
	item_quit.connect('activate', about)
	menu.append(item_quit)

	#item_quit = gtk.MenuItem('Play/pause')
	#item_quit.connect('activate', self.up_suspend)
	#menu.append(item_quit)
	#
	#separator =  gtk.SeparatorMenuItem()
	#menu.append(separator)

	item_quit = gtk.MenuItem('Exit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)

	menu.show_all()
	return menu

def add_box(self):
	#window allowing to add boxes with the fields title url image and init folder
	print "add_box"

def configuration(self):
	#window allowing to do basic configs
	print "configuration"

def about(self):
	print "about window"

def quit(self):
	#kill all the other inicators
	gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
