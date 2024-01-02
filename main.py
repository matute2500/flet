import requests
import flet as ft  

url = "https://raw.githubusercontent.com/matute2500/flet/master/juv_b.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("correcto")
    print(data)
    # Aquí puedes trabajar con los datos del archivo JSON
else:
    print("Error al acceder al archivo JSON en GitHub")


def main(page: ft.Page):
    
    texto=ft.Text("Hola Mundo")
    page.add(texto)

ft.app(target=main)