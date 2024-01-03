import requests
import flet as ft  
import csv
import pandas as pd


url = "https://raw.githubusercontent.com/matute2500/flet/master/juv_b1.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("juv_b1.csv", "wb") as file:
        file.write(response.content)
    print("Archivo descargado exitosamente")
else:
    print("Error al descargar el archivo")


#------------------------------------------------------
# Codigo para descargar un archivo CSV de GitHub y convertirlo a JSON y trabajar con el
url = "https://raw.githubusercontent.com/matute2500/flet/master/juv_b1.csv"
response = requests.get(url)
if response.status_code == 200:
    with open("juv_b1.csv", "wb") as file:
        file.write(response.content)
    print("Archivo descargado exitosamente")
else:
    print("Error al descargar el archivo")

csv_data = pd.read_csv("juv_b1.csv", sep=",")
csv_data.to_json("test.json", orient="records")
#------------------------------------------------------
# Codigo para accedera a un archivo CSV de GitHub
url_csv = "https://raw.githubusercontent.com/matute2500/flet/master/juv_b1.csv"
response_csv = requests.get(url_csv)
if response_csv.status_code == 200:
    content = response_csv.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    print("Correcto Acceso al archivo CSV en GitHub")
    for row in reader:
        print(row)
else:
    print("Error al acceder al archivo CSV en GitHub")
#------------------------------------------------------
# Codigo para crear una tabla con los datos de un archivo JSON de GitHub
def main(page: ft.Page):
    url_json = "https://raw.githubusercontent.com/matute2500/flet/master/test.json"
    response_json = requests.get(url_json)
    if response_json.status_code == 200:
        data = response_json.json()
        print("Acceso correcto al archivo JSON en GitHub")
        print(data)

        tabla=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("CODIGO")),
                ft.DataColumn(ft.Text("DORSAL")),
                ft.DataColumn(ft.Text("NOMBRE")),
                ft.DataColumn(ft.Text("APELLIDOS")),
                ft.DataColumn(ft.Text("CONVOCATORIA")),
                ft.DataColumn(ft.Text("MINUTOS")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(valor["codigo"])),
                        ft.DataCell(ft.TextField(value=valor["dorsal"],width=80, height=30)),
                        ft.DataCell(ft.Text(valor["nombre"])),
                        ft.DataCell(ft.Text(valor["apellidos"])),
                        ft.DataCell(ft.TextField(value=valor["convocatoria"],width=80, height=30)),
                        ft.DataCell(ft.TextField(value=valor["minutos"],width=80, height=30)),
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
