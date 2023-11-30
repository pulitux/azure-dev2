import cx_Oracle


class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def buscaSalarioComision(self, empleado):
        cursor = self.connection.cursor()
        salario = cursor.var(cx_Oracle.NUMBER)
        comision = cursor.var(cx_Oracle.NUMBER)

        try:
            args = (empleado, salario, comision)
            cursor.callproc('empleados.SalarioComisionBusca', args)
            cursor.close()
            return salario.getvalue(), comision.getvalue()
        except self.connection.Error as error:
            # print("Error: ", error)
            cursor.close()
            return error, 0

    def modSalarioComision(self, empleado, salario, comision):
        cursor = self.connection.cursor()
        count = cursor.var(cx_Oracle.NUMBER)

        try:
            args = (empleado, salario, comision, count)
            cursor.callproc('empleados.SalarioComisionMod', args)
            cursor.close()
            # print (type(count))
            return count.getvalue()
        except self.connection.Error as error:
            return error


# def menu():
#     print("")
#     print("1. Consulta de Salario")
#     print("2. Modificacion de Salario")
#     print("3. Salir")
#     try:
#         opcion = int(input("Ingrese una opcion: "))
#     except ValueError:
#         print("Ingrese una opcion valida")
#         return menu()
#     print("")
#     return opcion
#
#
# def consulta_salario():
#     empleado = input("Ingrese el numero de empleado: ")
#     salario, comision = Empleado().buscaSalarioComision(empleado)
#     print(f'Salario: {salario}\tComision: {comision}')
#
#
# def modificacion_salario():
#     empleado = input("Ingrese el numero de empleado: ")
#     salario = int(input("Ingrese el nuevo salario: "))
#     comision = int(input("Ingrese la nueva comision: "))
#     Empleado().modSalarioComision(empleado, salario, comision)
#
#
# def main():
#     while True:
#         opcion = menu()
#         if opcion == 1:
#             consulta_salario()
#         elif opcion == 2:
#             modificacion_salario()
#         elif opcion == 3:
#             break
#         else:
#             print("Ingrese una opcion valida")
#     Empleado().connection.close()

#
# if __name__ == '__main__':
#     main()