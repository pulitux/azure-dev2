import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    cursor.execute("select emp_no, apellido, loc from emp inner join dept on emp.dept_no = dept.dept_no")

    print("Lista de empleados:")
    print("---------------------------------------")

    for no, ape, loc in cursor:
            print(f"Numero: {no}\tApellido:", ape, "\tLocalidad: ", loc)


except connection.Error as error:
    print("Error: ", error)

connection.close()

# from emp inner join dept
# on emp.dept_no = dept.dept_no; -- solo registros con correspondencia en las dos tablas
# select apellido, loc