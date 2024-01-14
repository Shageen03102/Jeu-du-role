import os

import pygame
from pygame.locals import *


class App:
    def __init__(self):
        self.running = True
        # Create map
        currentdir = os.path.dirname(os.path.realpath(__file__))
        imagedir = os.path.join(currentdir, 'images', 'mur.jpg')
        self.map = pygame.image.load(imagedir)
        self.original_map = self.map.copy()
        self.maprect = self.map.get_rect()

        # Set initial window size to be the same as the map size
        self.size = self.map.get_size()

        # Create window
        self.window = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)

        self.maprect.center = self.window.get_rect().center
        self.blitmap()

        # Variables for click and drag
        self.dragging = False
        self.drag_start = (0, 0)

        pygame.display.flip()

    def blitmap(self):
        self.mapsurface = pygame.transform.smoothscale(self.map, self.maprect.size)
        self.window.fill(0)
        self.window.blit(self.mapsurface, self.maprect)

    def on_init(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def check_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.VIDEORESIZE:
            self.window = pygame.display.set_mode(event.dict['size'], pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
            self.maprect = self.map.get_rect(center=self.window.get_rect().center)
            self.blitmap()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 or event.button == 5:
                mx, my = event.pos
                zoom = 1.1 if event.button == 4 else 0.9  # Adjust zoom factors as needed

                # Calculate new dimensions based on zoom
                new_width = int(self.maprect.width * zoom)
                new_height = int(self.maprect.height * zoom)

                # Ensure the map image does not become smaller than the original size
                if new_width >= self.original_map.get_width() and new_height >= self.original_map.get_height():
                    left = mx - (mx - self.maprect.left) * zoom
                    top = my - (my - self.maprect.top) * zoom
                    self.maprect = pygame.Rect(left, top, new_width, new_height)
                    self.blitmap()

            elif event.button == 1:  # Left mouse button for click and drag
                self.dragging = True
                self.drag_start = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                dx, dy = event.rel
                self.maprect.x += dx
                self.maprect.y += dy
                self.blitmap()

        pygame.display.update()

    def on_execute(self):
        while self.running:
            for event in pygame.event.get():
                self.check_event(event)
        self.on_cleanup()


class Country(App):
    def __init__(self):
        super().__init__()


start = App()
start.on_init()
start.on_execute()
