from pygame import *
from pickle import Pickler


font.init(); display.init()
name = input('nom de la salle\n')
PIXELS_X = 60
PIXELS_Y = 60
TAILLE_X = 7
TAILLE_Y = 5
hors_map = TAILLE_X * PIXELS_X
 
screen = display.set_mode((hors_map + 100, TAILLE_Y * PIXELS_Y))
lobj = ["fond", "mur", "porte"]

lobja = []
for nom in lobj:
    try:
        img = image.load("images/" + nom + ".png").convert_alpha()
        loaded_images.append(img)
    except Exception as e:
        print(f"Erreur lors du chargement de l'image {nom}: {e}")




print(3)

salle = [[1] * TAILLE_X] + [[1] + [0] * (TAILLE_X - 2) + [1] for i in range(TAILLE_Y - 2)] + [[1] * TAILLE_X]
l_rect = [Rect(hors_map + 10, y, 90, 30) for  y in range(100, len(lobj) * 30 + 100, 30)]
select = None
print(4)
 
def ecrire(txt, taille, posx, posy, couleur = (0, 0, 0)):
    display.get_surface().blit(font.Font (None, taille).render (txt, 1, couleur), (posx, posy))
# problemme ici
def afficher ():
    for y, ligne in enumerate(salle):
        for x, case in enumerate(ligne):
            display.get_surface().blit(lobja[case], (x * PIXELS_X, y * PIXELS_Y))
    for i, r in enumerate(l_rect):
        ecrire(lobj[i], 30, hors_map + 10, r[1], (255, 255, 255))
    display.flip()
 
print(1)
 
afficher()
print(2)

while 1:
    ev = event.wait()
    if ev.type == QUIT or ev.type == KEYDOWN:
        quit(); break
    if ev.type == MOUSEBUTTONUP:
        if ev.pos[0] > hors_map or select == None:
            for i, r in enumerate(l_rect):
                if r.collidepoint(ev.pos): select = i
        else:
            x, y = ev.pos[0] // PIXELS_X, ev.pos[1] // PIXELS_Y
            salle[y][x] = select
            display.get_surface().blit(lobja[select], (PIXELS_X * x, PIXELS_Y * y))
            display.update((PIXELS_X * x, PIXELS_Y * y, PIXELS_X, PIXELS_Y))

with open(name + ".txt", "a") as f:
    for i in salle: f.write(" ".join(map(str, i)) + "\n")