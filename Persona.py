class Persona ():
    nombre = ""
    edad = 0
    estatura = 0
    profesion = ""
    
    def __init__(self, nombre, edad, estatura, profesion):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.profesion = profesion
    
    def enseñar (self):
        return f"Hola soy {self.nombre} y estoy enseñando Python."
    def hablar (self):
        return f"Mi profesion es {self.profesion} y estoy hablando sobre el metodo constructor."
    def estudiar (self):
        return f"Estoy en UNIMINUTO y tengo {self.edad} años."
    
persona1 = Persona ("Daniela", 18, 1.62, "Estudiante")
persona2 = Persona ("David", 22, 1.72, "Diseñador")
persona3 = Persona ("Jungkook", 27, 1.80, "Cantante")

print (persona1.enseñar())
print (persona1.hablar())
print (persona1.estudiar())
print ("\n**********")
print (persona2.enseñar())
print ("\n**********")
print (persona3.estudiar())