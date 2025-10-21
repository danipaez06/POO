class Persona:
  def __init__(self, edad):
    self._edad = edad

  @property
  def edad(self):
    return self._edad

persona = Persona(28)
persona.edad # Retorna 28
persona.edad = 500 # Esto no es posible con encapsulamiento