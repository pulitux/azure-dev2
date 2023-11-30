import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:
    minSalario = int(input('Introduce un sala minimo: '))
    maxSalario = int(input('Introduce un sala maximo: '))
    consulta = ("SELECT apellido,oficio,salario FROM emp where salario between :p1 and :p2")
    cursor.execute(consulta, (minSalario, maxSalario))

    # print(cursor.rowcount, "registros encontrados")
    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))
    print (cursor.rowcount, "registros encontrados")

except connection.Error as error:
    print("Error: ", error)

connection.close()
