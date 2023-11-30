import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    ConsultaModificacion = ("Update emp set salario=:Param1 where emp_no=:Param2")

    NumeroEmpleado = input("Número de empleado a modificar:")
    NuevoSal = input("Nuevo salario:")

    cursor.execute(ConsultaModificacion, (NuevoSal, NumeroEmpleado))
    if cursor.rowcount > 0:
        print("Registro modificado satisfactoriamente")
    else:
        print("Dato no encontrado")

    connection.commit()


except connection.Error as error:
    print("Error: ", error)

connection.close()