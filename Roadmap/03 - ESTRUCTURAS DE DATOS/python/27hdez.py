# LISTAS
import os

def listas():
    list = [1, 2, "hello", True]
    print("Lista: ", list)

    #Pintamos el primer elemento de la lista
    print("Primer elemento de la lista: ", list[0])

    #Añadimos un elemento a la lista
    list.append(42)
    print("Elemento añadido ", list)

    # Eliminamos el elemento "hello" de la lista
    list.remove("hello")
    print("Eliminar elemento: ", list)

    # Ordenamos la lista
    list = [1,5,3,6,8,9,4]
    list.sort()
    print("Ordenamos a reversa la lista: ", list)

#listas()

# TUPLAS
def tuplas():
    #En las tuplas no se puede:
    """ 
    En las tuplas no se puede:
    - Insertar datos
    - Eliminar datos
    - Actualizar elementos
    - Ordenar la tupla 
    """

    tuple = (1, "mundo", 2.5)
    print("Tupla: ", tuple)

    # Accede al segundo elemento de la tupla
    print("Elemento de la lista: ", tuple[1])

    new_tupla = tuple + (4,5)
    print("Añadir elemento: ", new_tupla)

    repetida = tuple * 2
    print("Repetición de elementos: ", repetida)

    #Verificamos si la tupla contiene un elemento
    print ("Verificación de pertenencia: ", 2.5 in tuple)

#tuplas()

# CONJUNTOS
def conjuntos():
    """
    En los conjuntos no se puede ni actualizar datos ni
    ordenar los elementos
    """
    set = {1, 2, 3, 4, 5}
    print ("Conjunto: ", set)

    set.add(6)
    print("Elementos añadido: ", set)

    set.remove(3)
    print("Elementos eliminado: ", set)

#conjuntos()

# CONJUNTOS INMUTABLES
def conjuntosInmutables():
    """
    En el caso de los conjuntos inmutables, no se puede ni
    añadir, eliminar, actualizar u ordenar elementos
    """
    conjunto_inmutable = frozenset([1, 2, 3])
    print("Conjunto inmutable: ", conjunto_inmutable)

#conjuntosInmutables()

# DICCIONARIO
def diccionario():
    diccionario = {"name": "Gabriel", "age": 22}
    print("Accedemos al nombre: ", diccionario["name"])

    diccionario["ocupación"] = "Desarrollador"
    print("Agregamos un nuevo valor: ", diccionario)

    diccionario["age"] = 23
    print("Actualizamos un valor: ", diccionario)

    del diccionario["age"]
    print("Eliminamos un valor: ", diccionario)

#diccionario()

# RANGOS
def rangos():
    """
    Los rangos son inmutables, pero podemos convertirlos en
    listas o tuplas para poder modificar sus valores
    """
    for i in range (1, 10, 2):
        print(i) # Imprime los números impares del 1 al 9

#rangos()

# EXTRA #
agenda = [
    {"name": "User1", "number": 111111111}, 
    {"name": "User2", "number": 222222222}, 
    {"name": "User3", "number": 333333333}
]

def findContact():
    os.system('clear')
    contact = ""
    name = input("Introduce el nombre del contacto: ")

    for i in agenda:
        if i["name"] == name:
            contact = i
            
    os.system('clear')
    if contact != "":
        print("Usuario encontrado:")
        print("\n\tNombre: ", i["name"])
        print("\n\tTeléfono: ", i["number"])
    else:
        print("Usuario no encontrado")

    input("\nPulse una tecla para volver al menú...")
    showMenu()    

def insertContact():
    os.system('clear')
    valid = True
    name = input("Introduzca el nombre del nuevo contacto: ")
    
    for i in agenda:
        if i["name"] == name:
            valid = False

    if valid:
        if isinstance(name, str):
            number = input("\nAhora debe introducir el número de teléfono: ")
            try:
                entero = int(number)
                if len(number) <= 11:
                    agenda.append({"name": name, "number": entero})
                    os.system('clear')
                    print("Usuario agregado correctamente a la agenda")
                    input("\nPulse cualquier tecla para volver al menú...")
                    showMenu()
                else:
                    os.system('clear')
                    print("Número en formato incorrecto")
                    input("\nPulse cualquier tecla para volver a introducir los datos...")
                    insertContact()
            except ValueError:
                os.system('clear')
                print("Número en formato incorrecto")
                input("\nPulse cualquier tecla para volver a introducir los datos...")
                insertContact()
        else:
            input("\nNombre de usuario inválido, pulse cualquier tecla para volver a introducir...")
            insertContact()
    else:
        os.system('clear')
        print("Usuario existente en la agenda")
        input("\nPulse cualquier tecla para volver a introducir los datos...")
        insertContact()


    return "agenda actualizada correctamente..."

def deleteContact():
    os.system('clear')
    contact = ""
    name = input("Introduce el nombre del contacto a eliminar: ")

    for i in agenda:
        if i["name"] == name:
            contact = i
            
    os.system('clear')
    if contact != "":
        agenda.remove(contact)
        print("Usuario eliminado de la agenda correctamente:")
    else:
        print("Usuario no encontrado en la agenda")

    input("\nPulse una tecla para volver al menú...")
    showMenu() 

switch = {
    1: findContact,
    2: insertContact,
    3: deleteContact,
    4: exit
}

def getOption():
    opcion = int(input(f"\nIntroduce una opción: "))
    switch.get(opcion, showMenu)()

def showMenu():
    os.system('clear')
    print("Agenda de contactos")
    print("1- Buscar contacto")
    print("2- Nuevo contacto")
    print("3- Eliminar contacto")
    print("4- Finalizar programa")
    getOption()

showMenu()