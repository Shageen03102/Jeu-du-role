import matplotlib.pyplot as plt
import numpy as np

# Initialisation des coordonnées du point
point = [50, 50]  # Commencer au centre

# Initialisation de la figure et de l'axe
fig, ax = plt.subplots()
ax.plot(point[0], point[1], 'ro')  # Point rouge

# Fonction pour mettre à jour le point
def on_key(event):
    if event.key == 'up':
        point[1] -= 1
    elif event.key == 'down':
        point[1] += 1
    elif event.key == 'left':
        point[0] -= 1
    elif event.key == 'right':
        point[0] += 1
    
    ax.clear()  # Efface l'ancien point
    ax.plot(point[0], point[1], 'ro')  # Dessine le nouveau point
    plt.draw()  # Met à jour la figure
    plt.colorbar(label='Altitude')


# Connecte l'événement de la touche à la fonction on_key
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
 