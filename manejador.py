import sys
import random

import os
import time
import shutil
from watchdog.observers.import Observer
from watchdog.events import FileSystemEvenHandler

from_dir="C:/Users/denis/Downloads"
to_dir="C:/Users/denis/Desktop"

dir_tree={ "Images_Files":['.jpg','.jpeg','.png','.gif','.jfif'], "Video_Files":['.mpg','.mp2','.mpeg','.mpe','.mpv','.mp4','.m4p'], "Documents_File":['.ppt','.xls','.xlsx','.cvs','.docx','.pdf','.txt'] }

class FileMovementHandler (FileSystemEvenHandler):

    def on_create(self,event):
    name,extension=os.path.splitext(event.src_path)
    time.sleep(1)

    for key,value in dir_tree.items():
        time.sleep(1)

        if extension in value:
            file_name=os.path(event.src_path)
            print("Descargando"+file_name)ç

            path1=from_dir+'/'+ file_name
            path2 =to_dir+'/'+key
            path3 = to_dir+'/'+key+'/'+file_name

        if os.path.exist(path2):
            print("El directorio existe....")
            print("moviendo"+file_name+"....")
            shutil.move(path1,path3)
            time.sleep(1)

        else: 
            print("Creando directorio...")
            os.makedirs(path2)
            print("Moviendo"+file_name+"...")
            shutil.move(path1,path3)
            time.sleep(1)



event_handler=FileSystemEventHandler()


observer=Observer()

observer.schedule(event_handle,from_dir,recursive=True)

observer.start()