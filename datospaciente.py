import cx_Oracle
class Paciente:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
    def consulta(self, nss):
        cursor = self.connection.cursor()
        nombre = cursor.var(cx_Oracle.STRING)
        sexo = cursor.var(cx_Oracle.STRING)

        cursor = self.connection.cursor()
        try:
            args = (nss, nombre, sexo)
            cursor.callproc('DatosPaciente', args)
            return nombre.getvalue(), 'HOMBRE' if sexo.getvalue() == 'M' else 'MUJER'
        except self.connection.Error as error:
            print("Error: ", error)

def menu():
    print("")
    print("1. Consulta de Paciente")
    print("2. Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Ingrese una opcion valida")
        return menu()
    print("")
    return opcion

def main():
    paciente = Paciente()

    while True:
        opcion = menu()
        if opcion == 1:
            nss = input("Ingrese el numero de nss: ")
            nombre, sexo = paciente.consulta(nss)
            print(f'Nombre: {nombre}\tSexo: {sexo}')
        elif opcion == 2:
            break
        else:
            print("Ingrese una opcion valida")
    paciente.connection.close()

if __name__ == '__main__':
    main()