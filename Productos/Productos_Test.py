import json

class Producto:
    def __init__(self, categoria, marca, modelo, precio):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

def busqueda(search):
    with open("./Recursos/base_productos.json", "r") as file:
        productos = json.load(file)
    for producto in productos:
        if producto['modelo'] == search:
            return producto
    
    return 'El producto no existe en la base'

search = 'test3'
resultado = busqueda(search)
if resultado != 'El producto no existe en la base':
    producto = Producto(**resultado)
    resultado = producto.__dict__

print(resultado)

def mostrar_catalogo():
    with open("./Recursos/base_productos.json", "r") as file:
        productos = json.load(file)

    catalogo = []
    for producto in productos:
        producto_obj = Producto(**producto)
        catalogo.append(producto_obj.__dict__)

    return catalogo

catalogo = mostrar_catalogo()
for producto in catalogo:
    print(producto)