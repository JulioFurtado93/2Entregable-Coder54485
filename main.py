import os #antes no funcionaban los cls en colabs, pero podria averiguar para tomar distintos OS para que le funcione a Patricia
from Clientes.Mod_Clientes import Cliente
from Productos.Mod_Productos import Producto

def menu_principal(sesion):
    while 1:
        print(f"\nHola {sesion}! Que le gustaria hacer?: \n") #por el momento saluda al username, no al nombre
        print('1- Modificar numero de telefono')
        print('2- Modificar direccion')
        print('3- Cargar un nuevo producto')
        print('4- Mostrar catalogo de productos')
        print('5- Comprar producto')
        print('6- Cerrar sesion\n')
        opcion = int(input('Ingrese una opcion: '))
        
        if opcion == 1:
            os.system('cls') 
            Cliente.actualizar_telefono(sesion) #llama al metodo desde cliente, envia username
        elif opcion == 2:
            os.system('cls')
            Cliente.actualizar_direccion(sesion) #llama al metodo desde cliente, envia username
        elif opcion == 3:
            os.system('cls')
            Producto.cargar() #llama al metodo desde producto
        elif opcion == 4:
            os.system('cls')
            catalogo = Producto.mostrar_catalogo() #llama al metodo desde producto usando una variable para iterar
            for producto in catalogo:
                print(producto) #imprime el listado completo con un bucle for
        elif opcion == 5:
            os.system('cls')
            print(Producto.compra()) #llama al metodo desde producto
        elif opcion == 6:
            os.system('cls')
            print("¡Hasta luego!")
            break
        else:
            os.system('cls')
            print("Opción inválida. Por favor, seleccione una opción válida.")

while 1: #bucle infinito para inicializar menu
    #DISEÑO DE MENU DE 1ER ENTREGA
    print('1- Iniciar sesión')
    print('2- Registro de nuevo usuario')
    print('3- Salir')
    
    interfaz = int(input('Ingrese una opcion: '))
    
    if interfaz == 1:
        os.system('cls')
        sesion = Cliente.login() #variable accesoria para entrar de parametro al menu interno, llama al metodo desde cliente
        if sesion: #ejecuta mientras el login no devuelva False
            menu_principal(sesion)
        # if Cliente.login() != 0:
            # #print(Cliente.login())
            # sesion_activa = Cliente.login()
            # menu_principal()
    elif interfaz == 2:
        os.system('cls')
        Cliente.registro() #llama al metodo desde cliente
    elif interfaz == 3: #con la opcion 3 como escape
        os.system('cls')
        print('Gracias por utilizar el sistema!')
        break
    else:
        os.system('cls')
        print('No se reconoce el comando')                                                    