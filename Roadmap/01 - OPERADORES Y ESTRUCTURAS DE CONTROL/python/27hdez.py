a = 10
b = 2

#Operadores Aritmétcios
print (a + b) #Suma
print (a - b) #Resta
print (a / b) #División
print (a // b) #División entera
print (a * b) #Multiplicación
print (a % b) #Devuelve el resto de una división
print (a ** b) #Eleva un número a la potencia de otro

#Operaciones Comparativas
print (a == b)
print (a != b)
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)

#Operadores Lógicos
x = True
y = False

print (x and y) #Devuelve 'True' si ambas condiciones son True
print (a or b) #Devuelve 'True' si alguna de las condiciones son True
print (not a) #Invierte el valor de una condición

#Operadores de Membresía
my_list = [1, 2, 3, 4]
print(3 in my_list)      # Devuelve 'True' si el valor está en la secuencia
print(5 not in my_list)  # Devuelve 'True' si el valor no está en la secuencia

#Operadores de Identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # Devuelve 'True' si ambas variables apuntan al mismo objeto
print(a is not c)  # Devuelve 'True' si ambas variables apuntan a objetos diferentes

#Operadores a Nivel de Bit
a = 5 # En binario: 0101
b = 3 # En binario: 0011

# AND bit a bit
# Compara bit a bit y devuelve 1 donde coinciden los operando a 1
print(bin(a & b))  # Salida: 0001 (1 en decimal)

# OR bit a bit
# Compara bit a bit y devuelve los que están a 1
print(bin(a | b))  # Salida: 0111 (7 en decimal)

# XOR bit a bit
# Devuelve 1 cuando uno de los bits (y no ambos) es 1
print(bin(a ^ b))  # Salida: 0110 (6 en decimal)

# NOT bit a bit
# Cambia cada 0 a 1 y cada 1 a 0
a = 5 # En binario: 0000 0101
print(bin(~a))     # Salida: 1111 1010 (-6 en decimal)

# Desplazamiento a la izquierda
""" Mueve todos los bits a la izquierda la 
cantidad de posiciones que se especifique """
print(bin(a << 1))  # Salida: 0000 1010 (10 en decimal)

# Desplazamiento a la derecha
""" Mueve todos los bits a la derecha la 
cantidad de posiciones que se especifique """
print(bin(a >> 1))  # Salida: 0000 0010 (2 en decimal)

# EXTRA #
""" Crea un programa que imprima por consola todos los
números comprendidos entre 10 y 55 (incluidos), pares, 
y que no son ni el 16 ni múltiplos de 3."""
for i in range(10, 56):
    if (i != 16) and (i % 2 == 0) and (i % 3 != 0):
        print(i)