# multiplicar dos numeros sin usar el simbolo de multiplicacion
a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b 

print(resultado)

# ingresar un nombre y apellido e imprimiirlo al reves
nombre = 'Geronimo'
apellido = 'Feliz' 

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])

# escribir una funcion que encuentre el elemento menor de una lista

lista = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)

# escribir una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calcularVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(6)
print(resultado)

# escribir una funcion que indique si el usuario es mayor de edad

# escribir una funcion que iondique si el numero es impar o par

# escribir una funcion que indique cuantas vocales tiene una palabra

# escribir una aplicacion que reciba una cantidad infinita de numeros
# hasta decir basta, luego que defvuelva la suma de los numeros ingresados

# escribir una funcion que reciba nombre y apellido y los vaya agregando a 
# un archivo