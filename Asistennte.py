class ReproductorMusica:
    def __init__(self):
        self.cancion_actual = None
        self.reproduciendo = False

    def reproducir(self, cancion):
        self.cancion_actual = cancion
        self.reproduciendo = True
        print(f"Reproduciendo la canción: {self.cancion_actual}")

    def pausar(self):
        if self.reproduciendo:
            self.reproduciendo = False
            print("La música ha sido pausada.")
        else:
            print("No hay ninguna canción reproduciéndose.")

class CalculadoraTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(f"Tarea '{tarea}' agregada correctamente.")

    def mostrar_tareas(self):
        if self.tareas_pendientes:
            print("Tareas pendientes:")
            for tarea in self.tareas_pendientes:
                print(f"- {tarea}")
        else:
            print("No hay tareas pendientes.")

class AsistenteMultifuncional(ReproductorMusica, CalculadoraTareas):
    def __init__(self, nombre):
        ReproductorMusica.__init__(self)
        CalculadoraTareas.__init__(self)
        self.nombre = nombre

    def presentar(self):
        print(f"Hola, soy {self.nombre}, tu asistente multifuncional.")
        print("Puedo reproducir música y ayudarte a organizar tus tareas :)")

def ejecutar_asistente():
    print("----- ASISTENTE MULTIFUNCIONAL -----")

    asistente = AsistenteMultifuncional("Luna")
    asistente.presentar()

    print("\n--- FUNCIÓN DE REPRODUCTOR DE MÚSICA ---")
    asistente.reproducir("Shape of You")
    asistente.pausar()

    print("\n--- FUNCIÓN DE CALCULADORA DE TAREAS ---")
    asistente.agregar_tarea("Estudiar para el examen")
    asistente.agregar_tarea("Hacer ejercicio")
    asistente.mostrar_tareas()

ejecutar_asistente()
