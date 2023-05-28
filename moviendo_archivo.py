import os 
import shutil

from_dir="C:/Users/denis/Descargas"

to_dir="C\Users\denis/Descargas/Prueba"

list_of_files=os.listdir(from_dir)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['txt','pdf','docx']:
        path1=from_dir + '/' + file_name
        path2=from_dir + '/' + "Documents_Files"
        path3=from_dir + '/' + "Documents_Files"+ file_name
