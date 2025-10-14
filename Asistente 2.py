class ReproductorMusica:
    def __init__(self):
        self.cancion_actual = None
        self.reproduciendo = False

    def reproducir(self, cancion):
        self.cancion_actual = cancion
        self.reproduciendo = True
        print(f"\nReproduciendo la canción: {self.cancion_actual}")

    def pausar(self):
        if self.reproduciendo:
            self.reproduciendo = False
            print("\nLa música ha sido pausada.")
        else:
            print("\nNo hay ninguna canción reproduciéndose.")


class CalculadoraTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(f"\nTarea '{tarea}' agregada correctamente.")

    def mostrar_tareas(self):
        if self.tareas_pendientes:
            print("\nTareas pendientes:")
            for tarea in self.tareas_pendientes:
                print(f"- {tarea}")
        else:
            print("\nNo hay tareas pendientes.")



    def presentar(self):
        print(f"\nHola, soy {self.nombre}, tu asistente multifuncional.")
        print("Puedo reproducir música y ayudarte con tus tareas :)")

    def mostrar_menu(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Reproducir una canción")
        print("2. Pausar música")
        print("3. Agregar una tarea")
        print("4. Ver tareas pendientes")
        print("5. Salir")

    def ejecutar(self):
        self.presentar()
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                cancion = input("\nIngrese el nombre de la canción: ")
                self.reproducir(cancion)
            elif opcion == "2":
                self.pausar()
            elif opcion == "3":
                tarea = input("\nIngrese una tarea: ")
                self.agregar_tarea(tarea)
            elif opcion == "4":
                self.mostrar_tareas()
            elif opcion == "5":
                print("\nFin del programa :)")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    print("----- ASISTENTE MULTIFUNCIONAL -----")
    nombre = input("Ingrese el nombre de su asistente: ")
    asistente = AsistenteMultifuncional(nombre)
    asistente.ejecutar()
