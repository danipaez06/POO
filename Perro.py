class Perro:
    def __init__(self, nombre, raza):
        print (f"El nombre de mi perro es {nombre} y es der raza {raza}.")
        self.nombre=nombre
        self.raza=raza
perro1 = Perro ("Luna","Pastor Aleman")