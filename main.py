import tkinter as tk


class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"


class BandaEscolar(Participante):
    CATEGORIAS_VALIDAS = ["Primaria", "Básico", "Diversificado"]
    CRITERIOS = ["ritmo", "uniformidad", "coreografia", "alineacion", "puntualidad"]

    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = None
        self._puntajes = {}
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria not in self.CATEGORIAS_VALIDAS:
            raise ValueError(f"Categoría inválida. Debe ser una de: {self.CATEGORIAS_VALIDAS}")
        self._categoria = categoria

    def registrar_puntajes(self, puntajes_dict):
        criterios_recibidos = list(puntajes_dict.keys())
        if len(criterios_recibidos) != len(self.CRITERIOS):
            raise ValueError(f"Debe proporcionar puntajes para todos los criterios: {self.CRITERIOS}")

        for criterio in self.CRITERIOS:
            if criterio not in criterios_recibidos:
                raise ValueError(f"Falta el criterio: {criterio}")
        for criterio, puntaje in puntajes_dict.items():
            if not (0 <= puntaje <= 10):
                raise ValueError(f"Puntaje para {criterio} debe estar entre 0 y 10")
        self._puntajes = puntajes_dict

    @property
    def total(self):
        if not self._puntajes:
            return 0
        suma = 0
        for puntaje in self._puntajes.values():
            suma += puntaje
        return suma

    @property
    def promedio(self):
        if not self._puntajes:
            return 0
        return self.total / len(self._puntajes)

    @property
    def puntajes(self):
        return self._puntajes.copy()

    def fue_evaluada(self):
        return bool(self._puntajes)

    def mostrar_info(self):
        info_base = f"{self.nombre} - {self.institucion} ({self.categoria})"
        if self.fue_evaluada():
            return f"{info_base} - Puntaje: {self.total}"
        return info_base


class Concurso:
    def __init__(self, nombre_concurso, fecha):
        self.nombre_concurso = nombre_concurso
        self.fecha = fecha
        self._bandas = {}

    def inscribir_banda(self, banda):
        if banda.nombre in self._bandas:
            raise ValueError(f"Ya existe una banda con el nombre '{banda.nombre}'")
        self._bandas[banda.nombre] = banda
        return f"Banda '{banda.nombre}' inscrita exitosamente"

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self._bandas:
            raise ValueError(f"No existe una banda con el nombre '{nombre_banda}'")
        banda = self._bandas[nombre_banda]
        banda.registrar_puntajes(puntajes)
        return f"Puntajes registrados para la banda '{nombre_banda}'"

    def listar_bandas(self):
        if not self._bandas:
            print("Aun no hay bandas inscritas")
            return
        print(f"\n--- LISTADO DE BANDAS - {self.nombre_concurso} ---")
        for nombre, banda in self._bandas.items():
            info = banda.mostrar_info()
            if banda.fue_evaluada():
                print(f"{info}")
                for criterio, puntaje in banda.puntajes.items():
                    print(f"{criterio.capitalize()}: {puntaje}")
            else:
                print(f"{info} (Sin evaluar)")
            print()


class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        # Crear instancia del concurso
        self.concurso = Concurso("Concurso 14 de Septiembre", "2024-09-14")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x300")

        etiqueta_inscribir = tk.Label(ventana_inscribir, text="Inscribir Banda")
        etiqueta_inscribir.pack(pady=5)

        etiqueta_nombre = tk.Label(ventana_inscribir, text="Ingrese el nombre de la banda: ")
        etiqueta_nombre.pack(pady=5)

        entrada_nombre = tk.Entry(ventana_inscribir)
        entrada_nombre.pack(pady=5)

        etiqueta_institucion = tk.Label(ventana_inscribir, text="Ingrese la institución: ")
        etiqueta_institucion.pack(pady=5)

        entrada_institucion = tk.Entry(ventana_inscribir)
        entrada_institucion.pack(pady=5)

        etiqueta_categoria = tk.Label(ventana_inscribir, text="Ingrese la categoria de la banda: ")
        etiqueta_categoria.pack(pady=5)

        entrada_categoria = tk.Entry(ventana_inscribir)
        entrada_categoria.pack(pady=5)

        def guardar_banda():
            nombre = entrada_nombre.get()
            institucion = entrada_institucion.get()
            categoria = entrada_categoria.get()

            try:
                banda = BandaEscolar(nombre, institucion, categoria)
                resultado = self.concurso.inscribir_banda(banda)
                print(resultado)
                ventana_inscribir.destroy()
            except ValueError as e:
                print(f"Error: {e}")

        boton_inscribir = tk.Button(ventana_inscribir, text="Inscribir Banda", command=guardar_banda)
        boton_inscribir.pack(pady=5)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_eval = tk.Toplevel(self.ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("400x400")

        etiqueta_ritmo = tk.Label(ventana_eval, text="Ingrese numero de puntos obtenidos en ritmo (1-10): ")
        etiqueta_ritmo.pack(pady=5)

        entrada_ritmo = tk.Entry(ventana_eval)
        entrada_ritmo.pack(pady=5)

        etiqueta_uniformidad = tk.Label(ventana_eval,
                                        text="Ingrese el numero de puntos obtenidos en uniformidad (1-10): ")
        etiqueta_uniformidad.pack(pady=5)

        entrada_uniformidad = tk.Entry(ventana_eval)
        entrada_uniformidad.pack(pady=5)

        etiqueta_coreografia = tk.Label(ventana_eval,
                                        text="Ingrese el numero de puntos obtenidos en coreografia (1-10): ")
        etiqueta_coreografia.pack(pady=5)

        entrada_coreografia = tk.Entry(ventana_eval)
        entrada_coreografia.pack(pady=5)

        etiqueta_alineacion = tk.Label(ventana_eval,
                                       text="Ingrese el numero de puntos obtenidos en alineacion (1-10): ")
        etiqueta_alineacion.pack(pady=5)

        entrada_alineacion = tk.Entry(ventana_eval)
        entrada_alineacion.pack(pady=5)

        etiqueta_puntualidad = tk.Label(ventana_eval,
                                        text="Ingrese el numero de puntos obtenidos en puntualidad (1-10): ")
        etiqueta_puntualidad.pack(pady=5)

        entrada_puntualidad = tk.Entry(ventana_eval)
        entrada_puntualidad.pack(pady=5)

        etiqueta_banda = tk.Label(ventana_eval, text="Ingrese el nombre de la banda a evaluar: ")
        etiqueta_banda.pack(pady=5)

        entrada_banda = tk.Entry(ventana_eval)
        entrada_banda.pack(pady=5)

        def guardar_evaluacion():
            nombre_banda = entrada_banda.get()
            puntajes = {
                "ritmo": int(entrada_ritmo.get()),
                "uniformidad": int(entrada_uniformidad.get()),
                "coreografia": int(entrada_coreografia.get()),
                "alineacion": int(entrada_alineacion.get()),
                "puntualidad": int(entrada_puntualidad.get())
            }

            try:
                resultado = self.concurso.registrar_evaluacion(nombre_banda, puntajes)
                print(resultado)
                ventana_eval.destroy()
            except ValueError as e:
                print(f"Error: {e}")

        boton_registrar = tk.Button(ventana_eval, text="Registrar", command=guardar_evaluacion)
        boton_registrar.pack(pady=5)

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("400x300")

        etiqueta_listado = tk.Label(ventana_listado, text="Listado de Bandas")
        etiqueta_listado.pack(pady=5)

        # Mostrar bandas en la consola
        self.concurso.listar_bandas()

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("400x300")


if __name__ == "__main__":
    ConcursoBandasApp()
