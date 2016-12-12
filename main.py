#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import serial, time
#from functools import partial

arduino = serial.Serial("/dev/cu.usbmodem17", 9600)
time.sleep(0.3)

class ventanaPrincipal(QtGui.QWidget):

    def __init__(self,parent=None):
        super(ventanaPrincipal, self).__init__(parent)

        grid = QtGui.QGridLayout()
        grid.addWidget(self.gridTemperatura(),0,0)
        grid.addWidget(self.gridPresion(),0,1)
        grid.addWidget(self.gridCo2(),1,0)
        grid.addWidget(self.gridO2(),1,1)
        grid.addWidget(self.gridCam(),0,2)
        grid.addWidget(self.gridIsometrico(),1,2)
        self.setLayout(grid)

        self.setWindowTitle("Software de Control de Clima Marciano v1.0")
        self.resize(1280,900)

    def gridTemperatura(self):

        self.groupbox = QtGui.QGroupBox("Temperatura | 'C")

        self.logoTemp = QtGui.QLabel(self)
        self.logoTemp.setPixmap(QtGui.QPixmap('img/t.png'))
        self.logoTemp.move(50, 50)
        self.logoTemp.resize(50,50)

        self.lcdAutoTemp = QtGui.QLCDNumber(self)
        self.lcdAutoTemp.display(self.serial())
        self.lcdTemp = QtGui.QLCDNumber(self)
        self.sldTemp = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldTemp.valueChanged.connect(self.lcdTemp.display)

        self.valvulaAutoTemp = QtGui.QRadioButton("Valor del Sensor")

        self.valvulaOnTemp = QtGui.QRadioButton("Valvula ON")
        self.valvulaOffTemp = QtGui.QRadioButton("Valvula OFF")

        self.valvulaAutoTemp.setChecked(True)


        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.logoTemp)
        vbox.addWidget(self.valvulaAutoTemp)
        vbox.addWidget(self.lcdAutoTemp)
        vbox.addWidget(self.valvulaOnTemp)
        vbox.addWidget(self.valvulaOffTemp)
        vbox.addWidget(self.lcdTemp)
        vbox.addWidget(self.sldTemp)
        vbox.addStretch(1)
        self.groupbox.setLayout(vbox)
        return self.groupbox


    def gridPresion(self):
        self.groupbox = QtGui.QGroupBox("Nivel de Presion | bar")

        self.logoPres = QtGui.QLabel(self)
        self.logoPres.setPixmap(QtGui.QPixmap('img/p.png'))
        self.logoPres.move(50, 50)
        self.logoPres.resize(50, 50)

        self.lcdAutoPres = QtGui.QLCDNumber(self)
        self.lcdPres = QtGui.QLCDNumber(self)
        self.sldPres = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldPres.valueChanged.connect(self.lcdPres.display)

        self.valvulaAutoPres = QtGui.QRadioButton("Valor del Sensor")
        self.valvulaOnPres = QtGui.QRadioButton("Valvula ON")
        self.valvulaOffPres = QtGui.QRadioButton("Valvula OFF")

        self.valvulaAutoPres.setChecked(True)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.logoPres)
        vbox.addWidget(self.valvulaAutoPres)
        vbox.addWidget(self.lcdAutoPres)
        vbox.addWidget(self.valvulaOnPres)
        vbox.addWidget(self.valvulaOffPres)
        vbox.addWidget(self.lcdPres)
        vbox.addWidget(self.sldPres)
        vbox.addStretch(1)
        self.groupbox.setLayout(vbox)
        return self.groupbox

    def gridCo2(self):

        self.groupbox = QtGui.QGroupBox("Nivel de Dioxido de Carbono | % ppm")

        self.logoCo2 = QtGui.QLabel(self)
        self.logoCo2.setPixmap(QtGui.QPixmap('img/co2.png'))
        self.logoCo2.move(50, 50)
        self.logoCo2.resize(50, 50)

        self.lcdAutoCo2 = QtGui.QLCDNumber(self)
        self.lcdCo2 = QtGui.QLCDNumber(self)
        self.sldCo2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldCo2.valueChanged.connect(self.lcdCo2.display)

        self.valvulaAutoCo2 = QtGui.QRadioButton("Valor del Sensor")
        self.valvulaOnCo2 = QtGui.QRadioButton("Valvula ON")
        self.valvulaOffCo2 = QtGui.QRadioButton("Valvula OFF")

        self.valvulaAutoCo2.setChecked(True)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.logoCo2)
        vbox.addWidget(self.valvulaAutoCo2)
        vbox.addWidget(self.lcdAutoCo2)
        vbox.addWidget(self.valvulaOnCo2)
        vbox.addWidget(self.valvulaOffCo2)
        vbox.addWidget(self.lcdCo2)
        vbox.addWidget(self.sldCo2)
        vbox.addStretch(1)
        self.groupbox.setLayout(vbox)
        return self.groupbox

    def gridO2(self):

        self.groupbox = QtGui.QGroupBox("Nivel de Oxigeno | % ppm")

        self.logoO2 = QtGui.QLabel(self)
        self.logoO2.setPixmap(QtGui.QPixmap('img/o2.png'))
        self.logoO2.move(50, 50)
        self.logoO2.resize(50, 50)

        self.lcdAutoO2 = QtGui.QLCDNumber(self)
        self.lcdO2 = QtGui.QLCDNumber(self)
        self.sldO2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.sldO2.valueChanged.connect(self.lcdO2.display)

        self.valvulaAutoO2 = QtGui.QRadioButton("Valor del Sensor")
        self.valvulaOnO2 = QtGui.QRadioButton("Valvula ON")
        self.valvulaOffO2 = QtGui.QRadioButton("Valvula OFF")

        self.valvulaAutoO2.setChecked(True)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.logoO2)
        vbox.addWidget(self.valvulaAutoO2)
        vbox.addWidget(self.lcdAutoO2)
        vbox.addWidget(self.valvulaOnO2)
        vbox.addWidget(self.valvulaOffO2)
        vbox.addWidget(self.lcdO2)
        vbox.addWidget(self.sldO2)
        vbox.addStretch(1)
        self.groupbox.setLayout(vbox)
        return self.groupbox

    def gridCam(self):

        groupbox = QtGui.QGroupBox("Vista Interna | camara")

        return groupbox

    def gridIsometrico(self):

        self.groupbox = QtGui.QGroupBox("Vista Isometrica | pos")

        self.logoO2 = QtGui.QLabel(self)
        self.logoO2.setPixmap(QtGui.QPixmap('img/iso.png'))
        self.logoO2.move(50, 50)
        self.logoO2.adjustSize()

        self.senTemp1 = QtGui.QPushButton('Sensor de Temp 1',self)
        self.senTemp1.clicked[bool].connect(self.pushSenTemp1)
        self.senTemp1.setCheckable(True)

        self.senTemp2 = QtGui.QPushButton("Sensor de Temp 2")
        self.senTemp3 = QtGui.QPushButton("Sensor de Temp 3")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.logoO2)
        vbox.addWidget(self.senTemp1)
        vbox.addWidget(self.senTemp2)
        vbox.addWidget(self.senTemp3)
        vbox.addStretch(0)
        self.groupbox.setLayout(vbox)
        return self.groupbox

    def serial(self):

        self.arduino = serial.Serial('/dev/cu.usbmodem17', 9600)
        self.arduino.setDTR(False)
        time.sleep(0.3)

        self.arduino.flushInput()
        self.arduino.setDTR()
        time.sleep(0.3)

        self.rawString = self.arduino.readline().replace("\r", '').replace("\n", '')
        print self.rawString

        return self.rawString

    def pushSenTemp1(self, pressed):

        source = self.sender()
        if pressed:
            val = 'Y'
        else:
            val = 'N'
        if source.setText('Sensor de Temp 1'):
            arduino.write(val)
        else:
            arduino.write(val)





if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    clock = ventanaPrincipal()
    clock.show()
    sys.exit(app.exec_())

