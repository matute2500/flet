import requests
import flet as ft  
import csv
import pandas as pd

#------------------------------------------------------
# Codigo para descargar un archivo CSV de GitHub y convertirlo a JSON
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

def main(page: ft.Page):
    
    #------------------------------------------------------
    url_json = "https://raw.githubusercontent.com/matute2500/flet/master/test.json"
    response_json = requests.get(url_json)
    if response_json.status_code == 200:
        data = response_json.json()
        print("Correcto Acceso al archivo JSON en GitHub")
        print(data)
        for value in data:
            fila=ft.Row(controls=
            [
            ft.Text(value="Codigo: "+str(value["codigo"])),    
            ft.Text(value=value["nombre"]),
            ft.Text(value=value["apellidos"]),
            ft.TextField(value=value["convocatoria"]),
            ft.TextField(value=value["minutos"]),
            ])
            page.add(fila)  
    else:
        print("Error al acceder al archivo JSON en GitHub")
#------------------------------------------------------
    fila1=ft.Column(controls=
        [
        ft.TextButton("Boton 1"),
        ft.TextButton("Boton 2")
        ]
    )
    #texto=ft.Text("Hola Mundo")
    page.add(fila1)

ft.app(target=main)