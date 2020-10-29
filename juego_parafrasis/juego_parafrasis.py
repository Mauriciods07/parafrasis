import tkinter as tk
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image
from numpy import random
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

# Variables de la ventana
# Diccionario para acceder a los textos
#### Agregar longitud palabras sushi y texto
dict_textos = {"sushi":["ListaSushi", "sushi0", 212, 28, "Sushi"], "cocina":["ListaCocina", "cocina_molecular", 189, 21, "Cocina"], "tequila":["lista01", "Tequila", 197, 25, "Tequila"], "kebab":["lista02", "Kebab", 184, 25, "Kebab"], "ofrenda":["lista03", "ofrenda", 195, 25, "ofrendas mexicanas"], "vegana":["lista04", "vegana", 199, 25, "comida vegana"], "camotes":["lista05", "camotes", 202, 25,"carrito de camotes"]}
HEIGHT = 600
WIDTH = 800
text_file = 0
# Número de oraciones por juego
oraciones = 5 
# Acceder al texto predeterminado
topic = "cocina"
lista_texto = dict_textos[topic][0]
parafrasis_texto = dict_textos[topic][1]
num_rand = dict_textos[topic][2]
sentence_length = dict_textos[topic][3]

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
sushi = tk.PhotoImage(file='imagenes/sushi.png')
sushi = sushi.subsample(12)
cocina = tk.PhotoImage(file='imagenes/cocina.png')
cocina = cocina.subsample(15)
file_img = tk.PhotoImage(file='imagenes/file.png')
file_img = file_img.subsample(8)
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

# Función para que el usuario pueda guardar el archivo 
def save_file(texto):
	files = [('Documento de texto', '*.txt'), ('Todos los archivos', '*.*')]
	file_dir = asksaveasfile(filetypes=files, defaultextension=files, mode='w')

	if(file_dir):
		with open(file_dir.name, "w") as doc:
			for elemento in texto:
				doc.write(elemento)
				doc.write("\n")

# Función para obtener la calificación de la creación lit.
def calificacion_lista(oracion, palabras):
    """
    

    Parameters oracion, palabras
    ----------
    oracion : str
        DESCRIPTION. Oración introducida por el usuario y creada a partir de la lista de palabras
                     que proporciona el juego.
    palabras : list
        DESCRIPTION.Lista de palabras que proporciona el juego.

    Returns calificación del usuario.
    -------
    TYPE
        DESCRIPTION.Se cuenta el número de palabras de la lista empleadas en la oración por el 
                    usuario y se asigna una calificación de acuerdo a la formula 
                    #(palabras de la lista usadas en la oración)/#(palabras en la lista).

    """
    
    from stop_words import get_stop_words
    stw = get_stop_words('spanish')
    stemmer = SnowballStemmer('spanish')
    
    
    def sg(palabra):
        sp = [",", ".", ";", "!", "¡", ")", "(", ":", '"', '¿', '?', '»', '«', "'", " "]
        for i in palabra:
            if i in sp:
                palabra = palabra.replace(i, "")
        return palabra

    t0 = []
    for p in oracion.split():
        t0.append(sg(p).lower())
        
    t0 = set(t0)
    t0 = list(t0)
    
    t1 = []
    for p in t0:
        if p not in stw:
            p = stemmer.stem(p)
            t1.append(p)
    
    c1 = set(t1) 
    c2 = []
    for p in palabras:
        c2.append(stemmer.stem(p))
    c2 = set(c2)

    c = c1 & c2
    
    c = len(c)
    c2 = len(c2)
    return c/c2

# función para dar la calificación de la paráfrasis baja
def calificacion_oracion(oracion, usuario):
    """

    Parameters: oracion, usuario. 
    ----------
    oracion : str
        DESCRIPTION.Oración que proporciona el juego. 
    usuario : str
        DESCRIPTION.Oración que introduce el usuario.

    Returns. Calificación del ususario.
    -------
    TYPE
        DESCRIPTION.Dependiendo del número de palabras que coincidan entre la oración que proporciona
        el juego y la oración que el usuario introduce se asigna una calificación de acuerdo a la 
        fórmula 1 - #(palabras que cooinciden)/#(total de palabras en la oración dada por el juego).

    """
    from stop_words import get_stop_words
    stw = get_stop_words('spanish')
    
    def sg(palabra):
        sp = [",", ".", ";", "!", "¡", ")", "(", ":", '"', '¿', '?', '»', '«', "'", " ", "-"]
        for i in palabra:
            if i in sp:
                palabra = palabra.replace(i, "")
        return palabra
    
    t0 = []
    for p in oracion.split():
        t0.append(sg(p).lower())
    t0 = list(set(t0)) 
    t_o = []
    for p in t0:
        if p not in stw:
            t_o.append(p)
                    
    t1 = []
    for p in usuario.split():
        t1.append(sg(p).lower())
    t1 = list(set(t1))
    t_u = []
    for p in t1:
        if p not in stw:
            t_u.append(p)
            
    c = set(t_o) & set(t_u)
    total = len(t_o)
    
    return round(1 - len(c)/total, 2)

# Función para elegir un texto para el juego
def elegirTexto(opcion):
	global lista_texto
	global parafrasis_texto
	global num_rand
	global sentence_length

	if(opcion == 0):
		topic = "cocina"
	elif(opcion == 1):
		topic = "sushi"
	elif(opcion == 2):
		topic = "tequila"
	elif(opcion == 3):
		topic = "kebab"
	elif(opcion == 4):
		topic = "ofrenda"
	elif(opcion == 5):
		topic = "vegana"
	elif(opcion == 6):
		topic = "camotes"

	lista_texto = dict_textos[topic][0]
	parafrasis_texto = dict_textos[topic][1]
	num_rand = dict_textos[topic][2]
	sentence_length = dict_textos[topic][3]

# Función para borrar la pantalla de resultados y regresar a la pantalla principal
def back_main():
	global label_results
	global label_results1
	global label_img
	global label_save
	global back_button
	global save_button

	label_results.place_forget()
	label_results1.place_forget()
	label_img.place_forget()
	back_button.place_forget()
	save_button.place_forget()
	label_save.place_forget()

	main_title()

# Función para mostrar el resultado del quizz
def results(counter, text_list):
	global text_file
	global label_results
	global label_results1
	global label_img
	global label_save
	global img_list
	global back_button
	global save_button

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
	label_save = tk.Label(frame, text="Guardar", bg='white', font=('Arial',12,'bold'))
	label_img = tk.Label(frame, image=img_list[img])
	back_button = tk.Button(frame, text="Regresar", bg="#412fe0", fg='white', command=back_main)
	save_button = tk.Button(frame, image=file_img, bg='white', command=lambda: save_file(text_list))
	# Colocar los resultados
	label_results.place(relx=0.3,y=100)
	label_results1.place(relx=0.2, y=150)
	label_save.place(relx=0.55, y=360)
	back_button.place(relx=0.6, rely=0.7, relheight=0.07, relwidth=0.2)
	label_img.place(relx=0.05, rely=0.35)
	save_button.place(relx=0.7, rely=0.82, relheight=0.08, relwidth=0.08)

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
	global lista_muestra

	stemmer = SnowballStemmer('spanish')

	if label == 1:
		# reiniciar el contador y la lista de oraciones
		counter = 0
		text_list = []
		word_list = []
		lista_muestra = []
		# Borrar las instrucciones
		instructions_label.place_forget()
		instructions_label2.place_forget()
		instructions_label.place_forget()
		instructions_label2.place_forget()
		start_button.place_forget()

		with open("textos/" + lista_texto + ".txt", "r", encoding='utf8') as doc:
			lista = doc.read()
			lista = lista.split() #len = 190

	else:
		# Calcular las palabras usadas en la caja de texto anterior
		word_counter = entry.get()
		counter += calificacion_lista(word_counter, lista_muestra)
		text_list.append(word_counter)

		lista_muestra = []

		# Borrar la lista anterior para poner la nueva
		list_label.grid_forget()
		list_label0.grid_forget()
		list_label1.grid_forget()
		list_label2.grid_forget()
		list_label3.grid_forget()
		list_label4.grid_forget()
		list_label5.grid_forget()
		list_label6.grid_forget()
		list_label10.grid_forget()
		quizz_img_label.grid_forget()
		count_label.grid_forget()
		entry.grid_forget()
		next_button.grid_forget()
	# Habrán diez preguntas distintas antes de terminar el juego
	if number < oraciones:
		val = 0

		# En las tres primeras partes, se toman palabras al azar del total de la lista
		if number < 3:
			# Crear lista de palabras provicional
			for elemento in range(8):
				# Elegir una palabra al azar
				word = lista[random.randint(num_rand)]
				# Si la palabra ya se encuentra en la misma lista, se elige otra palabra
				if word in lista_muestra:
					while word in lista_muestra:
						word = lista[random.randint(num_rand)]
				lista_muestra.append(word)
		# En las dos últimas rondas, se muestran palabras de una misma oración en cada una
		else:
			with open("textos/" + parafrasis_texto + ".txt", "r", encoding='utf8') as doc:
					paraphrasis_text = doc.read()
					paraphrasis_text = paraphrasis_text.split("\n")

			# Elegir una oración al azar
			sentence = paraphrasis_text[random.randint(sentence_length)]
			sentence = sentence.split()

			for word in sentence:
				for elemento in lista:
					if len(word) > 3:
						word = stemmer.stem(word)
						if word in elemento:
							if elemento not in lista_muestra:
								lista_muestra.append(elemento)	

			# Llenar la lista en caso de que no hubiera 10 palabras en la oración
			if(len(lista_muestra) < 8):
				while(len(lista_muestra) < 8):
					word = lista[random.randint(num_rand)]
					if word in lista_muestra:
						while word in lista_muestra:
							word = lista[random.randint(num_rand)]
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
		list_label10 = tk.Label(frame, text='Tu oración:', bg='white', font=('Arial', 12, 'bold'), justify='left')
		quizz_img_label = tk.Label(frame, image=quizz_img[val])
		count_label = tk.Label(frame, text=str(number + 1) + " de " + str(oraciones), bg='white', font=('Arial', 12, 'bold'), justify='right')
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
		quizz_img_label.grid(row=7, column=1, columnspan=5, rowspan=10,padx=40)
		count_label.grid(row=0, column=2)
		entry.grid(row=1, column=1, columnspan=2, padx=50, rowspan=2, ipadx=180, ipady=10)
		next_button.grid(row=3, column=2, ipadx=20, ipady=0.2)
	else:
		with open('NoParafrasis' + str(text_file) + '.txt', 'w') as doc:
			for elemento in text_list:
				doc.write(elemento)
				doc.write('\n')

		results(counter*30, text_list)

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
	global final_sentence

	lista_muestra = []

	if label == 1:
		# reiniciar el contador y la lista de oraciones
		counter = 0
		sentence = random.randint(sentence_length//2)
		text_list = []
		lista2 = []
		# Borrar las instrucciones
		instructions_label.place_forget()
		instructions_label2.place_forget()
		instructions_label.place_forget()
		instructions_label2.place_forget()
		start_button.place_forget()

		with open("textos/" + parafrasis_texto + ".txt", "r", encoding='utf8') as doc:
			lista = doc.read()
			lista = lista.split('\n') #len = 21
			for elemento in lista:
				strings = elemento.split()
				for string in strings:
					lista2.append(string.lower())

	else:
		# Calcular las palabras usadas en la caja de texto anterior
		word_counter = entry.get()
		counter += calificacion_oracion(final_sentence, word_counter)
		text_list.append(word_counter)

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
	if number < oraciones:
		# Valor para elegir una imagen al azar
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

		final_sentence = sentence1 + sentence2 + sentence3 + sentence4

		# Crear las etiquetas del juego
		sentence_label = tk.Label(frame, text="Oración original: ", bg='white', font=('Arial', 20, 'bold'))
		sentence_label0 = tk.Label(frame, text=sentence1, bg='white', font=('Arial', 12))
		sentence_label1 = tk.Label(frame, text=sentence2, bg='white', font=('Arial', 12))
		sentence_label2 = tk.Label(frame, text=sentence3, bg='white', font=('Arial', 12))
		sentence_label3 = tk.Label(frame, text=sentence4, bg='white', font=('Arial', 12))
		sentence_label4 = tk.Label(frame, text='Tu oración:', bg='white', font=('Arial', 20, 'bold'), anchor='e')
		quizz_img_label = tk.Label(frame, image=quizz_img[val])
		count_label = tk.Label(frame, text=str(number + 1) + " de " + str(oraciones), bg='white', font=('Arial', 20, 'bold'), justify='right')
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
		results(counter*20, text_list)


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
	global lists_label
	global boton_facil
	global boton_medio
	global boton_regresar
	global instructions_text
	global instructions_text2
	global boton_sushi
	global boton_cocina
	global boton_tequila
	global boton_kebab
	global boton_ofrenda
	global boton_vegana
	global boton_camotes
	# Borrar la pantalla principal
	main_label.place_forget()
	main_label2.place_forget()
	dificulty_label.place_forget()
	feather_label.place_forget()
	letters_label.place_forget()
	lists_label.place_forget()
	boton_facil.place_forget()
	boton_medio.place_forget()
	boton_sushi.place_forget()
	boton_cocina.place_forget()
	boton_tequila.place_forget()
	boton_kebab.place_forget()
	boton_ofrenda.place_forget()
	boton_vegana.place_forget()
	boton_camotes.place_forget()

	# Etiquetas para las instrucciones
	# Instrucciones para el nivel fácil
	if nivel == 1:
		instructions_text = """
			En cada pregunta, se desplegará una lista de palabras.
			Forma oraciones coherentes con la mayor cantidad de palabras 
			que se encuentre en la lista.
			Puedes flexionar las palabras y conjugar los verbos:
				Por ejemplo, si sale 'sol', puedes usar 'soles'.
			¡Mientras más palabras uses, demostrarás un mejor dominio de 
			la lengua!
		"""
	# Instrucciones para el nivel medio
	else:
		instructions_text = """
			En cada pregunta, se mostrará una oración.
			Haz todos los cambios que se te ocurran; emplea sinónimos,
			cambia de posición los elementos, usa nuevas palabras,
			pero no cambies la idea general del texto.
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
	global lists_label
	global boton_facil
	global boton_medio
	global boton_regresar
	global boton_sushi
	global boton_cocina
	global boton_tequila
	global boton_kebab
	global boton_ofrenda
	global boton_vegana
	global boton_camotes

	try:
		# Borrar el botón de regresar
		boton_regresar.place_forget()
	except:
		pass

	# Crear etiquetas del menú principal
	main_text = "¿Qué tan bueno eres con las palabras?"
	main_text2 = "¿Crees que tienes un amplio vocabulario? ¡Descúbrelo ahora!"
	dificulty_text = "Escoge una dificultad:"
	lists_text = "Listas:"
	main_label = tk.Label(frame, text=main_text, bg="white", font=('Arial', 25))
	main_label2 = tk.Label(frame, text=main_text2, bg="white", font=('Arial', 12))
	dificulty_label = tk.Label(frame, text=dificulty_text, bg="white", font=('Arial', 12))
	feather_label = tk.Label(frame, image=feather_img)
	letters_label = tk.Label(frame, image=letters_img)
	lists_label = tk.Label(frame, text=lists_text, bg="white", font=('Arial', 12, 'bold'))
	# Colocar las etiquetas
	main_label.place(x=25, y=30)
	main_label2.place(x=90, y=75)
	dificulty_label.place(x=225, y=110)
	feather_label.place(relx=0.2, rely=0.4)
	letters_label.place(relx=0.2, rely=0.6)
	lists_label.place(relx=0.01, rely=0.835)

	# Crear botones del menú principal
	boton_facil = tk.Button(frame, text='Creatividad', bg='#412fe0', fg='white', font=12, command=lambda: delete_main_label(1))
	boton_medio = tk.Button(frame, text='Paráfrasis', bg='#412fe0', fg='white', font=12, command=lambda: delete_main_label(2))
	boton_sushi = tk.Button(frame, image=sushi, bg='white', command=lambda: elegirTexto(0))
	boton_cocina = tk.Button(frame, image=cocina, bg='white', command=lambda: elegirTexto(1))
	boton_tequila = tk.Button(frame, text="01" , bg='white', command=lambda: elegirTexto(2))
	boton_kebab = tk.Button(frame, text="02" , bg='white', command=lambda: elegirTexto(3))
	boton_ofrenda = tk.Button(frame, text="03" , bg='white', command=lambda: elegirTexto(4))
	boton_vegana = tk.Button(frame, text="04" , bg='white', command=lambda: elegirTexto(5))
	boton_camotes = tk.Button(frame, text="05" , bg='white', command=lambda: elegirTexto(6))
	# Colocar botones del menú principal
	boton_facil.place(relx=0.4, rely=0.48, relheight=0.07, relwidth=0.2)
	boton_medio.place(relx=0.4, rely=0.68, relheight=0.07, relwidth=0.2)
	boton_sushi.place(relx=0.9, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_cocina.place(relx=0.81, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_tequila.place(relx=0.01, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_kebab.place(relx=0.1, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_ofrenda.place(relx=0.19, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_vegana.place(relx=0.28, rely=0.9, relheight=0.08, relwidth=0.08)
	boton_camotes.place(relx=0.37, rely=0.9, relheight=0.08, relwidth=0.08)


if __name__ == "__main__":
	main_title()

raiz.mainloop()