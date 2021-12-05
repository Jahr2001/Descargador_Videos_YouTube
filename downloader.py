from PyQt5.QtWidgets import QMessageBox
from concurrent.futures import ThreadPoolExecutor
from pytube import YouTube
#urls = ['https://www.youtube.com/watch?v=T8Z1VT1RE6E','https://www.youtube.com/watch?v=CjmzDHMHxwU','https://www.youtube.com/watch?v=lc5JJTQa4r8', 'https://www.youtube.com/watch?v=aD_kQBi6gOY', 'https://www.youtube.com/watch?v=0DNCCl3sCjY', 'https://www.youtube.com/watch?v=bm-PDiLiHCI','https://www.youtube.com/watch?v=mcWXvFC45hc','https://www.youtube.com/watch?v=oKAnOzIu66c']
urls = []
data = []
#urls = ['https://www.youtube.com/watch?v=T8Z1VT1RE6E']
#directorio_actual = "D:\\Documentos\\7mo Cuatrimestre\\Programación Concurrente\\Tercer Corte\\DescargadorVideosYouTube\\Video"

directorio_actual = ''

def descargando(urls):
    if not urls:
        print('VACIO ARREGLO')
        #QMessageBox.warning(None, 'Lista Vacia','Lista de videos vacia')
    else:
        video = YouTube(urls)
        print(f'--------------------------------------')
        print(f'Title: {video.title}')
        print(f'Author: {video.author}')
        print(f'URL C: {video.channel_url}')
        print(f'Lenght: {(video.length)/60} Min')
        print(f'URL V: {urls}')
        print(f'--------------------------------------')
        data.append((video.title, video.author, video.channel_url, video.length, urls))
        stream = video.streams.get_highest_resolution()
        stream.download(directorio_actual)
        print(f'DESCARGA COMPLETADA!! --> {video.title} URL--> {urls}')

def subProcesosMultiples():
    print('SubProcesos Multiples!!!!')
    if not urls:
        print('NO HAY URL')
        QMessageBox.warning(None, 'Lista Vacia','Lista de videos vacia')
    else:
        print('Entra a la descarga ddel video')
        with ThreadPoolExecutor(max_workers=(len(urls))) as excuter:
            excuter.map(descargando, urls)

        urls.clear()