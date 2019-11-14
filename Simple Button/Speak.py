from PySide2 import QtCore

class Speak():
    def __init__(self):
        pass

    @QtCore.Slot()
    def say_hi(self):
        print("Button clicked, Hi!")