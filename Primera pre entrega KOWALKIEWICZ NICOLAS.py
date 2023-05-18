import getpass as gp
import json
import os

def mostrar_usuarios(**kwargs):
    if not kwargs:
        print("La base de datos esta vacia, por favor, carga usuarios para continuar")
        return 0   
    print("\n", " *"*25)
    print("USUARIOS".ljust(20) + "CONTRASEÑAS")
    for key, value in kwargs.items():
        print(key.ljust(20) + value)

def usuario_existente(usuario, Base_datos):
    return usuario in Base_datos

def crear_usuario():
    print("\n"," *"*25)
    print("Vamos a crear un usuario, el mismo debe tener minimo 7 caracteres.")
    usuario = input("Ingrese usuario: ")
    while True:
        if usuario_existente(usuario, Base_de_datos):
            print("Error, usuario existente.")
            usuario = input("Ingrese usuario: ")
        elif len(usuario) < 8:
            print("Error, usuario corto.")
            usuario = input("Ingrese usuario: ")
        else: 
            break
    return usuario

def crear_contraseña():
    print("\n"," *"*25)
    print("Vamos a crear una contraseña, la misma debe tener: \n- 1 Mayuscula.\n- 1 Numero.\n- Minimo 7 caracteres.")
    contraseña = gp.getpass("Ingrese contraseña: ")
    Mayusucula = 0
    Numero = 0
    for letra in contraseña:
        if letra.isupper():
            Mayusucula = 1
        if letra.isdigit() == True:
            Numero = 1
    while True:
        if Mayusucula == 0:
            print("Tiene que tener una mayuscula")
        elif Numero == 0:
            print("Tiene que tener un numero")
        elif len(contraseña) < 7:
            print("Contraseña muy corta")
        elif len(contraseña) >= 12:
            print("Contraseña muy larga")
        else:
            break
        contraseña = gp.getpass("Ingrese contraseña: ")
        Mayusucula = 0
        Numero = 0
        for letra in contraseña:
            if letra.isupper():
                Mayusucula = 1
            if letra.isdigit() == True:
                Numero = 1
    return contraseña

def agregar_usuario(Base_datos):
    usuario = crear_usuario()
    contraseña = crear_contraseña()
    Base_datos.update({usuario:contraseña})

def Validar_contraseña(usuario, Base_datos):
    valor = Base_datos.get(usuario)
    return valor

def login(Base_datos):
    usuario = input("Ingrese usuario: ")
    validar_usuario = usuario_existente(usuario, Base_datos)
    while True:
        if validar_usuario == True:
            contador = 2
            contraseña = gp.getpass("Ingrese contraseña: ")
            validar_contraseña = Validar_contraseña(usuario, Base_datos)
            while True:
                if validar_contraseña == contraseña:
                    Acceso(usuario, Base_datos)
                    break
                if contador == 0:
                    print("INTENTOS AGOTADOS")
                    break
                else:
                    contador -=1
                    print(f"Contraseña incorrecta, tiene {contador +1} intentos")
                    contraseña = gp.getpass("ingrese contraseña: ")
                    validar_contraseña = Validar_contraseña(usuario, Base_datos)   
            break
        else:
            print("Usuario no encontrado. Intente de nuevo.")
            usuario = input("Ingrese usuario: ")
            validar_usuario = usuario_existente(usuario, Base_datos)

def Acceso(usuario, Base_datos):
    print("\n"," *"*25)
    print("Seleccione opcion para operar:\n1. Cambiar contraseña\n2. Mostrar usuarios\n3. Salir")
    opcion = limites(1,3,"Ingrese para continuar: ")
    if opcion == 1:
        cambiar_contraseña(usuario, Base_datos)
        print("\n"," *"*25)
    elif opcion ==2:
        mostrar_usuarios(**Base_datos)
    elif opcion == 3:
        print("Hasta luego!")
        return 0

def validar_numeros(frase):
    while True:
        try:
            valor = float(input(f"{frase}") )
            break
        except ValueError:
            print("No se ha detectado un numero, vuelva a ingresar.")
    return valor

def limites(inferior, superior, frase = "numero"):
    numero = validar_numeros(frase)
    while numero < inferior or numero > superior:
        print(f"El numero tiene que ser mayor que {inferior} y menor que {superior}")
        numero = validar_numeros(frase)
    return numero

def cambiar_contraseña(user, Base_datos):
    nueva_contraseña = crear_contraseña()
    Base_datos.update({user:nueva_contraseña})
    print("\n"," *"*25)
    menu_inicial(Base_datos)
    
def menu_inicial(Base_datos):
    print("Bienvenido al sistema, ingrese la opcion deseada:")
    print("1. Loguearse.")
    print("2. Crear un usuario.")
    print("3. Salir.")
    opcion = limites(1, 3,"\nIngrese para continuar: ")
    if opcion == 1:
        print("\n"," *"*25)
        login(Base_datos)
    elif opcion == 2:
        agregar_usuario(Base_datos)
        print("\n"," *"*25)
        login(Base_datos)
    elif opcion == 3:
        print("Hasta luego!")
        
# # # BLOQUE PRINCIPAL # # #

with open('Base_de_datos.json', 'a+') as archivo:
    archivo.seek(0, os.SEEK_END)
    isempty = archivo.tell() == 0
    archivo.seek(0)
    if isempty == 0:
        Base_de_datos = json.load(archivo)
    else:
        Base_de_datos = {}

menu_inicial(Base_de_datos)

with open('Base_de_datos.json', 'w+') as archivo:
    json.dump(Base_de_datos, archivo, indent=4)