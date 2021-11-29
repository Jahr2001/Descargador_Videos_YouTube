import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import os
#### Importar Downloader

qtCreatorFile = "./view/mainView.ui" # Nombre del archivo ui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Descargador de videos - Programación Concurrente - 193245 - 193213 .:: Version 1.0 ::.')
        #self.botonSalir.setIcon(QIcon('add.png'))       
        self.botonSalir.clicked.connect(self.salir)
        self.botonAgregar.clicked.connect(self.dirActual)
        
    def obtenerUrl(self):
        urlVideo = self.url.text()
        print(urlVideo)
        return urlVideo
    
    def dirActual(self):
        dir = os.getcwd()
        print(dir)
    
    def dir(self):
        ed = QFileDialog.getExistingDirectory(self)
        print(ed)
    
    def salir(self):
        self.close()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())