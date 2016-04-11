#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from subprocess import call
from PIL import Image
import glob, os, inspect

class StackWindow(Gtk.Window):

    def __init__(self):
        #set title
        Gtk.Window.__init__(self, title="Vman - Add Box")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        #add a label
        label = Gtk.Label()
        label.set_markup('<big>Add a Vagrant Box</big>')
        vbox.add(label)

        #add a stack
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(100)

        #adds the folder selector dialog
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 50)
        add_button = Gtk.Button(label="Select project Location")
        add_button.connect("clicked", self.on_addButton_clicked)
        hbox.add(add_button)
        row.add(hbox)
        #listbox.add(row)
        stack.add_titled(row, "add", "Location")

        #adds the check list and the field in the bottom
        ChecklistBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "ubuntu/trusty64")
        button1.connect("toggled", self.on_button_toggled, "1")
        ChecklistBox.pack_start(button1, False, False, 0)

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("ubuntu/trusty32")
        button2.connect("toggled", self.on_button_toggled, "2")
        ChecklistBox.pack_start(button2, False, False, 0)

        button3 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1,
            "laravel/homestead")
        button3.connect("toggled", self.on_button_toggled, "3")
        ChecklistBox.pack_start(button3, False, False, 0)

        button4 = Gtk.RadioButton.new_from_widget(button1)
        button4.set_label('Select from Hashicorp')
        button4.connect("toggled", self.on_button_toggled, "4")
        ChecklistBox.pack_start(button4, False, False, 0)

        label = Gtk.Label()
        #label.set_markup('<small><a href="http://www.gtk.org" "title="Click to find out more">internets</a></small>')
        label.set_markup("<small>Select a box from <a href=\"https://atlas.hashicorp.com/boxes/search?provider=virtualbox\" "
                         "title=\"Click to find out more\">Hashicorp</a></small>")
        ChecklistBox.add(label)

        checkbutton = Gtk.Entry()
        checkbutton.set_text("Box/Name")
        #vbox.pack_start(self.entry, True, True, 0)
        ChecklistBox.add(checkbutton)
        stack.add_titled(ChecklistBox, "check", "Select a Box")


        label = Gtk.Label()
        #read images from folder
        image_list = []
        pwd = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        print pwd[:-2]+"data/images"
        os.chdir(pwd[:-2]+"data/images")
        print glob.glob('*.svg')
        for filename in glob.glob('*.svg'):
            #reference
            #  http://stackoverflow.com/questions/3029574/custom-pygtk-button
            image = Gtk.Image()
            imgContainer = gtk.EventBox()
            image.set_from_file(pwd[:-2]+"data/images/"+filename)
            imgContainer.add(image)
            #button.set_image(image)
            #button.set_label("")
            pass
        label.set_markup("<big>Select a Picture</big>")
        stack.add_titled(label, "label", "Picture")
        ############

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

        canselButton = Gtk.Button(label="Cancel")
        canselButton.connect("clicked", self.on_canselButton_clicked)
        vbox.pack_end(canselButton, True, True, 0)

        canselButton = Gtk.Button(label="Init")
        vbox.pack_end(canselButton, True, True, 0)

############################
    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def on_canselButton_clicked(self, widget):
        quit()
############################
    def on_addButton_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
        )

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            widget.set_label(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

win = StackWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

#        vbox =Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#        self.add(vbox)
#
#        stack = Gtk.Stack()
#        stack.set_transition_duration(1000)
#        #set transition accepts values from 0 to 19
#        #more info http://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.StackTransitionType
#        stack.set_transition_type(6)
