import sys
from PyQt5 import QtWidgets, uic, QtCore
import radioSend

message = []

#Starting Application
application = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("arms_ui.ui")
window.showFullScreen()

#Function to render contents of message into the message box
def renderMessage() :
     window.message.setText(str(message))

#Function to send message. Shows error to user if something goes wrong
def send() :
     global message
     window.send.setText("Sending...")
     status = radioSend.transmit(message)
     #If nothing happens, clear the message
     message = []
     window.send.setText("Send")
     renderMessage()

#Removes the last word in the message
def backspace() :
     if len(message) != 0 :
          message.pop(len(message)-1)
     renderMessage()


#A whole bunch of functiosn to add chunks to the message
def white() :
    message.append("White")
    message.append("Other Vehicle")
    renderMessage()

def black() :
    message.append("Black")
    message.append("Other Vehicle")
    renderMessage()

def gray() :
    message.append("Gray")
    message.append("Other Vehicle")
    renderMessage()
     
def silver():
    message.append("Silver")
    message.append("Other Vehicle")
    renderMessage()
     
def red():
    message.append("Red")
    message.append("Other Vehicle")
    renderMessage()

def blue():
    message.append("Blue")
    message.append("Other Vehicle")
    renderMessage()

def brown():
    message.append("Brown")
    message.append("Other Vehicle")
    renderMessage()

def green():
    message.append("Green")
    message.append("Other Vehicle")
    renderMessage()


def beige():
    message.append("Beige")
    message.append("Other Vehicle")
    renderMessage()

def orange():
    message.append("Orange")
    message.append("Other Vehicle")
    renderMessage()

def gold():
    message.append("Gold")
    message.append("Other Vehicle")
    renderMessage()

def yellow():
    message.append("Yellow")
    message.append("Other Vehicle")
    renderMessage()

def purple():
    message.append("Purple")
    message.append("Other Vehicle")
    renderMessage()

def other():
    message.append("Other-colored or patterned")
    message.append("Other Vehicle")
    renderMessage()

def letter_A() :
     message.append("A")
     renderMessage()

def letter_B() :
     message.append("B")
     renderMessage()

def letter_C() :
     message.append("C")
     renderMessage()

def letter_D() :
     message.append("D")
     renderMessage()

def letter_E() :
     message.append("E")
     renderMessage()

def letter_F() :
     message.append("F")
     renderMessage()

def letter_G() :
     message.append("G")
     renderMessage()

def letter_H() :
     message.append("H")
     renderMessage()

def letter_I() :
     message.append("I")
     renderMessage()

def letter_J() :
     message.append("J")
     renderMessage()

def letter_K() :
     message.append("K")
     renderMessage()

def letter_L() :
     message.append("L")
     renderMessage()

def letter_M() :
     message.append("M")
     renderMessage()

def letter_N() :
     message.append("N")
     renderMessage()

def letter_O() :
     message.append("O")
     renderMessage()

def letter_P() :
     message.append("P")
     renderMessage()

def letter_Q() :
     message.append("Q")
     renderMessage()

def letter_R() :
     message.append("R")
     renderMessage()

def letter_S() :
     message.append("S")
     renderMessage()

def letter_T() :
     message.append("T")
     renderMessage()

def letter_U() :
     message.append("U")
     renderMessage()

def letter_V() :
     message.append("V")
     renderMessage()

def letter_W() :
     message.append("W")
     renderMessage()

def letter_X() :
     message.append("X")
     renderMessage()

def letter_Y() :
     message.append("Y")
     renderMessage()

def letter_Z() :
     message.append("Z")
     renderMessage()

def letter_1() :
     message.append("1")
     renderMessage()

def letter_2() :
     message.append("2")
     renderMessage()

def letter_3() :
     message.append("3")
     renderMessage()

def letter_4() :
     message.append("4")
     renderMessage()

def letter_5() :
     message.append("5")
     renderMessage()

def letter_6() :
     message.append("6")
     renderMessage()

def letter_7() :
     message.append("7")
     renderMessage()

def letter_8() :
     message.append("8")
     renderMessage()

def letter_9() :
     message.append("9")
     renderMessage()

def letter_0() :
     message.append("0")
     renderMessage()

def letter_0() :
     message.append("0")
     renderMessage()

def unsafe_driver() :
    message.append("Unsafe Driver")
    renderMessage()

def wrongway_driver() :
    message.append("Wrong-way Driver")
    renderMessage()

def unsafe_person() :
    message.append("Unsafe Person")
    renderMessage()

def obstacle() :
     message.append("Obstacle")
     renderMessage()

def spill() :
     message.append("Spill")
     renderMessage()
     
def loose_gravel() :
     message.append("Loose Gravel")
     renderMessage()

def closure() :
     message.append("Closure")
     renderMessage()

def ahead() :
     message.append("Ahead")
     renderMessage()

def prepo_in():
     message.append("In")
     renderMessage()

def prepo_at() :
     message.append("At")
     renderMessage()

def near() :
     message.append("Near")
     renderMessage()

def prepo_on() :
     message.append("On")
     renderMessage()

def crashed() :
     message.append("Crashed")
     renderMessage()

def stalled() :
     message.append("Stalled/stopped")
     renderMessage()

def disabled() :
     message.append("Disabled")
     renderMessage()

def on_fire() :
     message.append("On fire/burning")
     renderMessage()

def left_lane() :
     message.append("Left Lane(s)")
     renderMessage()

def right_lane() :
     message.append("Right Lane(s)")
     renderMessage()

def center_lane() :
     message.append("Center Lane(s)")
     renderMessage()

def plate_ending() :
     message.append("Plate ending in")
     renderMessage()

#Connecting all functions to their respective Qt Signals
window.white.clicked.connect(white)
window.beige.clicked.connect(beige)
window.black.clicked.connect(black)
window.blue.clicked.connect(blue)
window.brown.clicked.connect(brown)
window.gold.clicked.connect(gold)
window.gray.clicked.connect(gray)
window.green.clicked.connect(green)
window.orange.clicked.connect(orange)
window.other.clicked.connect(other)
window.purple.clicked.connect(purple)
window.red.clicked.connect(red)
window.silver.clicked.connect(silver)
window.yellow.clicked.connect(yellow)
window.a.clicked.connect(letter_A)
window.b.clicked.connect(letter_B)
window.c.clicked.connect(letter_C)
window.d.clicked.connect(letter_D)
window.e.clicked.connect(letter_E)
window.f.clicked.connect(letter_F)
window.g.clicked.connect(letter_G)
window.h.clicked.connect(letter_H)
window.i.clicked.connect(letter_I)
window.j.clicked.connect(letter_J)
window.k.clicked.connect(letter_K)
window.l.clicked.connect(letter_L)
window.m.clicked.connect(letter_M)
window.n.clicked.connect(letter_N)
window.o.clicked.connect(letter_O)
window.p.clicked.connect(letter_P)
window.q.clicked.connect(letter_Q)
window.r.clicked.connect(letter_R)
window.s.clicked.connect(letter_S)
window.t.clicked.connect(letter_T)
window.u.clicked.connect(letter_U)
window.v.clicked.connect(letter_V)
window.w.clicked.connect(letter_W)
window.x.clicked.connect(letter_X)
window.y.clicked.connect(letter_Y)
window.z.clicked.connect(letter_Z)
window.n1.clicked.connect(letter_1)
window.n2.clicked.connect(letter_2)
window.n3.clicked.connect(letter_3)
window.n4.clicked.connect(letter_4)
window.n5.clicked.connect(letter_5)
window.n6.clicked.connect(letter_6)
window.n7.clicked.connect(letter_7)
window.n8.clicked.connect(letter_8)
window.n9.clicked.connect(letter_9)
window.n0.clicked.connect(letter_0)
window.closure.clicked.connect(closure)
window.looseGravel.clicked.connect(loose_gravel)
window.obstacle.clicked.connect(spill)
window.unsafeDriver.clicked.connect(unsafe_driver)
window.unsafePerson.clicked.connect(unsafe_person)
window.wrongWay.clicked.connect(wrongway_driver)
window.at.clicked.connect(prepo_at)
window.ahead.clicked.connect(ahead)
window.prepoIn.clicked.connect(prepo_in)
window.near.clicked.connect(near)
window.on.clicked.connect(prepo_on)
window.crashed.clicked.connect(crashed)
window.disabled.clicked.connect(disabled)
window.onFire.clicked.connect(on_fire)
window.stalled.clicked.connect(stalled)
window.left.clicked.connect(left_lane)
window.center.clicked.connect(center_lane)
window.right.clicked.connect(right_lane)
window.send.clicked.connect(send)
window.plate.clicked.connect(plate_ending)
window.backspace.clicked.connect(backspace)

application.exec()