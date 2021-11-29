from pytube import YouTube
import os
import threading
from PyQt5.QtWidgets import QFileDialog

url = 'https://www.youtube.com/watch?v=T8Z1VT1RE6E'
SAVE_PATH = r'./Video/'
directorio_actual = ''

def dirActual():
    global directorio_actual
    directorio_actual = os.getcwd()

def nuevoDirectorio():
    global directorio_actual
    directorio = QFileDialog.getExistingDirectory()

    if directorio != '':
        os.chdir(directorio)
        directorio_actual=os.getcwd()

def descargando():
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(SAVE_PATH)
    print(f'DESCARGA COMPLETADA!!')

def descargar():
    print('hilos!!!!')
    t1 = threading.Thread(target=descargando).start()

if __name__ == '__main__':
    #print(f'DIRECTORIO: {os.getcwd()}')
    #print(f'Inicio de descarga')
    #descargar()
    #print('Fin de la descarga!!!')
    print(dirActual())
    print(nuevoDirectorio())