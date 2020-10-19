import tkinter as tk
from PIL import ImageTk, Image
from numpy import random
from nltk.stem import WordNetLemmatizer

# Variables de la ventana
HEIGHT = 600
WIDTH = 800
text_file = 0

raiz = tk.Tk()
raiz.title("Corpus Paráfrasis")
#raiz.configure(background="white") ### Revisar

# Crear la ventana
canvas = tk.Canvas(raiz, height=HEIGHT, width=WIDTH)
canvas.pack()

# Cargar las imágenes del menú
feather_img = tk.PhotoImage(file='imagenes/feather(original)1.png')
feather_img = feather_img.subsample(23)
letters_img = tk.PhotoImage(file='imagenes/letters.png')
letters_img = letters_img.subsample(3)
# Cargar las imágenes de las preguntas
img1 = tk.PhotoImage(file='imagenes/01.png')
img2 = tk.PhotoImage(file='imagenes/02.png')
img3 = tk.PhotoImage(file='imagenes/03.png')
img4 = tk.PhotoImage(file='imagenes/04.png')
img5 = tk.PhotoImage(file='imagenes/05.png')
img6 = tk.PhotoImage(file='imagenes/06.png')
img7 = tk.PhotoImage(file='imagenes/07.png')
img8 = tk.PhotoImage(file='imagenes/08.png')
img9 = tk.PhotoImage(file='imagenes/09.png')
img10 = tk.PhotoImage(file='imagenes/10.png')
quizz_img = [img1.subsample(3), img2.subsample(2), img3, img4.subsample(4), img5.subsample(3), img6.subsample(2), img7, img8, img9, img10.subsample(3)]
# Cargar las imágenes de los resultados
face00 = tk.PhotoImage(file='imagenes/face00.png')
face01 = tk.PhotoImage(file='imagenes/face01.png')
face02 = tk.PhotoImage(file='imagenes/face02.png')
face03 = tk.PhotoImage(file='imagenes/face03.png')
face04 = tk.PhotoImage(file='imagenes/face04.png')
img_list = [face00.subsample(2), face01.subsample(2), face02.subsample(2), face03.subsample(2), face04.subsample(2)]

# Crear un marco que contendrá las etiquetas, botones, etc.
frame = tk.Frame(raiz, bg='white', padx=50, pady=50)
frame.place(relx=0.05, rely=0.05, relheight=0.88, relwidth=0.9)

# Función para borrar la pantalla de resultados y regresar a la pantalla principal
def back_main():
	global label_results
	global label_results1
	global label_img
	global back_button

	label_results.place_forget()
	label_results1.place_forget()
	label_img.place_forget()
	back_button.place_forget()

	main_title()

# Función para mostrar el resultado del quizz
def results(counter):
	global text_file
	global label_results
	global label_results1
	global label_img
	global img_list
	global back_button

	# Variable para guardar en un documento diferente
	text_file += 1

	# Texto que se mostrará de acuerdo con el resultado
	if counter <= 10:
		text = """Tu dominio de la lengua es muy bajo o 
		probablemente te estás muriendo de sueño.
		A cualquiera le llega a pasar.
		¿Por qué no consigues una taza de café y
		lo intentas de nuevo?
		¡Posiblemente consigas una mejor puntuación! :D
		"""
		img = 0
		calif = 20
	elif counter > 10 and counter <= 45:
		text = """¡Eso es! Siguele echando ganas.
		Aún puedes obtener una mejor calificación,
		¿por qué no lo intentas de nuevo? :)
		"""
		img = 1
		calif = 40
	elif counter > 45 and counter <= 70:
		text = """¡Bien! Aunque puede ser todavía mejor.
	Tienes todo el ingenio a tu disposición,
	aún puedes hacer un mejor trabajo.
	¿Por qué no lo intentas de nuevo? :)
		"""
		img = 2
		calif = 60
	elif counter > 70 and counter < 100:
		text = """¡Muy bien! Tienes un dominio moderado de la lengua
	Si sigues estudiando y lees mucho, en poco tiempo
	podrás escribir y hablar de todo.
	¿Por qué no lo intentas de nuevo?
	¡Tal vez saques una calificación perfecta la próxima
	vez! :D
		"""
		img = 3
		calif = 80
	elif counter >= 100:
		text = """¡Excelente! Tienes un extenso vocabulario
	y dominas la lengua. Dominas las palabras
	al derecho y al revés. :)
			"""
		img = 4
		calif = 100

	# Crear las etiquetas de los resultados
	label_results = tk.Label(frame, text="Resultado:    " + str(calif) + " de 100", bg='white', font=('Arial',25,'bold'))
	label_results1 = tk.Label(frame, text=text, bg='white', font=('Arial',12,))
	label_img = tk.Label(frame, image=img_list[img])
	back_button = tk.Button(frame, text="Regresar", bg="#412fe0", fg='white', command=back_main)

	# Colocar los resultados
	label_results.place(relx=0.3,y=100)
	label_results1.place(relx=0.2, y=150)
	back_button.place(relx=0.6, rely=0.7, relheight=0.07, relwidth=0.2)
	label_img.place(relx=0.05, rely=0.35)


# Función para desplegar el juego de creación literaria
def creacion_lit(number, label):
	global instructions_label
	global instructions_label2
	global instructions_label
	global instructions_label2
	global list_label
	global list_label0
	global list_label1
	global list_label2
	global list_label3
	global list_label4
	global list_label5
	global list_label6
	global list_label7
	global list_label8
	global list_label9
	global list_label10
	global count_label
	global entry
	global next_button
	global start_button
	global boton_regresar
	global lista
	global counter
	global word_counter
	global text_list
	global word_list
	global text_file
	global quizz_img
	global quizz_img_label

	lista_muestra = []

	if label == 1:
		# reiniciar el contador y la lista de oraciones
		counter = 0
		text_list = []
		word_list = []
		# Crear el objeto para lematizar las palabras
		lemmatizer = WordNetLemmatizer()
		# Borrar las instrucciones
		instructions_label.place_forget()
		instructions_label2.place_forget()
		instructions_label.place_forget()
		instructions_label2.place_forget()
		start_button.place_forget()

		with open("textos/Lista01.txt", "r", encoding='utf8') as doc:
			lista = doc.read()
			lista = lista.split() #len = 190

	else:
		# Calcular las palabras usadas en la caja de texto anterior
		word_counter = entry.get()
		text_list.append(word_counter)
		for elemento in lista:
			if elemento.lower() in word_counter.lower():
				counter += 1
		# Borrar la lista anterior para poner la nueva
		list_label.grid_forget()
		list_label0.grid_forget()
		list_label1.grid_forget()
		list_label2.grid_forget()
		list_label3.grid_forget()
		list_label4.grid_forget()
		list_label5.grid_forget()
		list_label6.grid_forget()
		list_label7.grid_forget()
		list_label8.grid_forget()
		list_label9.grid_forget()
		list_label10.grid_forget()
		quizz_img_label.grid_forget()
		count_label.grid_forget()
		entry.grid_forget()
		next_button.grid_forget()
	# Habrán diez preguntas distintas antes de terminar el juego
	if number < 10:
		val = 0
		# Crear lista de palabras provicional
		for elemento in range(10):
			# Elegir una palabra al azar
			word = lista[random.randint(189)]
			# Si la palabra ya se encuentra en la misma lista, se elige otra palabra
			if word in lista_muestra:
				while word in lista_muestra:
					word = lista[random.randint(189)]
			lista_muestra.append(word)
			

		val = random.randint(10)

		# Crear etiquetas del juego, la entrada y el botón
		list_label = tk.Label(frame, text="Lista:", bg='white', font=('Arial', 12, 'bold'))
		list_label0 = tk.Label(frame, text=lista_muestra[0], bg='white', font=('Arial', 12))
		list_label1 = tk.Label(frame, text=lista_muestra[1], bg='white', font=('Arial', 12))
		list_label2 = tk.Label(frame, text=lista_muestra[2], bg='white', font=('Arial', 12))
		list_label3 = tk.Label(frame, text=lista_muestra[3], bg='white', font=('Arial', 12))
		list_label4 = tk.Label(frame, text=lista_muestra[4], bg='white', font=('Arial', 12))
		list_label5 = tk.Label(frame, text=lista_muestra[5], bg='white', font=('Arial', 12))
		list_label6 = tk.Label(frame, text=lista_muestra[6], bg='white', font=('Arial', 12))
		list_label7 = tk.Label(frame, text=lista_muestra[7], bg='white', font=('Arial', 12))
		list_label8 = tk.Label(frame, text=lista_muestra[8], bg='white', font=('Arial', 12))
		list_label9 = tk.Label(frame, text=lista_muestra[9], bg='white', font=('Arial', 12))
		list_label10 = tk.Label(frame, text='Tu oración:', bg='white', font=('Arial', 12, 'bold'), justify='left')
		quizz_img_label = tk.Label(frame, image=quizz_img[val])
		count_label = tk.Label(frame, text=str(number + 1) + " de 10", bg='white', font=('Arial', 12, 'bold'), justify='right')
		entry = tk.Entry(frame, bd=4)
		next_button = tk.Button(frame, text=">>", bg="#412fe0", fg='white', font=('Arial', 12, 'bold'), command=lambda: creacion_lit(number+1,0))
		# Colocar la lista y los demás elementos
		list_label.grid(row=0,column=0)
		list_label0.grid(row=1,column=0)
		list_label1.grid(row=2,column=0)
		list_label2.grid(row=3,column=0)
		list_label3.grid(row=4,column=0)
		list_label4.grid(row=5,column=0)
		list_label5.grid(row=6,column=0)
		list_label6.grid(row=7,column=0)
		list_label7.grid(row=8,column=0)
		list_label8.grid(row=9,column=0)
		list_label9.grid(row=10,column=0)
		list_label10.grid(row=0, column=1)
		quizz_img_label.grid(row=7, column=1, columnspan=5, rowspan=10,padx=40)
		count_label.grid(row=0, column=2)
		entry.grid(row=1, column=1, columnspan=2, padx=50, rowspan=2, ipadx=180, ipady=10)
		next_button.grid(row=3, column=2, ipadx=20, ipady=0.2)
	else:
		with open('NoParafrasis' + str(text_file) + '.txt', 'w') as doc:
			for elemento in text_list:
				doc.write(elemento)
				doc.write('\n')
		results(counter)

# Función para desplegar el juego de paráfrasis baja
def parafrasis_baja(number, label):	
	global instructions_label
	global instructions_label2
	global instructions_label
	global instructions_label2
	global sentence_label
	global sentence_label0
	global sentence_label1
	global sentence_label2
	global sentence_label3
	global sentence_label4
	global count_label
	global entry
	global next_button
	global start_button
	global boton_regresar
	global lista
	global lista2
	global counter
	global word_counter
	global text_list
	global text_file
	global quizz_img
	global quizz_img_label
	global sentence

	lista_muestra = []

	if label == 1:
		# reiniciar el contador y la lista de oraciones
		counter = 0
		sentence = random.randint(2)
		text_list = []
		lista2 = []
		# Borrar las instrucciones
		instructions_label.place_forget()
		instructions_label2.place_forget()
		instructions_label.place_forget()
		instructions_label2.place_forget()
		start_button.place_forget()

		with open("textos/cocina_molecular.txt", "r", encoding='utf8') as doc:
			lista = doc.read()
			lista = lista.split('\n') #len = 21
			for elemento in lista:
				strings = elemento.split()
				for string in strings:
					lista2.append(string.lower())

	else:
		# Calcular las palabras usadas en la caja de texto anterior
		word_counter = entry.get()
		text_list.append(word_counter)
		word_counter = word_counter.split()
		for elemento in word_counter:
			if elemento.lower() not in lista2:
				counter += 1
		# Borrar la lista anterior para poner la nueva
		sentence_label.place_forget()
		sentence_label0.place_forget()
		sentence_label1.place_forget()
		sentence_label2.place_forget()
		sentence_label3.place_forget()
		sentence_label4.place_forget()
		quizz_img_label.place_forget()
		count_label.place_forget()
		entry.place_forget()
		next_button.place_forget()
	# Habrán diez preguntas distintas antes de terminar el juego
	if number < 10:
		val = random.randint(10)
		# Crear etiquetas del juego, la entrada y el botón
		# Si la oración no cabe en la pantalla, hay que dividirla
		sentence1 = ''
		sentence2 = ''
		sentence3 = ''
		sentence4 = ''
		if len(lista[sentence]) > 90:
			sentence1 = lista[sentence][:86]
			if len(lista[sentence]) > 180:
				if len(lista[sentence]) > 270:
					sentence2 = lista[sentence][86:176]
					sentence3 = lista[sentence][176:266]
					sentence4 = lista[sentence][266:]
				else:
					sentence2 = lista[sentence][86:176]
					sentence3 = lista[sentence][176:]
			else:
				sentence2 = lista[sentence][86:]
		else:
			sentence1 = lista[sentence]

		# Crear las etiquetas del juego
		sentence_label = tk.Label(frame, text="Oración original: ", bg='white', font=('Arial', 20, 'bold'))
		sentence_label0 = tk.Label(frame, text=sentence1, bg='white', font=('Arial', 12))
		sentence_label1 = tk.Label(frame, text=sentence2, bg='white', font=('Arial', 12))
		sentence_label2 = tk.Label(frame, text=sentence3, bg='white', font=('Arial', 12))
		sentence_label3 = tk.Label(frame, text=sentence4, bg='white', font=('Arial', 12))
		sentence_label4 = tk.Label(frame, text='Tu oración:', bg='white', font=('Arial', 20, 'bold'), anchor='e')
		quizz_img_label = tk.Label(frame, image=quizz_img[val])
		count_label = tk.Label(frame, text=str(number + 1) + " de 10", bg='white', font=('Arial', 20, 'bold'), justify='right')
		entry = tk.Entry(frame, bd=4, font=('Arial', 11))
		next_button = tk.Button(frame, text=">>", bg="#412fe0", fg='white', font=('Arial', 12, 'bold'), command=lambda: parafrasis_baja(number+1,0))
		# Colocar la lista y los demás elementos
		sentence_label.place(relx=-0.07, rely=0.05)
		sentence_label0.place(relx=0, rely=0.14)
		sentence_label1.place(relx=0, rely=0.185)
		sentence_label2.place(relx=0, rely=0.23)
		sentence_label3.place(relx=0, rely=0.275)
		sentence_label4.place(relx=-0.07, rely=0.375)
		entry.place(relx=-0.07, rely=0.475, relwidth=1.1, relheight=0.09)
		next_button.place(relx=0.88, rely=0.585, relwidth=0.1, relheight=0.08)
		count_label.place(relx=0.7, rely=0.05)
		quizz_img_label.place(relx=0, rely=0.58)

		sentence += 2

	else:
		with open('ParafrasisBaja' + str(text_file) + '.txt', 'w') as doc:
			for elemento in text_list:
				doc.write(elemento)
				doc.write('\n')
		print(counter)
		results(counter)


def deploy_instructions(nivel):
	global instructions_label
	global instructions_label2
	global instructions_label
	global instructions_label2
	global start_button

	# Crear etiquetas para las instrucciones
	instructions_label = tk.Label(frame, text="Instrucciones:", bg='white', font=('Arial',25, 'bold'))
	instructions_label2 = tk.Label(frame, text=instructions_text, bg='white', font=('Arial', 12), justify='left')
	instructions_label.place(relx=0, rely=0.1)
	instructions_label2.place(relx=-0.1, rely=0.25)
	# Botón de inicio
	if nivel == 1:
		start_button = tk.Button(frame, text="Adelante", bg="#412fe0", fg='white', font=('Arial', 12), command=lambda: creacion_lit(0, 1))
	else:
		start_button = tk.Button(frame, text="Adelante", bg="#412fe0", fg='white', font=('Arial', 12), command=lambda: parafrasis_baja(0, 1))

	start_button.place(relx=0.4, rely=0.6, relheight=0.07, relwidth=0.2)


def delete_main_label(nivel):
	# Introducir las etiquetas y botones de la pantalla principal en la función
	global main_label
	global main_label2
	global dificulty_label
	global feather_label
	global letters_label
	global boton_facil
	global boton_medio
	global boton_regresar
	global instructions_text
	global instructions_text2
	# Borrar la pantalla principal
	main_label.place_forget()
	main_label2.place_forget()
	dificulty_label.place_forget()
	feather_label.place_forget()
	letters_label.place_forget()
	boton_facil.place_forget()
	boton_medio.place_forget()

	# Etiquetas para las instrucciones
	# Instrucciones para el nivel fácil
	if nivel == 1:
		instructions_text = """
			En cada pregunta, se desplegará una lista de palabras.
			Forma oraciones coherentes con la mayor cantidad de palabras 
			que se encuentre en la lista.
			¡Mientras más palabras uses, demostrarás un mejor dominio de 
			la lengua!
		"""
	# Instrucciones para el nivel medio
	else:
		instructions_text = """
			En cada pregunta, se mostrará una oración.
			Haz todos los cambios que se te ocurran; emplea sinónimos,
			cambia de posición los elementos, pero no cambies la idea general
			del texto.
			¡Mientras más elementos cambies y muevas, demostrarás un mejor 
			dominio de la lengua!
		"""

	deploy_instructions(nivel)

# Función para mostrar la pantalla principal
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
	boton_facil = tk.Button(frame, text='Fácil', bg='#412fe0', fg='white', font=12, command=lambda: delete_main_label(1))
	boton_medio = tk.Button(frame, text='Medio', bg='#412fe0', fg='white', font=12, command=lambda: delete_main_label(2))
	# Colocar botones del menú principal
	boton_facil.place(relx=0.4, rely=0.48, relheight=0.07, relwidth=0.2)
	boton_medio.place(relx=0.4, rely=0.68, relheight=0.07, relwidth=0.2)


main_title()

raiz.mainloop()