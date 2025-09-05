import tkinter as tk

def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")

    etiqueta_inscribir = tk.Label(ventana_inscribir, text="Inscribir Banda")
    etiqueta_inscribir.pack(pady=5)

    etiqueta_nombre = tk.Label(ventana_inscribir, text="Ingrese el nombre de la banda: ")
    etiqueta_nombre.pack(pady=5)

    entrada_nombre = tk.Entry(ventana_inscribir)
    entrada_nombre.pack(pady=5)

    etiqueta_categoria = tk.Label(ventana_inscribir, text="Ingrese la categoria de la banda: ")
    etiqueta_categoria.pack(pady=5)

    entrada_categoria = tk.Entry(ventana_inscribir)
    entrada_categoria.pack(pady=5)

    boton_inscribir = tk.Button(ventana_inscribir, text="Inscribir Banda", command=inscribir_banda) #cambiar funcion
    boton_inscribir.pack(pady=5)


def registrar_evaluacion():
    print("Se abrió la ventana: Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x400")

    etiqueta_ritmo = tk.Label(ventana_eval, text="Ingrese numero de puntos obtenidos en ritmo (1-10): ")
    etiqueta_ritmo.pack(pady=5)

    entrada_ritmo = tk.Entry(ventana_eval)
    entrada_ritmo.pack(pady=5)

    etiqueta_uniformidad = tk.Label(ventana_eval, text="Ingerse el numero de puntos obtenidos en uniformidad (1-10): ")
    etiqueta_uniformidad.pack(pady=5)

    entrada_uniformidad = tk.Entry(ventana_eval)
    entrada_uniformidad.pack(pady=5)

    etiqueta_coreografia = tk.Label(ventana_eval, text="Ingerse el numero de puntos obtenidos en coreografia (1-10): ")
    etiqueta_coreografia.pack(pady=5)

    entrada_coreografia = tk.Entry(ventana_eval)
    entrada_coreografia.pack(pady=5)

    etiqueta_alineacion = tk.Label(ventana_eval, text="Ingerse el numero de puntos obtenidos en alineacion (1-10): ")
    etiqueta_alineacion.pack(pady=5)

    entrada_alineacion = tk.Entry(ventana_eval)
    entrada_alineacion.pack(pady=5)

    etiqueta_puntualidad = tk.Label(ventana_eval, text="Ingerse el numero de puntos obtenidos en puntualidad (1-10): ")
    etiqueta_puntualidad.pack(pady=5)

    entrada_puntualidad = tk.Entry(ventana_eval)
    entrada_puntualidad.pack(pady=5)

    boton_registrar = tk.Button(ventana_eval, text="Registrar", command=registrar_evaluacion) #cambiar funcioooon
    boton_registrar.pack(pady=5)


def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

    etiqueta_listado = tk.Label(ventana_listado, text="Listado de 	Bandas")
    etiqueta_listado.pack(pady=5)


def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()