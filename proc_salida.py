import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

cursor = connection.cursor()
try:

    dp = input("Número de departamento:")
    loc = cursor.var(cx_Oracle.STRING)

    args = (loc, dp)
    cursor.callproc('DevolverLocalidad', args)
    print(loc.getvalue())

except connection.Error as error:
    print("Error: ", error)
cursor.close()
connection.close()