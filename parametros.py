import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    miOficio = input("Introduce Oficio Empleado: ").upper()
    miSalario = int(input('Introduce un sala minimo: '))
    consulta = ("SELECT apellido,oficio,salario FROM emp where oficio=:p1 and salario > :p2")
    cursor.execute(consulta, (miOficio,miSalario))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))



except connection.Error as error:
    print("Error: ", error)

connection.close()
