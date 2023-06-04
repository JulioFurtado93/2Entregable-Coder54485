import json

###CONSTRUCTOR DE LA CLASE###
class Cliente:
    def __init__(self, nombre, telefono, direccion, email, username, password):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email      #por el momento no se hace uso del email, pero podria ser mas adelante
        self.username = username
        self.password = password
    
    #Solo para pruebas > abro modulo de productos para luego generar productos y compras desde ahi
    # def comprar(self, producto):
        # print(f"{self.nombre} ha realizado la compra del producto {producto}.")

    #Obsoleto > ahora funciona con el json, tomando de parametro el username luego del login
    # def actualizar_telefono(self, nuevo_telefono):
        # self.telefono = nuevo_telefono
        # print(f"El telefono de {self.nombre} ha sido actualizado a {nuevo_telefono}.")

###FUNCION DE CAMBIO DE TELEFONO###
    def actualizar_telefono(username): #toma el username como parametro, modifica el telefono del username activo
        nuevo_telefono = input("Ingrese el nuevo telefono: ") #pide input
        with open("./Clientes/Recursos/base_clientes.json", "r") as file:
            clientes = json.load(file) #abre el json en modo lectura

        for cliente in clientes: #bucle for para iterar en usuarios registrados
            if cliente["username"] == username: #busca el usuario
                cliente["telefono"] = nuevo_telefono #modifica el valor de clave 'telefono' con el input pedido antes
                break
        
        with open("./Clientes/Recursos/base_clientes.json", "w") as file:
            json.dump(clientes, file) #escribe el nuevo telefono
            print("Telefono actualizado.")
    
    #Obsoleto > ahora funciona con el json, tomando de parametro el username luego del login
    # def actualizar_direccion(self, nueva_direccion):
        # self.direccion = nueva_direccion
        # print(f"La dirección de {self.nombre} ha sido actualizada a {nueva_direccion}.")

###FUNCION DE CAMBIO DE DIRECCION###
    def actualizar_direccion(username): #funciona exactamente igual que la anterior
        nueva_direccion = input("Ingrese la nueva dirección: ")
        with open("./Clientes/Recursos/base_clientes.json", "r") as file:
            clientes = json.load(file)

        for cliente in clientes:
            if cliente["username"] == username:
                cliente["direccion"] = nueva_direccion
                break
        
        with open("./Clientes/Recursos/base_clientes.json", "w") as file:
            json.dump(clientes, file)
            print("Direccion actualizada.")

###FUNCION __STR__ POR CONSIGNA###
    def __str__(self): #ver como usarlo desde el main para el saludo de usuario
        return self.nombre
    #puedo hacer que el login retorne el cliente completo en lugar de solo el username
    #deberia en ese caso, adaptar las funciones de "actualizar_nnn"
        #iterarian como? con un enumerate alcanza?
        #y aun asi: serviria para cumplir con esta parte de la consigna?
        
###FUNCION PARA EVITAR DUPLICADOS > ACCESORIA DE REGISTRO###
    def verificar_username(username):
        with open("./Clientes/Recursos/base_clientes.json", "r") as file:
            try:
                clientes = json.load(file)
            except json.decoder.JSONDecodeError:
                return False

            for cliente in clientes:
                if cliente["username"] == username:
                    return True #retorna true en caso de encontrar coincidencia
        return False #false para que haciendo un break continue el registro

###FUNCION PARA DAR FORMATO JSON DESDE LOS PARAMETROS > ACCESORIA2 DE REGISTRO###
    def nuevo_usuario(self):
        nuevo_cliente = {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email,
            "username": self.username,
            "password": self.password
        } #lee los parametros y los pasa al formato diccionario

        with open("./Clientes/Recursos/base_clientes.json", "r") as file: #lee los preexistentes
            try:
                clientes = json.load(file)
            except json.decoder.JSONDecodeError:
                clientes = [] #si no existe, lo crea como lista vacía, para hacer lista de dicts

        clientes.append(nuevo_cliente) #suma el nuevo usuario

        with open("./Clientes/Recursos/base_clientes.json", "w") as file:
            json.dump(clientes, file) #escribe

###FUNCION DE REGISTRO###
    def registro(): #registro pide los inputs
        nombre = input("Ingrese su nombre: ")
        telefono = input("Ingrese su numero de telefono: ")
        direccion = input("Ingrese su dirección: ")
        email = input("Ingrese su email: ")

        while True: #el username pide validacion
            username = input("Ingrese un nombre de usuario: ")
            if Cliente.verificar_username(username):
                print("El nombre de usuario ya existe. Por favor, elija otro.")
            else:
                break

        password = input("Ingrese una contraseña de al menos 4 caracteres: ") #valida igual que el 1 entregable
        if len(password) < 4:
            print('La contraseña debe contener al menos 4 caracteres')
            return

        cliente = Cliente(nombre, telefono, direccion, email, username, password) #envía los inputs como parametros de clase
        cliente.nuevo_usuario() #llamado a la funcion para agregar el usuario
        print("Registro exitoso.")

###FUNCION DE INGRESO###
    def login():
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        with open("./Clientes/Recursos/base_clientes.json", "r") as file:
            clientes = json.load(file)
            for cliente in clientes: 
                if cliente["username"] == username and cliente["password"] == password:
                    print("Inicio de sesión exitoso.")
                    return username #devuelve el username para utilizarlo con la sesion "iniciada" e ingresarlo de parametro para los cambios de telefono y direccion
                #else:  ###DOS HORAS ESTUVE PARA ENCONTRAR ESTE ERROR, DOS HORAS 
            print("Credenciales inválidas. Por favor, intente nuevamente.")
            return False #era moverlo fuera del bucle for, menos mal que probe con mas usuarios