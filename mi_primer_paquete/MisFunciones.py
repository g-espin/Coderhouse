def crear_mail(nombre, apellido):
        primera_letra = nombre[0]
        primera_letra = primera_letra.capitalize()
        apellido2 = apellido
        extension = "@mitienda.com"
        mail = primera_letra + apellido2 + extension
    
        return mail

def validar_numeros(frase):
    # frase = frase.capitalize()
    while True:
        try:
            valor = int(input(f"{frase}: ") )
            break
        except ValueError:
            print("No se ha detectado un numero, vuelva a ingresar")
    return valor

def limites(inferior, superior, frase = "numero"):
    numero = validar_numeros(frase)
    while numero < inferior or numero > superior:
        print(f"El numero tiene que ser mayor que {inferior} y menor que {superior}")
        numero = validar_numeros(frase)
    return numero
