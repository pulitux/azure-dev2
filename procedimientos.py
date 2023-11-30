import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    nombre = input("Nombre departamento:").upper()
    localidad = input("localidad:").upper()

    cursor.callproc("InsertarDEPT", (dp, nombre, localidad))

    if cursor.rowcount > 0:
        print("Registro insertado satisfactoriamente")
    else:
        print("Dato no encontrado")



except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()