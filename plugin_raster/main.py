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

from .raster import interfaz

class mainMenu:
    def __init__(self, iface):
        self.iface= iface
    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("Raster")#este el el titulo del menu
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.IMenu)
        self.IMenuBar= self.iface.addToolBar("Raster")

        self.ejemploRaster = QAction(QIcon(""), "Raster", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)
        
    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers= QgsProject.instance().mapLayers().values()#se almacenarán todas las capas del proyecto
        for layer in layers:#corremos las capas para ver si son de tipo raster o vector
            if layer.type()== QgsMapLayer.VectorLayer and layer.geometryType()==QgsWkbTypes.PolygonGeometry:#la capa debe ser tipo vectoy y poligono
                vLayer = layer
            if layer.type() == QgsRasterLayer.RasterLayer:#la capa debe der tipo raster para que entre en la condicion
                rLayer= layer
                self.dialogo.ui.cmbbx1.addItem(rLayer.name())#se agregara al combobox el nombre de la capa raster
                crs = QgsCoordinateReferenceSystem()
                self.dialogo.ui.groupBox.
        
        
def unload(self):
    QgsApplication.processingRegistry().removeProvider(self.provider)