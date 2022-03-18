
class Persona():
    nombre = ""
    apellido = ""
    direccion = ""
    telefono = "" 
        
    def __init__(self, nombre, apellido, direccion, telefono) ->None:
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
            print(f"Direccion: {self.direccion}")
            print(f"Numero de telefono: {self.telefono}")


def main():
    persona1 = Persona(nombre="Andres", apellido="Monterrosa", direccion="carrera 17 # 14b-10", telefono="3136708763")         #Crear una instamcia de la clase 
    
    persona1.mostrarPersona()




if __name__ == "__main__":
    main()