from PyQt5.QtWidgets import QMessageBox
from concurrent.futures import ThreadPoolExecutor
from pytube import YouTube

#urls = ['https://www.youtube.com/watch?v=T8Z1VT1RE6E','https://www.youtube.com/watch?v=CjmzDHMHxwU','https://www.youtube.com/watch?v=lc5JJTQa4r8', 'https://www.youtube.com/watch?v=aD_kQBi6gOY', 'https://www.youtube.com/watch?v=0DNCCl3sCjY', 'https://www.youtube.com/watch?v=bm-PDiLiHCI','https://www.youtube.com/watch?v=mcWXvFC45hc','https://www.youtube.com/watch?v=oKAnOzIu66c']

urls = []
data = []

directorio_actual = ''

def descargando(urls):
    if not urls:
        print('VACIO ARREGLO')
        
    else:
        video = YouTube(urls)
        print(f'--------------------------------------')
        print(f'Title: {video.title}')
        print(f'Author: {video.author}')
        print(f'URL C: {video.channel_url}')
        print(f'Lenght: {(video.length)/60} Min')
        print(f'URL V: {urls}')
        print(f'--------------------------------------')
        
        title = video.title
        author = video.author
        urlChannel = video.channel_url
        time = video.length
        length = str(round((time/60),2)) + ' Min'
        url = urls
        
        data.append((title,author,urlChannel,length,url))

        stream = video.streams.get_highest_resolution()
        stream.download(directorio_actual)
        print(f'DESCARGA COMPLETADA!! --> {video.title} URL--> {urls}')
        

def subProcesosMultiples():
    
    if not urls:
        QMessageBox.critical(None, 'La lista esta Vacia','Lista de videos a descargar esta vacía!!\nIngrese la url del video que desea descargar!!!')
    else:
        
        with ThreadPoolExecutor(max_workers=(len(urls))) as excuter:
            excuter.map(descargando, urls)

        QMessageBox.information(None, 'Descarga!!!','La descarga esta completada!!')

        urls.clear()