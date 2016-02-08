import os
import signal
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('sample_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_quit = gtk.MenuItem('Vagrant Um')
    #item = gtk.MenuItem('um_ponto_um')
    #item_quit.set_submenu(box_controllers)
    
    item_quit.connect('activate', box_controllers)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Vagrant Dois')
    #item_quit.connect('activate', quit)
    menu.append(item_quit)

    item_quit = gtk.MenuItem('Vagrant Tres')
    #item_quit.connect('activate', quit)
    menu.append(item_quit)

    separator =  gtk.SeparatorMenuItem()
    menu.append(separator)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu


def box_controllers(self):
    submenu = gtk.Menu()

    item_quit = gtk.MenuItem('Open location')
    #item_quit.connect('activate', quit)
    submenu.append(item_quit)

    item_quit = gtk.MenuItem('Up/Suspend')
    #item_quit.connect('activate', quit)
    submenu.append(item_quit)

    item_quit = gtk.MenuItem('Halt')
    #item_quit.connect('activate', quit)
    submenu.append(item_quit)

    separator =  gtk.SeparatorMenuItem()
    submenu.append(separator)

    item_quit = gtk.MenuItem('Open Location')
    #item_quit.connect('activate', quit)
    submenu.append(item_quit)

    submenu.show_all()
    return submenu

def open_location():
    print "open_location"

def halt():
    print "halt"

def up_suspend():
    print "up_suspend"

def ssh(source):
    print "ssh"

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()