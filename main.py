import os
import TableauDesktopPy as tdp
import pandas as pd
folders = []
for dirPath, dirNames, fileNames in os.walk(os.getcwd()):
    folders.append(dirPath)
i = 0
files = {}
for carpeta in folders:
    contenido = os.listdir(carpeta)
    for archivo in contenido:
        i += 1
        nombre, extension = os.path.splitext(archivo)
        if extension == '.twbx':
            try:
                ruta = carpeta+carpeta[2] + archivo
                files[i] = {'ruta':ruta,'archivo':archivo,'datos':0}
            except:
                print('ERROR obtener data line 18')

'''ruta=os.getcwd()
book = tdp.Workbook(ruta+ruta[2]+'archivo.twbx')
#df = pd.DataFrame(data = book.fields)

print(type(book))
'''
