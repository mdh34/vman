#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from subprocess import call

class StackWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label()
        label.set_markup('<big>Add a Vagrant Box</big>')
        vbox.add(label)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 50)
        add_button = Gtk.Button(label="Select project Location")
        add_button.connect("clicked", self.on_addButton_clicked)
        hbox.add(add_button)
        row.add(hbox)
        #listbox.add(row)

        stack.add_titled(row, "add", "Location")

        StackBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        checkbutton = Gtk.CheckButton("ubuntu/trusty64")
        StackBox.add(checkbutton)
        checkbutton = Gtk.CheckButton("ubuntu/trusty32")
        StackBox.add(checkbutton)
        checkbutton = Gtk.CheckButton("laravel/homestead")
        StackBox.add(checkbutton)

        checkbutton = Gtk.Entry()
        checkbutton.set_text("type box name from https://atlas.hashicorp.com/boxes/search?provider=virtualbox")
        #vbox.pack_start(self.entry, True, True, 0)
        StackBox.add(checkbutton)
        stack.add_titled(StackBox, "check", "Select a Box")

        label = Gtk.Label()
        label.set_markup("<big>Select a Picture</big>")
        stack.add_titled(label, "label", "Picture")


        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)

        canselButton = Gtk.Button(label="Cancel")
        canselButton.connect("clicked", self.on_canselButton_clicked)
        vbox.pack_end(canselButton, True, True, 0)

        canselButton = Gtk.Button(label="Init")
        vbox.pack_end(canselButton, True, True, 0)


    def on_canselButton_clicked(self, widget):
        quit()

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
