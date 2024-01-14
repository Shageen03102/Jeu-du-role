
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import *
from scipy.ndimage.filters import gaussian_filter

# Paramètres pour la taille de la carte et l'échelle du bruit
largeur, hauteur = 100, 100
echelle = 20

# Générer un terrain aléatoire
terrain = np.random.rand(largeur, hauteur)
terrain = gaussian_filter(terrain, sigma=echelle)
print(terrain)

# Position du point à ajouter (par exemple au centre)

print('Entrer X : ')
point_x = input()
print('Entrer Y : ')
point_y = input()

# point_x, point_y = largeur // 2, hauteur // 2



# Visualiser le terrain
plt.figure(figsize=(10, 10))
plt.imshow(terrain, cmap='terrain')
plt.colorbar(label='Altitude')
plt.scatter(point_x, point_y, c='red', s=100)  # Ajout d'un point rouge pour marquer un emplacement
plt.title('Carte de Terrain Générée Proceduralement')
plt.show()  
