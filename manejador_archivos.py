import sys
import time 
import random
import os
import logging
import watchdog.observers 
import Observer
from watchdog.events import FileSystemEventHandle

from_dir="C:/Users/denis/Descargas"

class FileEventHnadler(FileSystemEventHandle):
    def on_created(self,event):
        print(f"Oye,{event.src_path}ha sido creado")

    def on_delete(self,event):
        print(f"Lo siento alguen borro{event.src_path}")

    def on_delete(self,event):   
    print(f"Hola{event.src_path}ha sido modificado")

event_handler=FileEventHandler(
    observer=Observer()
)