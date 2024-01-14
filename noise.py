# //Créez le module de bruit (generator/noise.py)://

# generator/noise.py
import math

def fast_floor(x):
    return int(x) if x > 0 else int(x) - 1

def fast_dot(g, x, y):
    return g[0] * x + g[1] * y

def gradient(hash, x, y):
    h = hash & 15
    grad = 1 + (h & 7)  # Gradient value 1-8
    if h & 8:
        grad = -grad  # Randomly invert half of them
    return grad * x + grad * y

def noise2(x, y):
    # ... (Votre implémentation du bruit simplex pour 2D)
    pass

# //Créez le module de génération de carte (generator/map_generator.py)://

# generator/map_generator.py
from noise import noise2

def generate_world_map(width, height, scale):
    world_map = []

    for y in range(height):
        row = []
        for x in range(width):
            sample_x = x / scale
            sample_y = y / scale
            noise_value = noise2(sample_x, sample_y)
            row.append(noise_value)
        world_map.append(row)

    return world_map

# //Créez un fichier de test (tests/test_noise.py)//

# tests/test_noise.py


import unittest
# from generator.noise import noise2

class TestNoiseFunctions(unittest.TestCase):
    def test_noise2(self):
        # Test your noise2 function here
        pass

if __name__ == '__main__':
    unittest.main()