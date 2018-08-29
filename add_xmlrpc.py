import xmlrpc.client
import sys
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QPushButton,QFormLayout,QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QRegExpValidator

class Addition(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.widget = QWidget()
        fbox = QFormLayout()

        regexp2 = QtCore.QRegExp('[0-9]{1,}')
        self.validator2 = QRegExpValidator(regexp2)
        l1 = QLabel("number 1: ")
        self.add1 = QLineEdit()
        self.add1.setValidator(self.validator2)
        fbox.addRow(l1,self.add1)

        l2 = QLabel("number 2: ")
        self.add2 = QLineEdit()
        self.add2.setValidator(self.validator2)
        fbox.addRow(l2,self.add2)

        b = QPushButton()
        b.setText("ADD")
        b.clicked.connect(self.addition)
        fbox.addRow(b)

        l3 = QLabel("Sum is: ")
        self.add3 = QLineEdit()
        self.add3.setReadOnly(True)
        fbox.addRow(l3,self.add3)

        self.widget.setLayout(fbox)
        self.widget.show()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Addition")

    def addition(self):
        num1 = int(self.add1.text())
        num2 = int(self.add2.text())
        api = xmlrpc.client.ServerProxy("http://username:password@0.0.0.0:8442/")
        sums = str(api.add(num1,num2))
        self.add3.setText(sums)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apps = Addition()
    apps.show()
    sys.exit(app.exec_())