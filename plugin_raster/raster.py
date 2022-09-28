import imp
import os 
import sys

'''librerias de QyQt5'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''librerias de Qgis'''
from qgis.core import *
from qgis.gui import *
from qgis.utils import * 

from .interfaz import Ui_MainWindow #importamos de interfaz.py

class interfaz (QMainWindow): #se crea una clase para poder hacer uso de la clase Ui_MainWindow
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.Btn4.clicked.connect(self.cerrar)#Se cerrara el plugin al dar clic sobre el boton4(cerrar)
    
    def cerrar (self):
        self.close()


