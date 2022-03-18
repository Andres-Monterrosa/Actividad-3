from Poo3 import *
from math import floor


class Main(Menu):

    def __init__(self) -> None:
        super().__init__()
        self.__lista = []
        self.__SUB_TRA = 60000
        self.__SUB_ALI = 80000
        self.__PENSION = 0.04
        self.__SALUD = 0.03375
        self.__total = 0
        self.main()

    def mostrarLista(self):
        if self.__lista == []:
            print ("¡No hay registros, la lista está vacía!")
        else: 
            
            [print(f"Posicion[{p}]: {x}") for (p, x) in enumerate(self.__lista)]

    def agregarEmpleado(self):
        sl = float(input('Digite el salario del empleado:'))
        datosEmpleado = {
            'Nombre': input('Digite el nombre del empleado:'),
            'Edad': int(input('Digite la edad del empleado:')),
            'Salario': sl,
            "Devengado": self._calcularDevengado(sl),
            'Deduciones': self._calcularDeducciones(sl),
            'SalarioFinal': self._calcularSalarioFinal(sl)
        }

        self.__lista.append(datosEmpleado)
        print('El empleado se ha agregado correctamente.')

    def borrarEmpleado(self):
        empleado = input('Digite el nombre del empleado que desea borrar: ')
        for elemento in self.__lista:
            if elemento['Nombre'] == empleado:
                self.__lista.remove(elemento)
                print("")
                print('El empleado se ha eliminado correctamente.')
            else:
                print('El empleado no existe o se equivocó al escribir.')

    def _calcularDevengado(self,salario) -> float:
        if salario < 2000000:
            return (self.__SUB_ALI + self.__SUB_TRA)
        else:
            return 0                      


    def _calcularDeducciones(self,salario):
        
        pension = salario * self.__PENSION
        salud = salario * self.__SALUD
        saludPension = pension + salud
        
        return saludPension
               

    def _calcularSalarioFinal(self,salario):
       deducciones = self._calcularDeducciones(salario)
       devengado = self._calcularDevengado(salario)

       return salario + devengado - deducciones

    def main(self):
        while True:
            if self.choise == '1':
                self.mostrarLista()
            elif self.choise == "2":
                self.agregarEmpleado()
            elif self.choise == "3":
                self.borrarEmpleado()
            elif self.choise == "4":
                break
            print("")
            input('Presione enter para continuar:')
            self.menu()


if __name__ == "__main__":
    Main()