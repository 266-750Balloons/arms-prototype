#import whatever the code for transmitting is called
import gi

gi.require_version("Gtk", "3.0")
from gi import Gtk
builder = Gtk.builder
builder.add_from_file("arms_ui.glade")

message = []

def white() :
    message.append("White")

def black() :
    message.append("Black")

def gray() :
    message.append("Gray")

def silver():
    message.append("Silver")

def red():
    message.append("Red")

def blue():
    message.append("Blue")

def brown():
    message.append("Brown")

def green():
    message.append("Green")

def beige():
    message.append("Beige")

def orange():
    message.append("Orange")

def gold():
    message.append("Gold")

def yellow():
    message.append("Yellow")

def purple():
    message.append("Purple")

def other():
    message.append("Other")

