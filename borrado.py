import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    NumeroEmpleado = int(input("Introduce Empleado: "))
    ConsultaBaja = 'DELETE FROM emp WHERE emp_no=:p1'
    cursor.execute(ConsultaBaja, (NumeroEmpleado,))

    if cursor.rowcount > 0:
        print("Empleado eliminado")
    else:
        print("Empleado no encontrado")

    connection.commit()

except connection.Error as error:
    print("Error: ", error)

connection.close()
