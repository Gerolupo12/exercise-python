import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="prueba"
)

cursor = midb.cursor()

# listar datos
# cursor.execute('select * from usuario')
# resultado = cursor.fetchall()
# print(resultado)

cursor.execute('select * from usuario limit 2')
resultado = cursor.fetchall()
print(resultado)

# ver definiciones de tablas
# cursor.execute('show create table usuario')

# insertar datos
# sql = 'insert into usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@correo.co.ne', 'nombreusuario', 45)

# update datos
# sql = 'update usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 4)

# cursor.execute(sql, values)

# midb.commit()

# print(cursor.rowcount)\

# eliminar datos
# sql = 'delete from usuario where id = %s'
# values = (4,)
# cursor.execute(sql, values)
# midb.commit()

