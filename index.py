
from home import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
import screen_brightness_control as sbc
import os

class Main(object):
	def __init__(self):
		self.Dialog = QtWidgets.QDialog()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self.Dialog)
		self.Dialog.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
		self.Dialog.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
		self.light = self.ui.light

		self.controller = self.ui.lightControler
		self.controller.setMinimum(0)
		self.controller.setMaximum(100)

		self.all_screens_brightness = sbc.get_brightness()
		self.controller.setValue(self.all_screens_brightness)
		self.light.setText(str(self.all_screens_brightness ))
		self.controller.valueChanged.connect(self.brightness)
		self.ui.nightLight.clicked.connect(lambda:self.night_light())

		self.Dialog.show()
		res =  self.Dialog.exec_()
		



	def brightness(self, val):
		self.light.setText(str(val))
		sbc.set_brightness(val, force=True)

	def night_light(self):
		os.system('start ms-settings:nightlight')


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = Main()
	
