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
        return f"El conductor {self.nombre} aceptó el viaje con {viaje.usuario.nombre}"

    def finalizar_viaje(self, viaje):
        viaje.estado = "Finalizado"
        return f"{self.nombre} finalizó el viaje."


class Vehiculo:
    tarifas = {
        "Uber X": 5000,
        "Uber Black": 7000,
        "Uber Pool": 9000,
        "Uber Van": 12000
    }
    def __init__(self, placa, modelo, tipo):
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo
        
    def calcular_tarifa (self, distancia):
        tarifa_base = self.tarifas.get(self.tipo, 10)
        return tarifa_base * distancia

    def __str__(self):
        return f"Vehículo {self.tipo} - Placa {self.placa}"


class MetodoPago:
    def __init__(self, tipo, detalle=""):
        self.tipo = tipo
        self.detalle = detalle

    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con {self.tipo}"


class Viaje:
    def __init__(self, usuario, origen, destino, metodo_pago, vehiculo, distancia):
        self.usuario = usuario
        self.conductor = None
        self.origen = origen
        self.destino = destino
        self.metodo_pago = metodo_pago
        self.vehiculo = vehiculo
        self.estado = "Pendiente"
        self.distancia = self
        self.tarifa = self.calcular_tarifa()

    def __str__(self):
        return (f"Viaje de {self.usuario.nombre} en {self.vehiculo.tipo}, "
                f"estado: {self.estado}, tarifa: {self.tarifa}")


def main ():
    print ("Inicio de sesión para usuario: ")
    nombre = input ("Por favor, ingrese su nombre: ")
    telefono = input ("Por favor, confirme su numero de telefono: ")
    email = input ("Por favor, confirme su email: ")
    Usuario1 = Usuario(nombre, telefono, email)
    
    