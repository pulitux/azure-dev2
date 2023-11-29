import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    cursor.execute("select apellido, loc from emp inner join dept on emp.dept_no = dept.dept_no")

    print("Lista de empleados:")
    print("---------------------------------------")

    for ape, loc in cursor:
            print("Apellido:", ape, "\tLocalidad: ", loc)


except connection.Error as error:
    print("Error: ", error)

connection.close()

# from emp inner join dept
# on emp.dept_no = dept.dept_no; -- solo registros con correspondencia en las dos tablas
# select apellido, loc