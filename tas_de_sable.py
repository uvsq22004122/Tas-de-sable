######################
# Import des modules #
######################
import tkinter as tk
import random as rd
from functools import partial

#############################
# Définition des constantes #
#############################
# hauteur du canevas
HEIGHT = 600
# largeur du canevas
WIDTH = 600
# taille de la grille en carreaux
N = 4
# taille des lignes de la grille
OFFSET_GRID = WIDTH / N

######################
# Variables globales #
######################
config_courante = []


#############
# Fonctions #
#############

def reset_affichage_grains(func):
    '''Permet de reset l'affichage du tas de sable et d'appeler les fonctions
    avec des décorateurs.'''
    def wrapper(*args, **kwargs):
        delete_affichage_tas_de_sable(*args, **kwargs)
        func(*args, **kwargs)
        affichage_tas_de_sable(*args, **kwargs)
    return wrapper


@reset_affichage_grains
def config_vide(racine, canvas):
    '''Initialise la configuration de tas de sable à 0.'''
    global config_courante
    config_courante = [[0] * N for _ in range(N)]
    print(f"0: {config_courante}")


@reset_affichage_grains
def config_aleatoire(racine, canvas):
    '''Génération d'une matrice de tas de sable de taille N.
    Ajout à la variable config_courante de la configuration aléatoire.'''
    global config_courante
    config_courante = [[rd.randint(0, 9)
                        for _ in range(N)] for _ in range(N)]
    print(f"avant: {config_courante}")


@reset_affichage_grains
def commencer_config_aleatoire(racine, canvas):
    '''Exécute les règles :
        - Si un élément de la grille >= 4 alors on le soustrait par 4
                et on ajoute 1 à tous ses voisins.'''
    global config_courante
    stable = False
    while not stable:
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
    # affection des fonctions avec des paramètres appliqués partiellement
    # dans des variables pour les utiliser quand un bouton est cliqué
    # (car les boutons prennent seulement des fonctions sans paramètres)
    config_vide_no_args = partial(config_vide, racine, canvas)
    config_aleatoire_no_args = partial(config_aleatoire, racine, canvas)
    commencer_config_aleatoire_no_args = partial(commencer_config_aleatoire,
                                                 racine, canvas)
    # création des boutons
    bouton_config_aleatoire = tk.Button(
        racine, text="Configuration aléatoire", command=config_aleatoire_no_args)
    bouton_commencer_config_aleatoire = tk.Button(
        racine, text="Commencer", command=commencer_config_aleatoire_no_args)
    bouton_quitter = tk.Button(racine, text='Quitter', command=racine.quit)
    bouton_effacer_tas_de_sable = tk.Button(
        racine, text='Effacer', command=config_vide_no_args)
    # placement des widgets
    canvas.grid(column=0, row=1)
    bouton_config_aleatoire.grid(row=0, column=1)
    bouton_commencer_config_aleatoire.grid(row=1, column=1)
    bouton_quitter.grid(row=2, ipadx=50)
    bouton_effacer_tas_de_sable.grid(row=2, column=1)


def generation_grille(canvas):
    '''Génération de la grille pour le tas de sable en fonction de N.'''
    for i in range(1, N):
        # ligne x0
        canvas.create_line((OFFSET_GRID * i, 0), (OFFSET_GRID * i, WIDTH))
        # ligne y0
        canvas.create_line((0, OFFSET_GRID * i), (HEIGHT, OFFSET_GRID * i))


def affichage_tas_de_sable(racine, canvas):
    '''Génération du contenu de config_courante dans la grille.'''
    global config_courante
    offset_insertion_x = OFFSET_GRID / 2
    offset_insertion_y = OFFSET_GRID / 2

    for i in range(N):
        for j, x in enumerate(config_courante[i]):
            canvas.create_text(offset_insertion_x,
                               offset_insertion_y, text=str(x), tags='grains')
            offset_insertion_x += OFFSET_GRID
        offset_insertion_x = OFFSET_GRID / 2
        offset_insertion_y += OFFSET_GRID


def delete_affichage_tas_de_sable(racine, canvas):
    '''Efface les grains du tas de sable dans la grille.'''
    canvas.delete('grains')


def main():

    racine = tk.Tk()
    racine.title("Génération tas de sables")
    canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
    config_vide(racine, canvas)
    generation_grille(canvas)
    affichage_widget(racine, canvas)

    racine.mainloop()


if __name__ == '__main__':
    main()
