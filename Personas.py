class Persona:
    nombre = ""
    edad = 0
    altura = 0
    genero = ""
    
    def caminar (self):
        return   f"Hola, soy {self.nombre} y estoy caminando..."
    
    def hablar (self):
        return f"Me gusta estar en clase."
    
persona1 = Persona ()
persona2 = Persona ()
persona3 = Persona ()

persona1.nombre = "Daniela"
persona1.edad = "18"
persona1.altura = "1.62"
persona1.genero = "Femenino"
persona2.nombre = "David"
persona3.nombre = "Jungkook"

print (persona1.nombre)
print (persona1.edad)
print (persona1.altura)
print (persona1.genero)

print(persona1.caminar())
print(persona1.hablar())

#print (persona2.nombre)
#print (persona3.nombre)