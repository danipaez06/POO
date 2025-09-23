class Persona2 ():
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
    
personas_encuestadas = []  
while True:
    opciones = int (input(""" Selecciona:
    1. Ingresar datos.
    2. Ver datos.
    3. Salir. """))
    print ("\n1")
    
    if opciones == 3:
        break
    elif opciones == 1:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))  
        estatura = float(input("Ingrese su estatura: "))
        profesion = input("Ingrese su profesion: ")
        print ("\n **********")
        
        persona = Persona2 (nombre, edad, estatura, profesion)
        personas_encuestadas.append(persona)
    elif opciones == 2:
        for persona in personas_encuestadas:
            print (persona.enseñar())
            print (persona.hablar())
            print (persona.estudiar())
            print ("\n **********")
            
    else:
        print ("Opcion no valida. Intente nuevamente.")      
    