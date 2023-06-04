import json

###CONSTRUCTOR DE LA CLASE###
class Producto:
    def __init__(self, categoria, marca, modelo, precio):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

###ACTUALIZACION DE PRECIO### Queda abierta por si acaso, por consigna, pero no tiene uso desde main
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print(f"El precio de {self.modelo} ha sido actualizado a {nuevo_precio}.")

###CALCULO DE DESCUENTO### Queda abierta por si acaso, por consigna, pero no tiene uso desde main
    def calcular_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        return self.precio - descuento

###FUNCION __STR__ POR CONSIGNA###
    def __str__(self):
        return self.modelo
    #Me pasa igual que en Cliente. Podria usarlo para otras funciones, pero tengo aun varias dudas al respecto

###FUNCION PARA DAR FORMATO JSON DESDE LOS PARAMETROS > ACCESORIA DE CARGAR###
    def nuevo_articulo(self):
        nuevo_producto = {
            "categoria": self.categoria,
            "marca": self.marca,
            "modelo": self.modelo,
            "precio": self.precio
        } #lee los parametros y los pasa al formato diccionario

        with open("./Productos/Recursos/base_productos.json", "r") as file:
            try:
                productos = json.load(file)
            except json.decoder.JSONDecodeError:
                productos = [] #si no existe, lo crea como lista vacía, para hacer lista de dicts

        productos.append(nuevo_producto) #suma el nuevo producto

        with open("./Productos/Recursos/base_productos.json", "w") as file:
            json.dump(productos,file) #escribe

##FUNCION PARA CARGAR (SUBIR UN NUEVO PRODUCTO)##
    def cargar(): #funciona como registro, pide por input los valores
        categoria = input("Ingrese la categoria del articulo: ")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        precio = int(input("Ingrese el precio al que desea publicarlo: "))
        #no tiene validaciones por el momento

        producto = Producto(categoria, marca, modelo, precio) #convierte los inputs en objeto
        producto.nuevo_articulo() #llama a la funcion para formatear
        print("Articulo cargado exitosamente.")

##FUNCION PARA MOSTRAR CATALOGO##
#sin esta funcion, el "cliente" estaria comprando "ciego" o deberia meterse en el archivo
    def mostrar_catalogo():
        with open("./Productos/Recursos/base_productos.json", "r") as file:
            productos = json.load(file) #abre el json en modo lectura

        catalogo = [] #crea una variable como lista vacía
        for producto in productos:
            producto_temp = Producto(**producto) #itera usando kwargs, porque son dicts en el archivo
            catalogo.append(producto_temp.__dict__) #retiene el formato

        return catalogo #devuelve la variable, para imprimir iterando por cada producto en el main

##FUNCION PARA COMPRAR##
    def compra():
        search = input('Ingrese el modelo que quiera comprar:') #pide el modelo por input
        with open("./Productos/Recursos/base_productos.json", "r") as file:
            productos = json.load(file) #abre en modo lectura

        for producto in productos: #itera para buscar el modelo
            if producto['modelo'] == search:
                return 'Compra exitosa!'
            return 'El producto no existe en la base'
        #podria agregarse en algun punto stock, modificando la clase
        #para mas adelante podria ser util (o mas realista?)
        #mismo caso con un carrito, esto solo permite compras de un producto especifico