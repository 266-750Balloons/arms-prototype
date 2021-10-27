#import whatever the code for transmitting is called
import gi
import radioSend

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

def letter_A() :
     message.append("A")

def letter_B() :
     message.append("B")

def letter_C() :
     message.append("C")

def letter_D() :
     message.append("D")

def letter_E() :
     message.append("E")

def letter_F() :
     message.append("F")

def letter_G() :
     message.append("G")

def letter_H() :
     message.append("H")

def letter_I() :
     message.append("I")

def letter_J() :
     message.append("J")

def letter_K() :
     message.append("K")

def letter_L() :
     message.append("L")

def letter_M() :
     message.append("M")

def letter_N() :
     message.append("N")

def letter_O() :
     message.append("O")

def letter_P() :
     message.append("P")

def letter_Q() :
     message.append("Q")

def letter_R() :
     message.append("R")

def letter_S() :
     message.append("S")

def letter_T() :
     message.append("T")

def letter_U() :
     message.append("U")

def letter_V() :
     message.append("V")

def letter_W() :
     message.append("W")

def letter_X() :
     message.append("X")

def letter_Y() :
     message.append("Y")

def letter_Z() :
     message.append("Z")

def letter_1() :
     message.append("1")

def letter_2() :
     message.append("2")

def letter_3() :
     message.append("3")

def letter_4() :
     message.append("4")

def letter_5() :
     message.append("5")

def letter_6() :
     message.append("6")

def letter_7() :
     message.append("7")

def letter_8() :
     message.append("8")

def letter_9() :
     message.append("9")

def letter_0() :
     message.append("0")

def letter_0() :
     message.append("0")

def unsafe_driver() :
    message.append("Unsafe Driver")

def wrongway_driver() :
    message.append("Wrong-way Driver")

def unsafe_person() :
    message.append("Unsafe Person")