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

url_json ="https://api.npoint.io/7d8fe0ae2ca3255710a3"
response_json = requests.get(url_json)
if response_json.status_code == 200:
    data = response_json.json()
    print("Acceso correcto al archivo JSON en GitHub")
    #print(data)

# Obtener la referencia de la base de datos
ref = db.reference('/')

# Agregar los datos a Firebase
ref.push().set(data)

# Obtener los datos de la referencia
data_firebase = ref.get()

# Mostrar los datos
print(data_firebase)

