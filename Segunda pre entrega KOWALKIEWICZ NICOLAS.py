from mi_primer_paquete.MisFunciones import *

# se crea la clase persona con los atributos nombre apellido dni
class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

# se crea la clase cliente que hereda los atributos de persona, sumandole un telefono, un mail que se crea a partir de su nombre y apellido
# la clase guarda los strings necesarios para generar un ticket de compra
class Cliente(Persona): 
    def __init__(self, nombre, apellido, dni, telefono):
        super().__init__(nombre, apellido, dni)
        self.telefono = telefono
        self.mail = crear_mail(self.nombre, self.apellido)
        self.codigo = str(self.dni)
        self.listadecompras = []
        self.cantidades = []
        self.valores = []
        self.total = 0

# imprime datos del cliente
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Telefono: {self.telefono}, Codigo: {self.codigo}, Mail: {self.mail}"    
    
# agregar a 3 vectores paralelos la compra que se hizo, la cantidad y el total de la compra individual y parcial
    def agregar_al_carrito(self, producto, cantidad, totalparcial):
        self.listadecompras.append(producto)
        self.cantidades.append(cantidad)
        self.valores.append(totalparcial)
        
# genera un ticket mostrando el detalle de la compra y el total
    def ticket(self):
        print("\n", "- " * 25)
        print(f"Ticket para el cliente {self.nombre} nº{self.codigo}\n")
        print("PRODUCTO\tCANTIDAD\tPRECIO")
        for num in range(len(self.listadecompras)):
            producto = self.listadecompras[num].ljust(10)
            cantidad = str(self.cantidades[num]).ljust(10)
            precio = "$" + str(self.valores[num])
            print(f"{producto}\t{cantidad}\t{precio}")
        print(f"\nTotal: ${self.total}.\nGracias por su compra!")
        
#realiza la compra de un listado de productos creados en el main, guardados en un diccionario, son productos y precios ficticios que sirven como ejemplo
#una vez hecha la compra lo agrega al carrito y da la opcion de seguir comprando          
    def comprar(self):
        print("SELECCIONAR PRODUCTOS:")
        eleccion = 0
        while eleccion != 5:
            valor = 0
            totalparcial = 0
            print("*.-"*25, "\n")
            eleccion = limites(1, 5,("1. Mate\n2. Cafe\n3. Harina\n4. Palmitos\n5. Finalizar"))
            if eleccion == 1:
                valor = productos.get("mate")
                producto = "mate"
            if eleccion == 2:
                valor =productos.get("cafe")
                producto = "cafe"
            if eleccion == 3:
                valor =productos.get("harina")
                producto = "harina"
            if eleccion == 4:
                valor =productos.get("palmito")
                producto = "palmito"
            if eleccion != 5:
                cantidad = limites(0, 100000, "Ingrese cantidad: ")
                self.total += valor*cantidad
                totalparcial += valor * cantidad
                self.agregar_al_carrito(producto, cantidad, totalparcial)
        self.ticket()
    

    
# # # # #   M A I N   # # # # # # 

#da la opcion de crear un cliente ingresando los datos por teclado
def crear_cliente():
    print("*-* " * 25)
    nombre = input("Ingrese nombre: ").capitalize()
    apellido = input("Ingrese apellido: ").capitalize()
    dni = limites(10000000, 99999999, "Ingrese DNI: ")
    telefono = limites(1000000000, 9999999999, "Ingrese telefono: ")
    cliente = Cliente(nombre, apellido, dni, telefono)
    return cliente

#listado de productos guardado en un diccionario
productos = {
    "mate": 272.74,
    "cafe": 1355,
    "harina": 139.49,
    "palmito": 363
}

#ejemplo de cliente 
cliente1 = Cliente("Juan", "Perez", "99999999", "1100000000")
cliente1.comprar()

# asd