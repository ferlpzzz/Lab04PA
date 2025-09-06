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
            raise ValueError(f"Debe proporcionar puntajes para todos los criterios")

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
        info_base = super().mostrar_info()
        if self.fue_evaluada():
            return f"{info_base} - Puntaje: {self.total}"
        return f"{info_base} ({self.categoria}) - SIN EVALUAR"

class Concurso:
    def __init__(self, nombre_concurso, fecha):
        self.nombre_concurso = nombre_concurso
        self.fecha = fecha
        self.bandas = {}

    def inscribir_banda(self, banda):
        if banda.nombre in self.bandas:
            raise ValueError(f"Ya existe una banda con el nombre '{banda.nombre}'")
        self.bandas[banda.nombre] = banda
        return f"Banda '{banda.nombre}' inscrita exitosamente"

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError(f"No existe una banda con el nombre '{nombre_banda}'")
        banda = self.bandas[nombre_banda]
        banda.registrar_puntajes(puntajes)
        return f"Puntajes registrados para la banda '{nombre_banda}'"

    def listar_bandas(self):
        if not self.bandas:
            print("Aun no hay bandas inscritas")
            return
        print(f"\n--- LISTADO DE BANDAS - {self.nombre_concurso} ---")
        for nombre, banda in self.bandas.items():
            info = banda.mostrar_info()
            if banda.fue_evaluada():
                print(f"{info}")
                for criterio, puntaje in banda.puntajes.items():
                    print(f"{criterio.capitalize()}: {puntaje}")
            else:
                print(f"{info} (Sin evaluar)")
            print()

    def comparar(self, banda1, banda2):
        if banda1.total > banda2.total:
            return -1
        elif banda1.total < banda2.total:
            return 1
        if banda1.puntajes["ritmo"] > banda2.puntajes["ritmo"]:
            return -1
        elif banda1.puntajes["ritmo"] < banda2.puntajes["ritmo"]:
            return 1
        if banda1.puntajes["uniformidad"] > banda2.puntajes["uniformidad"]:
            return -1
        elif banda1.puntajes["uniformidad"] < banda2.puntajes["uniformidad"]:
            return 1
        if banda1.puntajes["coreografia"] > banda2.puntajes["coreografia"]:
            return -1
        elif banda1.puntajes["coreografia"] < banda2.puntajes["coreografia"]:
            return 1
        if banda1.puntajes["alineacion"] > banda2.puntajes["alineacion"]:
            return -1
        elif banda1.puntajes["alineacion"] < banda2.puntajes["alineacion"]:
            return 1
        if banda1.puntajes["puntualidad"] > banda2.puntajes["puntualidad"]:
            return -1
        elif banda1.puntajes["puntualidad"] < banda2.puntajes["puntualidad"]:
            return 1
        return 0

    def rankear(self):
        bandas_evaluadas = []
        for banda in self.bandas.values():
            if banda.fue_evaluada():
                bandas_evaluadas.append(banda)
        if not bandas_evaluadas:
            return []
        n = len(bandas_evaluadas)
        for i in range(n):
            for j in range(0, n - i - 1):
                comparacion = self.comparar(bandas_evaluadas[j],
                                            bandas_evaluadas[j + 1])
                if comparacion > 0:
                    bandas_evaluadas[j], bandas_evaluadas[j + 1] = bandas_evaluadas[j + 1], bandas_evaluadas[j]
        return bandas_evaluadas

    def mostrar_ranking(self):
        ranking = self.rankear()
        if not ranking:
            print("No hay bandas evaluadas para generar ranking")
            return
        print(f"\n--- RANKING FINAL - {self.nombre_concurso} ---")
        for i, banda in enumerate(ranking, 1):
            print(f"{i}°. {banda.mostrar_info()}")

# ACA VOY A HACER EL CONCURSO SOLICITADO CON LA INFO QUE NOS DIERON.
concurso = Concurso("Concurso de Bandas - 15 de Septiembre", "2025-09-15")
try:
    banda1 = BandaEscolar("Liceo Xela", "Liceo Guatemala", "Básico")
    banda2 = BandaEscolar("Estrella Infantil", "Escuela La Esperanza", "Primaria")
    banda3 = BandaEscolar("Águilas del Occidente", "Colegio La Patria Occidente", "Diversificado")
    print(concurso.inscribir_banda(banda1))
    print(concurso.inscribir_banda(banda2))
    print(concurso.inscribir_banda(banda3))
    puntajes_banda1 = {
        "ritmo": 9,
        "uniformidad": 8,
        "coreografia": 7,
        "alineacion": 8,
        "puntualidad": 10
    }
    puntajes_banda2 = {
        "ritmo": 8,
        "uniformidad": 9,
        "coreografia": 8,
        "alineacion": 7,
        "puntualidad": 9
    }
    puntajes_banda3 = {
        "ritmo": 10,
        "uniformidad": 9,
        "coreografia": 9,
        "alineacion": 8,
        "puntualidad": 10
    }
    print(concurso.registrar_evaluacion("Liceo Xela", puntajes_banda1))
    print(concurso.registrar_evaluacion("Estrella Infantil", puntajes_banda2))
    print(concurso.registrar_evaluacion("Águilas del Occidente", puntajes_banda3))
    concurso.listar_bandas()
    concurso.mostrar_ranking()
except ValueError as e:
    print(f"Error: {e}")

import tkinter as tk
from tkinter import messagebox

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.concurso = Concurso("Concurso de Bandas - 15 de Septiembre", "2025-09-15")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 15 de Septiembre - Quetzaltenango",
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
        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x350")

        tk.Label(ventana_inscribir, text="Inscribir Banda", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(ventana_inscribir, text="Ingrese el nombre de la banda: ").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_inscribir, width=30)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_inscribir, text="Ingrese la institución: ").pack(pady=5)
        entrada_institucion = tk.Entry(ventana_inscribir, width=30)
        entrada_institucion.pack(pady=5)

        tk.Label(ventana_inscribir, text="Ingrese la categoría de la banda (Primaria, Básico, Diversificado): ").pack(
            pady=5)
        entrada_categoria = tk.Entry(ventana_inscribir, width=30)
        entrada_categoria.pack(pady=5)

        def guardar_banda():
            nombre = entrada_nombre.get().strip()
            institucion = entrada_institucion.get().strip()
            categoria = entrada_categoria.get().strip()

            try:
                banda = BandaEscolar(nombre, institucion, categoria)
                resultado = self.concurso.inscribir_banda(banda)
                messagebox.showinfo("Éxito", resultado)
                ventana_inscribir.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana_inscribir, text="Inscribir Banda", command=guardar_banda).pack(pady=15)

    def registrar_evaluacion(self):
        if not self.concurso.bandas:
            messagebox.showinfo("Información", "No hay bandas inscritas para evaluar")
            return

        ventana_eval = tk.Toplevel(self.ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("450x500")

        tk.Label(ventana_eval, text="Registrar Evaluación", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(ventana_eval, text="Seleccione la banda:").pack(pady=5)
        bandas_names = list(self.concurso.bandas.keys())
        selected_banda = tk.StringVar(ventana_eval)
        selected_banda.set(bandas_names[0] if bandas_names else "")
        opciones_banda = tk.OptionMenu(ventana_eval, selected_banda, *bandas_names)
        opciones_banda.pack(pady=5)

        criterios = BandaEscolar.CRITERIOS
        entries = {}

        for criterio in criterios:
            tk.Label(ventana_eval, text=f"Ingrese puntos para {criterio} (0-10):").pack(pady=2)
            entry = tk.Entry(ventana_eval, width=10)
            entry.pack(pady=2)
            entries[criterio] = entry

        def guardar_evaluacion():
            nombre_banda = selected_banda.get()
            puntajes = {}

            try:
                for criterio, entry in entries.items():
                    puntaje = int(entry.get())
                    if not (0 <= puntaje <= 10):
                        raise ValueError(f"Puntaje para {criterio} debe estar entre 0 y 10")
                    puntajes[criterio] = puntaje

                resultado = self.concurso.registrar_evaluacion(nombre_banda, puntajes)
                messagebox.showinfo("Éxito", resultado)
                ventana_eval.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana_eval, text="Registrar Evaluación", command=guardar_evaluacion).pack(pady=15)
