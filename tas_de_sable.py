######################
# Import des modules #
######################
import tkinter as tk
import random as rd

#############################
# Définition des constantes #
#############################
# hauteur du canevas 
HAUTEUR = 600
# largeur du canevas 
LARGEUR = 600
# taille de la grille
N = 3


#############
# Fonctions #
#############
def config_aleatoire():
	pass	


#######################
# Programme principal #
#######################

def affichage():
	racine = tk.Tk()
	racine.title("Génération tas de sables")
	canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="white")

	bouton_config_aleatoire = tk.Button(racine, text="Configuration aléatoire", command=config_aleatoire)

	a, u = 0, 0
	while a != 16 :
		canvas.create_line(37.5 + u, 0, 37.5 +u, 600)
		canvas.create_line(0,37.5+u, 600,37.5+u)
		u += 37.5
		a+=1


	# placement des widgets
	canvas.grid(column=0, row=1)
	bouton_config_aleatoire.grid(row=0)

	racine.mainloop()


def main():
	'''Génération de la grille de taille N.
		Applique la règle : 
			Si un élément de la grille >= 4 alors on le soustrait par 4 et on ajoute 1 à tous ses voisins.'''

	config_courante = []
	# affichage()

	for i in range(N):
		row = []
		for j in range(N):
			row.append(rd.randint(0,9))
		config_courante.append(row)
	print(f"avant: {config_courante}")
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

if __name__ == '__main__':
	main()
