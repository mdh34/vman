#!/usr/bin/python

#import important stuff
import os
import signal
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
#from gi.repository import Gtk #as Gtk
from gi.repository import AppIndicator3 as appindicator
from subprocess import call



vmanLocal = sys.argv[1]

ID = 'VmanMenu'
def main():
	indicator = appindicator.Indicator.new(ID, os.path.abspath('drawing.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())
	Gtk.main()

def build_menu():
	menu = Gtk.Menu()

	item_quit = Gtk.MenuItem('Add Box')
	item_quit.connect('activate', add_box)
	menu.append(item_quit)

	item_quit = Gtk.MenuItem('Configuration')
	item_quit.connect('activate', configuration)
	menu.append(item_quit)

	item_quit = Gtk.MenuItem('About')
	item_quit.connect('activate', about)
	menu.append(item_quit)

	#item_quit = Gtk.MenuItem('Play/pause')
	#item_quit.connect('activate', self.up_suspend)
	#menu.append(item_quit)
	#
	#separator =  Gtk.SeparatorMenuItem()
	#menu.append(separator)

	item_quit = Gtk.MenuItem('Exit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)

	menu.show_all()
	return menu

def add_box(self):
	#window allowing to add boxes with the fields title url image and init folder
	call(["python", vmanLocal + "Window.py", "&"])
	print "add_box"

def configuration(self):
	#window allowing to do basic configs
	print "configuration"

def about(self):
	print "about window"

def quit(self):
	#kill all the other inicators
	Gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
