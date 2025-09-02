class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
Daniela = Estudiante("Vivian Daniela", "18", "3° semestre")
Juan = Estudiante("Juan Esteban", "20", "3° semestre")  
    
print(Daniela.nombre)  
print(Daniela.edad)  
print(Juan.edad)  
    