import requests
import flet as ft  
import csv
import pandas as pd

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
    
    boton_convertir=ft.TextButton(text="convertir",on_click=lambda:print("click en el boton convertir")) 
    page.add(boton_convertir)

ft.app(target=main)

