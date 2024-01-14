import io
import noise
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sqlite3

def generate_perlin_noise(width, height, scale):
    world = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            world[i][j] = noise.pnoise2(i/scale,
                                         j/scale,
                                         octaves=6,
                                         persistence=0.5,
                                         lacunarity=2.0,
                                         repeatx=1024,
                                         repeaty=1024,
                                         base=42)
    return world

# Database setup
conn = sqlite3.connect('perlin_noise.db')  # Change this to your actual database connection
cursor = conn.cursor()

# Fetch image data from the database
cursor.execute('SELECT value FROM perlin_noise')
values_from_database = cursor.fetchall()

# Reshape the 1D list back to a 2D array
width, height = 500, 500
world_from_database = np.array(values_from_database).reshape((width, height))

# Close the database connection
conn.close()

# Visualization code remains the same

plt.imshow(world_from_database, cmap='terrain', origin='upper')
plt.colorbar()

# Utilize io.BytesIO() for non-interactive environments
image_stream = io.BytesIO()
plt.savefig(image_stream, format='png')
plt.close()

# Display the image using PIL
image = Image.open(image_stream)
image.show()