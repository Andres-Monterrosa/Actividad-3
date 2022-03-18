from re import S


def main():
    class Persona():
        def __init__(self) -> None:
            self.nombre = input("Ingresar el nombre:  ")
            self.apellido = input("Ingresar el apellido:  ")
            self.direccion = input("Ingresar el direccion:  ")
            self.telefono = input("Ingresar el telefono:  ")

        def mostrarPersona(self):
            print(f"nombre: {self.nombre} {self.apellido}")

    class Empleado(Persona):
        def __init__(self) -> None:
            super().__init__()
            self.__sueldo = float(input("Ingrese el sueldo:  "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
        def mostrarempleado(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Transporte: {self.transporte}")
            print(f"Alimentacion: {self.alimentacion}")
            print(f"Pension: {self.pension}")

    empleado1 = Empleado()
    empleado1.mostrarempleado()

if __name__ == "__main__":
    main()