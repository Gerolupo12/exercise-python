import random   
import string

longitud = int(input("Ingrese la cantidad de letras de tu password: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(caracteres) for i in range(longitud))

print("La password generada es: " + password)