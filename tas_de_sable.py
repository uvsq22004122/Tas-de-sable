######################
# Import des modules #
######################
import tkinter as tk
import random as rd

#############################
# Définition des constantes #
#############################
# hauteur du canevas 
HEIGHT = 600
# largeur du canevas 
WIDTH = 600
# taille de la grille
N = 4


######################
# Variables globales #
######################
config_courante = []


#############
# Fonctions #
#############

def config_vide():
	'''Initialise la configuration de tas de sable à 0.'''
	for i in range(N):
		row = []
		for j in range(N):
			row.append(rd.randint(0,0))
		config_courante.append(row)
	print(f"0: {config_courante}")

def config_aleatoire():
	'''Génération d'une matrice de tas de sable de taille N.
		Ajout à la variable config_courante de la configuration aléatoire.'''
	for i in range(N):
		row = []
		for j in range(N):
			row.append(rd.randint(0,9))
		config_courante.append(row)
	print(f"avant: {config_courante}")

def commencer_config_aleatoire():
	'''Exécute les règles : 
		- Si un élément de la grille >= 4 alors on le soustrait par 4 et on ajoute 1 à tous ses voisins.'''
	stable = False
	while stable == False:
		stable = True
		for i in range(N):
			for j in range(N):
				if config_courante[i][j] >= 4:
					config_courante[i][j] -= 4
					stable = False
					if i + 1 < N:
						config_courante[i+1][j] += 1
					if i - 1 >= 0:
						config_courante[i-1][j] += 1
					if j + 1 < N:
						config_courante[i][j+1] += 1
					if j - 1 >= 0:
						config_courante[i][j-1] += 1
	print(f"apres: {config_courante}")

def affichage_widget(racine, canvas):
	'''Interface tkinter : créations et placement des widgets.'''
	# création des boutons
	bouton_config_aleatoire = tk.Button(racine, text = "Configuration aléatoire", command = config_aleatoire)
	bouton_commencer_config_aleatoire = tk.Button(racine, text = "Commencer", command = commencer_config_aleatoire)
	bouton_quitter = tk.Button(racine, text = 'Quitter', command = racine.quit)
	# placement des widgets
	canvas.grid(column = 0, row = 1)
	bouton_config_aleatoire.grid(row = 0, column = 1)
	bouton_commencer_config_aleatoire.grid(row = 1, column = 1)
	bouton_quitter.grid(row = 2, ipadx= 50)
	
def generation_grille(canvas):
	'''Génération de la grille pour le tas de sable en fonction de N.'''
	offset_grille = WIDTH / N
	for i in range(1, N):
    	#ligne x0
		canvas.create_line((offset_grille * i, 0), (offset_grille * i, WIDTH))
		#ligne y0
		canvas.create_line((0, offset_grille * i), (HEIGHT, offset_grille * i))

def affichage_tas_de_sable(racine, canvas):
	'''Génération du contenu de config_courante dans la grille.'''
	offset_insertion_x = ((WIDTH / 2) / N)
	offset_insertion_y = ((WIDTH / 2) / N) 
	offset_grille = WIDTH / N
	for i in range(N): 
		offset_insertion_y += (i * offset_grille)
		print(i)
		for j, x in enumerate(config_courante[i]):
			canvas.create_text(offset_insertion_x, offset_insertion_y, text = str(x))
			offset_insertion_x += offset_grille
		
			
		
			
def main():

	racine = tk.Tk()
	racine.title("Génération tas de sables")
	canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
	# config_vide()
	config_aleatoire()
	generation_grille(canvas)
	affichage_widget(racine, canvas)
	affichage_tas_de_sable(racine, canvas)
	racine.mainloop()

if __name__ == '__main__':
	main()
