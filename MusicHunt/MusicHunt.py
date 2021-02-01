#-----------------------------------------------
# Nombre:      Music Hunt
# Basado en:   Duck Hunt - Clasico de NES

# Autoras:     Karla Arias
#              Michelle Arias
#              Katherine Criollo
#-----------------------------------------------

import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

negro= (0, 0, 0) #Color Negro
blanco= (255, 255, 255) #Color Blanco

# Tamano de la Pantalla y Lugar de Aparicion
screen= pygame.display.set_mode((890, 550), 0, 32) 

# Titulo de la Ventana
pygame.display.set_caption("Music Hunt")

# Coordenadas del Mouse
x_pos= 0
y_pos= 0

# Coordenadas del Clic
x_clic= 0
y_clic= 0

# Coordanadas de la Nota Musical
x_nota= 0
y_nota= randint(0, 500)

puntaje= 0
velocidad= 1
perder= False

# Pixeles del Area de Juego
pygame.mixer.init(44100, -16, 2, 1024)

# Musica
pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
pygame.mixer.music.load("guitarra.mp3") #Carga de mp3 sonido de fondo
pygame.mixer.music.play(-1, 0.0) #Bucle infinito de reproduccion del sonido, se detiene al momento de un evento


while True:
	for event in pygame.event.get():
		if event.type== QUIT:
			exit() #Cierra la ventana si se presiona el boton salir
		elif event.type == MOUSEMOTION: 
			x_pos, y_pos= pygame.mouse.get_pos() #Deteccion de la posicion en pantalla del mouse
		elif event.type == MOUSEBUTTONDOWN:
			x_clic, y_clic= pygame.mouse.get_pos() #Deteccion del clic en pantalla

	posicion= (x_pos - 50, y_pos - 50) #Posicion de la nota musical

	x_nota += 1 #Movimiento en x
	y_nota += 1 #MOvimiento en y

	if x_nota * velocidad > 890 and not perder: 
		x_nota= 0 
		y_nota= randint(0, 500)
		if y_nota > 400 or y_nota < 0:
			y_nota = y_nota * -1 #Movimiento randomico en y
		if x_nota > 600 or x_nota < 0:
			x_nota = x_nota * -1 #Movimiento randomico en x

		# Game Over
		pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
		pygame.mixer.music.load("burla.mp3") #Carga de mp3 sonido de gameover
		pygame.mixer.music.play() #Ejecucion al momento de evento
		perder= True #Se ejecuta cuando se pierde el juego

	# Fondo Negro
	screen.fill(negro) #Llenar el fondo de color negro
	pygame.mouse.set_visible(False) #Curso del mouse invisible

	# Fondo de Pantalla
	screen.blit(pygame.image.load("fondo.png"), (0, 0)) #Carga de imagen de fondo en coordenada 0,0 para que este centrada en la pantalla de juego
	screen.blit(pygame.image.load("musica.png"), (0,0)) #Carga del titulo del juego 

	screen.blit(pygame.font.SysFont("tahoma", 30).render("Puntacion: " + str(puntaje), True, blanco), (650, 500)) #Puntaje mostrado en pantalla con el fondo blanco

	# Puntaje
	if x_clic in range(x_nota * velocidad - 30, x_nota * velocidad + 30) and y_clic in range(y_nota - 30, y_nota + 30):

		puntaje += 5 #Aumento del puntaje +5
		velocidad += 1 #Aumento de la velocidad
		x_nota= 0
		y_nota= randint(50, 500)

	screen.blit(pygame.image.load("nota.png"), (x_nota * velocidad, y_nota)) #Carga de la nota musical y movimiento

	if puntaje== 50: #Condicion para entrar al Bonus Time 1
		screen.fill(negro) #Volvemos a llenar la pantalla de negro para cargar una nueva imagen momentanea
		pygame.mouse.set_visible(False) #Ocultamos el cursor

		screen.blit(pygame.image.load("fondo2.png"), (0, 0)) #Carga de la imagen Bonus 1
		screen.blit(pygame.font.SysFont("tahoma", 30).render("Puntacion " + str(puntaje), True, blanco), (700, 500)) #Continuamos con el aumnento del puntaje
		screen.blit(pygame.font.SysFont("tahoma", 40).render("Bonus Time 1", True, blanco), (20, 0)) #Titulo del Bonus

		screen.blit(pygame.image.load("musical.png"), (x_nota * velocidad, y_nota)) #Carga de nota musical especial de Bonus

	if puntaje== 100: #COndicion para entrar al Bonus Time 2
		screen.fill(negro) #Volvemos a llenar la pantalla de negro para cargar una nueva imagen momentanea
		pygame.mouse.set_visible(False) #Ocultamos el cursor

		screen.blit(pygame.image.load("fondo3.png"), (0, 0)) #Carga de imagen Bonus 2
		screen.blit(pygame.font.SysFont("tahoma", 30).render("Puntacion " + str(puntaje), True, blanco), (700, 500)) #Continuamos con el aumnento del puntaje
		screen.blit(pygame.font.SysFont("tahoma", 40).render("Bonus Time 2", True, blanco), (20, 0)) #Titulo del Bonus

		screen.blit(pygame.image.load("play.png"), (x_nota * velocidad, y_nota)) #Carga de nota musical especial de Bonus

	if perder: 
		x_nota = -50 #Cuando en x sale de la pantalla
		y_nota = -50 #Cuando en y sale de la pantalla
		screen.blit(pygame.image.load("burla.png"), (400, 340)) #Cargamos la imagen de burla
		screen.blit(pygame.image.load("gameover.png"), (150, 340)) #Cargamso la imagen de game over


	screen.blit(pygame.image.load("mira.gif").convert(), posicion) #Cargamos la mira que colisionara con las notas musicales, esta se carga con la imagen base para que dure durante todo el programa

	pygame.display.update() #Actualizacion de pantalla en funcion de bytes

