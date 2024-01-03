from github import Github

# Primero debes crear un objeto Github usando tu token de acceso personal
g = Github("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")

# Obtén el repositorio donde quieres subir el archivo
repo = g.get_user().get_repo("flet")

# Abre el archivo que quieres subir
with open("juv_b1.csv", "rb") as file:
    content = file.read()
    print(content)

# Sube el archivo
repo.create_file("xxx.csv", "actualizado", content)
print("Archivo subido exitosamente")