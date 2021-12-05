import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QHeaderView, QTableWidgetItem

import os
import re
import downloader as dl

qtCreatorFile = "./view/mainView.ui" # Nombre del archivo ui
SAVE_PATH = '\Video'

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Descargador de videos - Programación Concurrente - 193245 - 193213 .:: Version 1.0 ::.')
        #data.append(('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'))

        #self.tableWidget.setHorizontalHeaderLabels(['Titulosss','Nombre Canal','URL Canal','Tiempo','URL video'])
        ### AJUSTAR LA TABLA A LA VENTANA #####
        '''self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)'''

        #Botones
        self.botonSalir.clicked.connect(self.salir)
        self.botonAgregar.clicked.connect(self.obtenerUrl)
        self.botonCambiarRuta.clicked.connect(self.cambiarDirectorio)
        self.botonIniciarDescarga.clicked.connect(dl.subProcesosMultiples)
        #self.botonIniciarDescarga.clicked.connect(self.arreglo)
        
        self.dirActual()
        self.guardarDirectorio()

        data = [
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc'),
            ('Educar en valores: corto sobre bullying', 'Maestra de Corazón','https://www.youtube.com/channel/UC6zMIzDKIswol2YSLpkzH2Q','1.6166666666666667 Min','https://www.youtube.com/watch?v=mcWXvFC45hc')
        ]

        #dl.data
        self.tableWidget.setRowCount(len(data))

        for i, (Titulo, NombreCanal, urlChannel, time, urlVideo) in enumerate(data):
            self.tableWidget.setItem(i,0, QTableWidgetItem(Titulo))
            self.tableWidget.setItem(i,1,QTableWidgetItem(NombreCanal))
            self.tableWidget.setItem(i,2,QTableWidgetItem(urlChannel))
            self.tableWidget.setItem(i,3,QTableWidgetItem(time))
            self.tableWidget.setItem(i,4,QTableWidgetItem(urlVideo))


   
    def obtenerUrl(self):
        urlVideo = self.url.text()
        if not urlVideo:
            self.url.setStyleSheet('border: 3px solid yellow; font: 12pt "MS Shell Dlg 2"; color: rgb(0, 0, 255); background-color: rgb(255, 255, 255);')
            QMessageBox.warning(None, 'Campo Vacio', 'Campo Vacio!!\n Por favor, ingrese una url de video de YouTube para la descarga!')
        else:
            regex = re.compile(r'(^https:\/\/www\.youtube\.com\/watch\?v\=)([a-zA-Z0-9_\-]){11}$')
            result = re.fullmatch(regex, urlVideo)

            if result:
                self.url.setStyleSheet('border: 3px solid green; font: 12pt "MS Shell Dlg 2"; color: rgb(0, 0, 255); background-color: rgb(255, 255, 255);')
                print(f'URL: {urlVideo}')
                dl.urls.append(urlVideo)
                
                self.url.clear()
            else:
                self.url.setStyleSheet('border: 3px solid red; font: 12pt "MS Shell Dlg 2"; color: rgb(0, 0, 255); background-color: rgb(255, 255, 255);')
                QMessageBox.critical(None, 'URL Invalidad', 'La URL '+str(urlVideo)+' es invalida, verifique nuevamente que la cadena ingresada sea una url de videos de YouTube!!')
                self.url.clear()

    def dirActual(self):
        dir = os.getcwd()
        self.rutaGuardar.addItem(dir+SAVE_PATH)
        self.rutaGuardar.setCurrentIndex(0)
        
        guardarEn = self.rutaGuardar.currentText()
        dl.directorio_actual = guardarEn
        print(f'GUARDAR EN: {dl.directorio_actual}')

    def arreglo(self):
        #print(f'DIREWCTORORIO ACTUAL: {dl.directorio_actual}')
        print(f'DATA: {dl.data}')
        
        
    def cambiarDirectorio(self):
        dirCambiar = QFileDialog.getExistingDirectory(self)
        print(dirCambiar)

        if dirCambiar !='':
            os.chdir(dirCambiar)
            dir = os.getcwd()

            self.rutaGuardar.clear()
            self.rutaGuardar.addItem(dir)
            self.rutaGuardar.setCurrentIndex(0)
            self.guardarDirectorio()
    
    def guardarDirectorio(self):
        ruta = self.rutaGuardar.currentText()
        print('Esta es la ruta que desea gurdar: ', ruta)
        dl.directorio_actual = ruta
        print(f'DERECTORIO CAMBIADO A: {dl.directorio_actual}')
    
    def salir(self):
        #self.close()
        salir = QMessageBox.question(self, 'Salir', '¿Esta seguro que desea salir?', QMessageBox.Yes, QMessageBox.No)
        if salir == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())