from concurrent.futures import ThreadPoolExecutor
from pytube import YouTube
import os
import threading
from PyQt5.QtWidgets import QFileDialog
from multiprocessing import Pool
import re


urls = ['https://www.youtube.com/watch?v=T8Z1VT1RE6E','https://www.youtube.com/watch?v=CjmzDHMHxwU','https://www.youtube.com/watch?v=lc5JJTQa4r8']

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

def descargando(urls):
    video = YouTube(urls)
    #print(f'ByPass: {video.bypass_age_gate}')
    stream = video.streams.get_highest_resolution()
    stream.download(SAVE_PATH)
    print(f'DESCARGA COMPLETADA!!')

def multiprocesamiento():
    print('MultiProcesamiento')
    pool = Pool(len(urls))
    pool.map(descargando, urls)

def subProcesosMultiples():
    print('SubProcesos Multiples!!!!')
    #t1 = threading.Thread(target=descargando).start()
    with ThreadPoolExecutor(max_workers=(len(urls))) as excuter:
        excuter.map(descargando, urls)
    #print('SIUUUUUUU')
    

if __name__ == '__main__':
    #print(f'DIRECTORIO: {os.getcwd()}')
    #print(f'Inicio de descarga')
    subProcesosMultiples()
    ###multiprocesamiento()
    
    print('Fin de la descarga!!!')
    