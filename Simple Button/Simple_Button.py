import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from Speak import *

@QtCore.Slot()
def say_hello():
 print("Button clicked, Hello!")

# Instantiate class Speak
speaking = Speak


# Create the Qt Application
app = QtWidgets.QApplication(sys.argv)
# Create a button, connect it and show it
button = QtWidgets.QPushButton("Click me")
button.clicked.connect(speaking.say_hi)
button.show()
# Run the main Qt loop
app.exec_()



    