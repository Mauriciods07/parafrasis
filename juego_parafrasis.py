import tkinter as tk
from PIL import ImageTk, Image

# Variables de la ventana
HEIGHT = 600
WIDTH = 800
start = False

raiz = tk.Tk()
raiz.title("Paráfrasis baja")
#raiz.configure(background="white") ### Revisar

# Crear la ventana
canvas = tk.Canvas(raiz, height=HEIGHT, width=WIDTH)
canvas.pack()

# Cargar las imágenes
feather_img = tk.PhotoImage(file='feather(original)1.png')
feather_img = feather_img.subsample(23)
letters_img = tk.PhotoImage(file='letters.png')
letters_img = letters_img.subsample(3)

# Función para eliminar etiquetas
def delete_label():
	global instructions_label
	global instructions_label2
	global start_button
	global start

	instructions_label.place_forget()
	instructions_label2.place_forget()
	start_button.place_forget()
	start=True

# Función para desplegar el juego de creación literaria
def creacion_lit():
	# Introducir las etiquetas y botones de la pantalla principal en la función
	global main_label
	global main_label2
	global dificulty_label
	global feather_label
	global letters_label
	global boton_facil
	global boton_medio
	global boton_regresar
	global instructions_label
	global instructions_label2
	global start_button
	global start
	# Borrar la pantalla principal
	main_label.place_forget()
	main_label2.place_forget()
	dificulty_label.place_forget()
	feather_label.place_forget()
	letters_label.place_forget()
	boton_facil.place_forget()
	boton_medio.place_forget()

	# Etiquetas para las instrucciones
	instructions_text = "Instrucciones:"
	instructions_text2 = """
		En cada pregunta se desplegará una lista de palabras.
		Forma oraciones coherentes con la mayor cantidad de palabras 
		que se encuentre en la lista.
		¡Mientras más palabras uses, demostrarás un mejor dominio de la lengua!
	"""
	instructions_label = tk.Label(frame, text=instructions_text, bg='white', font=('Arial',25))
	instructions_label2 = tk.Label(frame, text=instructions_text2, bg='white', font=('Arial', 12), justify='left')
	instructions_label.place(relx=0, rely=0)
	instructions_label2.place(relx=-0.1, rely=0.25)
	# Botón de inicio
	start_button = tk.Button(frame, text="Adelante", bg="#412fe0", fg='white', font=('Arial', 12), command=delete_label)
	start_button.place(relx=0.4, rely=0.6, relheight=0.07, relwidth=0.2)

	if start:
		print("hola mundo")

	# Botón para regresar a la pantalla principal
	#boton_regresar = tk.Button(frame, text="click", comman=main_title)
	#boton_regresar.place(x=20,y=20)

# Función para desplegar el juego de paráfrasis baja
def parafrasis_baja():	
	# Introducir las etiquetas y botones de la pantalla principal en la función
	global main_label
	global main_label2
	global dificulty_label
	global feather_label
	global letters_label
	global boton_facil
	global boton_medio
	global boton_regresar
	global instructions_label
	global instructions_label2
	global start_button
	global start
	# Borrar la pantalla principal
	main_label.place_forget()
	main_label2.place_forget()
	dificulty_label.place_forget()
	feather_label.place_forget()
	letters_label.place_forget()
	boton_facil.place_forget()
	boton_medio.place_forget()

	# Botón para regresar a la pantalla principal
	boton_regresar = tk.Button(frame, text="click", comman=main_title)
	boton_regresar.place(x=20,y=20)

# Crear un marco que contendrá las etiquetas, botones, etc.
frame = tk.Frame(raiz, bg='white', padx=50, pady=50)
frame.place(relx=0.05, rely=0.05, relheight=0.88, relwidth=0.9)

def main_title():
	# Introducir las etiquetas y botones de la pantalla principal en la función
	global main_label
	global main_label2
	global dificulty_label
	global feather_label
	global letters_label
	global boton_facil
	global boton_medio
	global boton_regresar

	try:
		# Borrar el botón de regresar
		boton_regresar.place_forget()
	except:
		pass

	# Crear etiquetas del menú principal
	main_text = "¿Qué tan bueno eres con las palabras?"
	main_text2 = "¿Crees que tienes un amplio vocabulario? ¡Descúbrelo ahora!"
	dificulty_text = "Escoge una dificultad:"
	main_label = tk.Label(frame, text=main_text, bg="white", font=('Arial', 25))
	main_label2 = tk.Label(frame, text=main_text2, bg="white", font=('Arial', 12))
	dificulty_label = tk.Label(frame, text=dificulty_text, bg="white", font=('Arial', 12))
	feather_label = tk.Label(frame, image=feather_img)
	letters_label = tk.Label(frame, image=letters_img)
	# Colocar las etiquetas
	main_label.place(x=25, y=30)
	main_label2.place(x=90, y=75)
	dificulty_label.place(x=225, y=110)
	feather_label.place(relx=0.2, rely=0.4)
	letters_label.place(relx=0.2, rely=0.6)

	# Crear botones del menú principal
	boton_facil = tk.Button(frame, text='Fácil', bg='#412fe0', fg='white', font=12, command=creacion_lit)
	boton_medio = tk.Button(frame, text='Medio', bg='#412fe0', fg='white', font=12, command=parafrasis_baja)
	# Colocar botones del menú principal
	boton_facil.place(relx=0.4, rely=0.48, relheight=0.07, relwidth=0.2)
	boton_medio.place(relx=0.4, rely=0.68, relheight=0.07, relwidth=0.2)


main_title()

raiz.mainloop()