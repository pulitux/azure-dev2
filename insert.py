import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    ConsultaAlta = ("INSERT INTO emp "
                    "(emp_no,apellido,oficio,dir,fecha_alt,salario, comision,dept_no) "
                    "VALUES (:P1, :P2, :P3, :P4, to_date(:P5,'dd-mm-yyyy'), :P6, :P7, :P8)")

    datosEmpleados = (1111, 'Benito', 'Programado', 7566, '4-6-1976', 100000, 100, 20)

    cursor.execute(ConsultaAlta, datosEmpleados)

    connection.commit()


except connection.Error as error:
    print("Error: ", error)

connection.close()