from firebase_admin import credentials, firestore, initialize_app

# Usa un archivo de credenciales de servicio para inicializar Firebase
cred = credentials.Certificate('flet-cuc-firebase-adminsdk-9qcmi-adc95321e0.json')
initialize_app(cred)

db = firestore.client()

# Crea una colección
data = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 30
}

# Agrega los datos a la colección
db.collection('jugadores_prueba').add(data)