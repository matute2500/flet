import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred_obj = firebase_admin.credentials.Certificate('flet-cuc-firebase-adminsdk-9qcmi-adc95321e0.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': "https://flet-cuc-default-rtdb.europe-west1.firebasedatabase.app"
})

# Verificar si la conexión se ha realizado con éxito
if default_app:
    print("Conexión exitosa")
    # Obtener todas las referencias de la base de datos
 
else:
    print("Error al conectar")
'''
    all_refs = db.reference().get()

    # Imprimir el nombre de cada colección
    for nombre_coleccion in all_refs.keys():
        print(nombre_coleccion)

    # Obtener una referencia de la base de datos
        ref_name = db.reference(nombre_coleccion)  
        print(ref_name)   
'''

#data_firebase = ref_name.get()
#print(data_firebase)
#db.reference(ref_name).delete()
def crear_coleccion():
    new_ref = db.reference()
    new_ref.push([{"marca":"Samsung","modelo":"Galaxy","pulgadas":"6","sistema":"Android","tipo":"Smartphone"},
                  {"marca":"Apple","modelo":"iPhone","pulgadas":"5.8","sistema":"iOS","tipo":"Smartphone"}])
def listar_colecciones():
    all_refs = db.reference().get()
    for nombre_coleccion in all_refs.keys():
        print(nombre_coleccion)

#crear_coleccion()
listar_colecciones()
'''
# Vaciar todas las referencias de la base de datos
ref = db.reference()    
ref.delete()

Crear una nueva referencia y agregar datos
new_ref = db.reference()
new_ref.push([{"marca":"Samsung","modelo":"Galaxy","pulgadas":"6","sistema":"Android","tipo":"Smartphone"},
                  {"marca":"Apple","modelo":"iPhone","pulgadas":"5.8","sistema":"iOS","tipo":"Smartphone"}])
'''
