import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    nss = input("Número de nss: ")
    nombre = cursor.var(cx_Oracle.STRING)
    sexo = cursor.var(cx_Oracle.STRING)

    args = (nss, nombre, sexo)
    cursor.callproc('DatosPaciente', args)
    print('Nombre: ', nombre.getvalue())
    print('Sexo: ', 'HOMBRE' if sexo.getvalue() == 'M' else 'MUJER')

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()