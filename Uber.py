class Usuario:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def solicitar_viaje(self, origen, destino, metodo_pago, vehiculo):
        return Viaje(self, origen, destino, metodo_pago, vehiculo)

    def __str__(self):
        return f"Usuario: {self.nombre}, Tel: {self.telefono}"


class Conductor:
    def __init__(self, nombre, licencia, calificacion, vehiculo):
        self.nombre = nombre
        self.licencia = licencia
        self.calificacion = calificacion
        self.vehiculo = vehiculo

    def aceptar_viaje(self, viaje):
        viaje.conductor = self
        viaje.estado = "En curso"
        return f"{self.nombre} aceptó el viaje con {viaje.usuario.nombre}"

    def finalizar_viaje(self, viaje):
        viaje.estado = "Finalizado"
        return f"{self.nombre} finalizó el viaje."


class Vehiculo:
    def __init__(self, placa, modelo, tipo):
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return f"Vehículo {self.tipo} - Placa {self.placa}"


class MetodoPago:
    def __init__(self, tipo, detalle=""):
        self.tipo = tipo
        self.detalle = detalle

    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con {self.tipo}"


class Viaje:
    def __init__(self, usuario, origen, destino, metodo_pago, vehiculo):
        self.usuario = usuario
        self.conductor = None
        self.origen = origen
        self.destino = destino
        self.metodo_pago = metodo_pago
        self.vehiculo = vehiculo
        self.estado = "Pendiente"
        self.tarifa = self.calcular_tarifa()

    def calcular_tarifa(self):
        # Tarifa de ejemplo
        return 5000 + len(self.destino) * 100

    def __str__(self):
        return (f"Viaje de {self.usuario.nombre} en {self.vehiculo.tipo}, "
                f"estado: {self.estado}, tarifa: {self.tarifa}")


Usuario1 = Usuario("Daniela", "3202763186", "daniela@gmail.com")
Vehiculo1 = Vehiculo("ABC123", "Mazda 3", "UberX")
Pago1 = MetodoPago("Tarjeta de Crédito", "****1234")

viaje1 = Usuario1.solicitar_viaje("Calle 10", "Carrera 20", Pago1, Vehiculo1)
print(viaje1)

conductor1 = Conductor("David", "LIC123", 4.9, Vehiculo1)
print(conductor1.aceptar_viaje(viaje1))
print(viaje1)

print(conductor1.finalizar_viaje(viaje1))
print(Pago1.procesar_pago(viaje1.tarifa))
