class Persona:
    # Constructor con atributos en snake_case
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para mostrar la información de la persona
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
