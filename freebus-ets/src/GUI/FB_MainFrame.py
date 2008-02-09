#!/usr/bin/
#-*- coding: iso-8859-1 -*-
#===============================================================================
#      __________  ________________  __  _______
#     / ____/ __ \/ ____/ ____/ __ )/ / / / ___/
#    / /_  / /_/ / __/ / __/ / __  / / / /\__ \
#   / __/ / _, _/ /___/ /___/ /_/ / /_/ /___/ /
#  /_/   /_/ |_/_____/_____/_____/\____//____/
#
#Source File: FB_MainFrame.py
#Version: V0.1 , 09.02.2008
#Author: Jerome Leisner
#email: j.leisner@ing-automation.de
#===============================================================================


import pygtk
pygtk.require('2.0')
import gtk

class FB_MainFrame:

    __WindowWidth = 0
    __WindowHeigth = 0

    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.
    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
    # If you return FALSE in the "delete_event" signal handler,
    # GTK will emit the "destroy" signal. Returning TRUE means
    # you don't want the window to be destroyed.
    # This is useful for popping up 'are you sure you want to quit?'
    # type dialogs.
        print "delete event occurred"

    # Change FALSE to TRUE and the main window will not be destroyed
    # with a "delete_event".
        return False

    # Another callback
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
    # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(1280,1024)
        self.window.maximize()
        self.window.set_title("Freebus-ETS")

        screen = self.window.get_screen()
        self.__WindowHeigth = screen.get_height()
        self.__WindowWidth = screen.get_width
    # When the window is given the "delete_event" signal (this is given
    # by the window manager, usually by the "close" option, or on the
    # titlebar), we ask it to call the delete_event () function
    # as defined above. The data passed to the callback
    # function is NULL and is ignored in the callback function.
        self.window.connect("delete_event", self.delete_event)

    # Here we connect the "destroy" event to a signal handler.
    # This event occurs when we call gtk_widget_destroy() on the window,
    # or if we return FALSE in the "delete_event" callback.
        self.window.connect("destroy", self.destroy)

    # Sets the border width of the window.
        self.window.set_border_width(10)

    # Creates a new button with the label "Hello World".
        #self.button = gtk.Button("Hello World11")

    # When the button receives the "clicked" signal, it will call the
    # function hello() passing it None as its argument.  The hello()
    # function is defined above.
       # self.button.connect("clicked", self.hello, None)

    # This will cause the window to be destroyed by calling
    # gtk_widget_destroy(window) when "clicked".  Again, the destroy
    # signal could come from here, or the window manager.
        #self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

    # This packs the button into the window (a GTK container).
        #self.window.add(self.button)

    # The final step is to display this newly created widget.
        #self.button.show()

    # and the window
        self.window.show()

    def main(self):
    # All PyGTK applications must have a gtk.main(). Control ends here
    # and waits for an event to occur (like a key press or mouse event).
        gtk.main()