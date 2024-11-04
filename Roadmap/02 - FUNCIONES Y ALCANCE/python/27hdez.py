txt = "Hello World"

# Función simple sin parámetros predeterminados
def firstFuntion():
    return txt

print(firstFuntion())

# Función
def secondFuntion(name="friend"):
    return f"1. Hello {name}"

print(secondFuntion())
print(secondFuntion("Gabriel"))

# Función recursiva
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print (factorial(5))

# Funciones anidadas
def funcion_externa(msg):
    def funcion_interna():
        return msg.upper()
    return funcion_interna()

print(funcion_externa("anidadas"))

def modificacionGlobal():
    global txt
    txt += " fin."

modificacionGlobal()
print(txt)

# EXTRA #
def extraFuntion(first, second):
    contador = 0

    for i in range(1,101):
        if i % 3 == 0:
            print(first)
            if i % 5 == 0:
                print(f"{first}{second}")
        elif 1 % 5 == 0:
            print (second)
        else:
            contador += 1

    return contador

result = extraFuntion("first", "second")
print("Números impresos: ", result)