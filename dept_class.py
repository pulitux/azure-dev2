import cx_Oracle


class Departamento:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    def alta(self):
        while True:
            try:
                codigo = int(input("Ingrese el codigo del departamento: "))
            except ValueError:
                continue
            break
        nombre = input("Ingrese el nombre del departamento: ").upper()
        localidad = input("Ingrese la localidad del departamento: ").upper()

        # connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = self.connection.cursor()

        try:
            ConsultaAlta = "INSERT INTO dept VALUES (:P1, :P2, :P3)"
            cursor.execute(ConsultaAlta, (codigo, nombre, localidad))
            if cursor.rowcount == 1:
                print("Departamento registrado")
            else:
                print("Departamento no registrado")
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        # connection.close()

    def baja(self):
        while True:
            try:
                codigo = int(input("Ingrese el codigo del departamento: "))
            except ValueError:
                continue
            break

        # connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = self.connection.cursor()

        try:
            ConsultaBaja = "DELETE FROM dept where dept.dept_no = :P1"
            cursor.execute(ConsultaBaja, (codigo,))
            if cursor.rowcount == 1:
                print("Departamento eliminado")
            else:
                print("Departamento no eliminado")
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        # self.connection.close()

    def modificacion(self):
        while True:
            try:
                codigo = int(input("Ingrese el codigo del departamento: "))
            except ValueError:
                continue
            break
        localidad = input("Ingrese la nueva localidad del departamento: ").upper()

        # connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = self.connection.cursor()

        try:
            ConsultaModificacion = "UPDATE dept SET loc = :P1 WHERE dept.dept_no = :P2"
            cursor.execute(ConsultaModificacion, (localidad, codigo))
            if cursor.rowcount == 1:
                print("Departamento modificado")
            else:
                print("Departamento no modificado")
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        # connection.close()

    def consulta(self):
        # connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
        cursor = self.connection.cursor()

        try:
            ConsultaConsulta = "SELECT * FROM dept ORDER BY dept.dept_no ASC"
            cursor.execute(ConsultaConsulta)
            for codigo, nombre, localidad in cursor:
                print(f'Codigo: {codigo}\tNombre: {nombre}\tLocalidad: {localidad}')
        except self.connection.Error as error:
            print("Error: ", error)
        cursor.close()
        # connection.close()


def main():
    departamento = Departamento()

    while True:
        opcion = menu()
        if opcion == 1:
            departamento.alta()
        elif opcion == 2:
            departamento.baja()
        elif opcion == 3:
            departamento.modificacion()
        elif opcion == 4:
            departamento.consulta()
        elif opcion == 5:
            break
        else:
            print("Ingrese una opcion valida")
    departamento.connection.close()


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
