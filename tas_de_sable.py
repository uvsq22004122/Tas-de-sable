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

def main():

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

	def affichage():
		'''Interface tkinter : Créations et placement des widgets'''
		# création des boutons
		bouton_config_aleatoire = tk.Button(racine, text = "Configuration aléatoire", command = config_aleatoire)
		bouton_commencer_config_aleatoire = tk.Button(racine, text = "Commencer", command = commencer_config_aleatoire)
		bouton_quitter = tk.Button(racine, text = 'Quitter', command = racine.quit)
		# placement des widgets
		canvas.grid(column = 0, row = 1)
		bouton_config_aleatoire.grid(row = 0, column = 1)
		bouton_commencer_config_aleatoire.grid(row = 1, column = 1)
		bouton_quitter.grid(row = 2, ipadx= 50)
		
	def grille():
		'''Génération de la grille pour le tas de sable'''
		offset_grille = WIDTH / N
		for i in range(1, N):
			canvas.create_line((offset_grille * i, 0), (offset_grille * i, WIDTH))
			canvas.create_line((0, offset_grille * i), (HEIGHT, offset_grille * i))
	
	def insertion_tas_de_sables():
		'''blabla'''
		offset_insertion = ((WIDTH / 2) / N)
		for i in range(1, N):
			for j in range(1, N):
				canvas.create_oval(x = offset_insertion * j, y = offset_insertion * i)

	config_courante = []
	racine = tk.Tk()
	racine.title("Génération tas de sables")
	canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
	grille()
	insertion_tas_de_sables()
	affichage()
	racine.mainloop()

if __name__ == '__main__':
	main()
