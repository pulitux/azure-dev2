from empleados import Empleado
class Menu:
    def __init__(self):
        pass
    def principal(self):
        print("")
        print("1. Consulta de Salario")
        print("2. Modificacion de Salario")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            return self.principal()
        if opcion == 1:
            self.consulta_salario()
            self.principal()
            return
        elif opcion == 2:
            self.modificacion_salario()
            self.principal()
            return
        elif opcion == 3:
            return
        else:
            print("Ingrese una opcion valida")
            self.principal()

    def consulta_salario(self):
        empleado = input("Ingrese el numero de empleado: ")
        salario, comision = Empleado().buscaSalarioComision(empleado)
        print(f'Salario: {salario}\tComision: {comision}')

    def modificacion_salario(self):
        empleado = input("Ingrese el numero de empleado: ")
        salario = int(input("Ingrese el nuevo salario: "))
        comision = int(input("Ingrese la nueva comision: "))
        count = Empleado().modSalarioComision(empleado, salario, comision)
        print(f'Moficación de salario realizada sobre {count} empleados')

def main():
    menu = Menu()
    menu.principal()

if __name__ == '__main__':
    main()