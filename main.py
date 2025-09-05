class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion
    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"
class BandaEscolar(Participante):
    CATEGORIAS_VALIDAS = ["Primaria", "Básico", "Diversificado"]
    CRITERIOS  = ["ritmo", "uniformidad", "coreografia", "alineacion", "puntualidad"]

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
            print("No hay bandas inscritas")
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





