import modulos as xs
# from modulos import saludo, mascotas #seleccionamos lo que queremos importar   
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oracion necesita camelcase!'

camelcased = c.hump(s)
print(camelcased)