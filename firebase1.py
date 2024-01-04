import requests
import flet as ft  
import csv
import pandas as pd
import json
import firebase_admin
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('flet-cuc-firebase-adminsdk-9qcmi-3ea5228ac1.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': "https://flet-cuc-default-rtdb.europe-west1.firebasedatabase.app"
})

url_json ="https://api.npoint.io/7d8fe0ae2ca3255710a3"
response_json = requests.get(url_json)
if response_json.status_code == 200:
    data = response_json.json()
    print("Acceso correcto al archivo JSON en GitHub")
    #print(data)

# Obtener la referencia de la base de datos
ref = db.reference('/')

# Agregar los datos a Firebase
#ref.push().set(data)

# Obtener los datos de la referencia
data_firebase = ref.get()

def main(page: ft.Page):
    page.scroll = True

    # Obtén la lista de diccionarios
    lista_datos = next(iter(data_firebase.values()))
    print(lista_datos)

    # Crear las filas de la tabla
    

    # Crear la tabla
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('CODIGO')),
            ft.DataColumn(ft.Text('NOMBRE')),
            ft.DataColumn(ft.Text('APELLIDOS')),
            ft.DataColumn(ft.Text('F_NAC')),
            ft.DataColumn(ft.Text('F_REC')),
            ft.DataColumn(ft.Text('CONVOCATORIA')),
            ft.DataColumn(ft.Text('DORSAL')),
            ft.DataColumn(ft.Text('MINUTOS'))
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
                )for valor in lista_datos
            ]
    )
    def on_click(event):
       ref.update(data_firebase)
       ref.push().set(data_firebase)

    boton_convertir=ft.TextButton(text="convertir",on_click=on_click) 
    
    page.add(tabla,boton_convertir)
ft.app(target=main)

# Actualizar los datos en Firebase
#ref.update(data_firebase)

# Mostrar los datos
print(data_firebase)