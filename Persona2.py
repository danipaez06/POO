class Persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.edad = edad
        self.genero = genero
        
    @property
    def Nombre (self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre (self, value):
        self.__nombre = value

P1 = Persona ("Daniela", 19, "Femenino")
print (P1.Nombre)

P1.Nombre = "Dani P"
print(P1.Nombre)