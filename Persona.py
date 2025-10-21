class Persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.genero = genero
        
    @property
    def Nombre (self):
        return self.__nombre
    
    @property
    def Edad (self):
        return self.__edad
    
P1 = Persona ("Daniela", 19, "Femenino")
print(P1.Nombre, P1.Edad)