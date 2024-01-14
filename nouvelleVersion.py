from pygame import *
from pickle import Pickler

font.init()
display.init()

PIXELS_X = 70
PIXELS_Y = 70
TAILLE_X = 7
TAILLE_Y = 7
hors_map = TAILLE_X * PIXELS_X

screen = display.set_mode((hors_map + 100, TAILLE_Y * PIXELS_Y))
lobj = ["fond", "mur", "porte"]

lobja = []
for nom in lobj:
    try:
        img = image.load("images/" + nom + ".JPG").convert_alpha()
        lobja.append(img)
    except Exception as e:
        print(f"Erreur lors du chargement de l'image {nom}: {e}")

def ecrire(txt, taille, posx, posy, couleur=(0, 0, 0)):
    display.get_surface().blit(font.Font(None, taille).render(txt, 1, couleur), (posx, posy))

def afficher():
    for y, ligne in enumerate(salle):
        for x, case in enumerate(ligne):
            display.get_surface().blit(lobja[case], (PIXELS_X,PIXELS_Y))
    # for i, r in enumerate(l_rect):
        # ecrire(lobj[i], 30, hors_map + 10, r[1], (255, 255, 255))
    display.flip()

def sauvegarder_carte(nom_fichier, carte):
    with open(nom_fichier, 'wb') as fichier:
        pickler = Pickler(fichier)
        pickler.dump(carte)

def charger_carte(nom_fichier):
    try:
        with open(nom_fichier, 'rb') as fichier:
            carte = Pickler.load(fichier)
            return carte
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas. Création d'une nouvelle carte.")
        return [[1] * TAILLE_X] + [[1] + [0] * (TAILLE_X - 2) + [1] for _ in range(TAILLE_Y - 2)] + [[1] * TAILLE_X]

print(3)
salle = charger_carte('carte_generée.pkl')
l_rect = [Rect(hors_map + 10, y, 90, 30) for y in range(100, len(lobj) * 30 + 100, 30)]
select = None
print(4)

afficher()

while True:
    ev = event.wait()
    if ev.type == QUIT or ev.type == KEYDOWN:
        sauvegarder_carte('carte_generée.pkl', salle)
        quit()
        break
    if ev.type == MOUSEBUTTONUP:
        if ev.pos[0] > hors_map or select is None:
            for i, r in enumerate(l_rect):
                if r.collidepoint(ev.pos):
                    select = i
        else:
            x, y = ev.pos[0] // PIXELS_X, ev.pos[1] // PIXELS_Y
            salle[y][x] = select
            display.get_surface().blit(lobja[select], (PIXELS_X * x, PIXELS_Y * y))
            display.update((PIXELS_X * x, PIXELS_Y * y, PIXELS_X, PIXELS_Y))