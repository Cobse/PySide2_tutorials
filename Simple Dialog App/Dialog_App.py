import sys
from PySide2 import QtWidgets

class Form(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        # Create widgets
        self.edit = QtWidgets.QLineEdit("Write my name here")
        self.button = QtWidgets.QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.print_greetings)

    def greetings(self):
        hello = "Hello %s" % self.edit.text()
        return hello

    def print_greetings(self):
        print(self.greetings())

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())