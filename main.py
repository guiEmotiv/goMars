#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys

class VentanaPrincipal(QtGui.QWidget):

    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        self.iniUI()

    def iniUI(self):
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle('INTERFACE NASA')
        self.setWindowIcon(QtGui.QIcon('img/logo.jpg'))

        self.show()

    def closeEvent(self, QCloseEvent):

        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = VentanaPrincipal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()






