class Menu:
    choise = ""

    def __init__(self) -> None:
        self.menu()

    def menu(self):
        print('------------------------------------------')
        print('1: Ver la lista')
        print('2: Agregar empleado')
        print('3: Borrar empleado')
        print('4: exit')
        print('------------------------------------------')
        self.choise = input('Elige una opcion: ')