import requests
import flet as ft  
import csv
import pandas as pd
import json
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('flet-cuc-firebase-adminsdk-9qcmi-adc95321e0.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': "https://flet-cuc-default-rtdb.europe-west1.firebasedatabase.app"
})

# Obtener la referencia de la base de datos
ref = db.reference('/')

# Agregar los datos a Firebase
#ref.push().set(data_firebase)

# Obtener los datos de la referencia
data_firebase = ref.get()

# Mostrar los datos
print(data_firebase)


# Codigo para crear una tabla con los datos de un archivo JSON de GitHub
def main(page: ft.Page):
    page.scroll = True

    #url_json = "https://raw.githubusercontent.com/matute2500/flet/master/juv_A.json"
    url_json ="https://api.npoint.io/7d8fe0ae2ca3255710a3"
    response_json = requests.get(url_json)
    if response_json.status_code == 200:
        data = response_json.json()
        print("Acceso correcto al archivo JSON en GitHub")
        print(data)

        tabla=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("CODIGO")),
                ft.DataColumn(ft.Text("NOMBRE")),
                ft.DataColumn(ft.Text("APELLIDOS")),
                ft.DataColumn(ft.Text("F_NAC")),
                ft.DataColumn(ft.Text("F_REC")),
                ft.DataColumn(ft.Text("CONVOCATORIA")),
                ft.DataColumn(ft.Text("DORSAL")),
                ft.DataColumn(ft.Text("MINUTOS")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(valor["CODIGO"])),
                        ft.DataCell(ft.Text(valor["NOMBRE"])),
                        ft.DataCell(ft.Text(valor["APELLIDOS"])),
                        ft.DataCell(ft.Text(value=valor["F_NAC"],width=80, height=30)),
                        ft.DataCell(ft.Text(value=valor["F_REC"],width=80, height=30)),
                        ft.DataCell(ft.TextField(value=valor["CONVOCATORIA"],width=80, height=30)),
                        ft.DataCell(ft.TextField(value=valor["DORSAL"],width=80, height=30)),
                        ft.DataCell(ft.TextField(value=valor["MINUTOS"],width=80, height=30)),
                    ]
                )for valor in data
            ]
        )
        page.add(tabla)
    else:
        print("Error al acceder al archivo JSON en GitHub")
    
   
    def grabar_datos(event):
        lista_datos_nuevos = []
        for row in tabla.rows:
            for cell in row.cells:
                if isinstance(cell.content, ft.Text):
                    lista_datos_nuevos.append(cell.content.value)
                elif isinstance(cell.content, ft.TextField):
                    lista_datos_nuevos.append(cell.content.value)
        print(lista_datos_nuevos)
        
        # Grabar los datos de lista_datos_nuevos a un archivo JSON
        with open('nuevo.json', 'w') as file:
            json.dump(lista_datos_nuevos, file)

        # Upload the file to the specified URL
        url_upload = "https://api.npoint.io/7d8fe0ae2ca3255710a3"
        files = {'file': open('nuevo.json', 'rb')}
        response_upload = requests.post(url_upload, files=files)

        if response_upload.status_code == 200:
            print("Archivo subido correctamente")
        else:
            print("Error al subir el archivo")  
    
        
        
        

    boton_GRABAR_DATOS=ft.TextButton(text="GRABAR",on_click=grabar_datos) 
    
    
    page.add(boton_GRABAR_DATOS)

ft.app(target=main)
