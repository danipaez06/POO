class Perro:
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza

    def ladrar (self):
        return "¡Guau!¡Guau!"
    
    def datos (self):
        return f"{self.nombre} es de raza {self.raza}"
    
p1 = Perro ("lulu", "Pastor Alemán")
p2 = Perro("killer", "chandanes")
    
print(p1.nombre)# Output: Rex (atributo)
print(p1.ladrar())
print(p2.nombre)
print(p2.datos())




    
    
