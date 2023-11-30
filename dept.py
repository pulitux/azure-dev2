import cx_Oracle

def altaDepartamento():
    while True:
        try:
            codigo = int(input("Ingrese el codigo del departamento: "))
        except ValueError:
            continue
        break
    nombre = input("Ingrese el nombre del departamento: ").upper()
    localidad = input("Ingrese la localidad del departamento: ").upper()

    connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = connection.cursor()

    try:
        ConsultaAlta = "INSERT INTO dept VALUES (:P1, :P2, :P3)"
        cursor.execute(ConsultaAlta, (codigo, nombre, localidad))
        if cursor.rowcount == 1:
            print("Departamento registrado")
        else:
            print("Departamento no registrado")
        connection.commit()
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

def bajaDepartamento():
    while True:
        try:
            codigo = int(input("Ingrese el codigo del departamento: "))
        except ValueError:
            continue
        break

    connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = connection.cursor()

    try:
        ConsultaBaja = "DELETE FROM dept where dept.dept_no = :P1"
        cursor.execute(ConsultaBaja, (codigo,))
        if cursor.rowcount == 1:
            print("Departamento eliminado")
        else:
            print("Departamento no eliminado")
        connection.commit()
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

def modificacionDepartamento():
    while True:
        try:
            codigo = int(input("Ingrese el codigo del departamento: "))
        except ValueError:
            continue
        break
    localidad = input("Ingrese la nueva localidad del departamento: ").upper()

    connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = connection.cursor()

    try:
        ConsultaModificacion = "UPDATE dept SET loc = :P1 WHERE dept.dept_no = :P2"
        cursor.execute(ConsultaModificacion, (localidad, codigo))
        if cursor.rowcount == 1:
            print("Departamento modificado")
        else:
            print("Departamento no modificado")
        connection.commit()
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

def consultaDepartamento():
    connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    cursor = connection.cursor()

    try:
        ConsultaConsulta = "SELECT * FROM dept ORDER BY dept.dept_no ASC"
        cursor.execute(ConsultaConsulta)
        for codigo, nombre, localidad in cursor:
            print(f'Codigo: {codigo}\tNombre: {nombre}\tLocalidad: {localidad}')
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

def main():

    while True:
        opcion = menu()
        if opcion == 1:
            altaDepartamento()
        elif opcion == 2:
            bajaDepartamento()
        elif opcion == 3:
            modificacionDepartamento()
        elif opcion == 4:
            consultaDepartamento()
        elif opcion == 5:
            break
        else:
            print("Ingrese una opcion valida")

def menu():
    print("")
    print("1. Alta de Departamento")
    print("2. Baja de Departamento")
    print("3. Modificacion de Departamento")
    print("4. Consulta de Departamento")
    print("5. Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Ingrese una opcion valida")
        return menu()
    print("")
    return opcion

if __name__ == '__main__':
    main()