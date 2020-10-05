import pygame
import random
import SpawnPosition


class Point:
    def __init__(self, screen_window, pt_X, pt_Y, windowX, windowY):
        self.screen_window = screen_window
        self.pt_X = pt_X
        self.pt_Y = pt_Y
        self.windowX = windowX
        self.windowY = windowY
        self.rect_dim = 26


        self.color = (255, 255, 255)

        self.X = SpawnPosition.spawn_pos_X(self.pt_X, self.windowX)
        self.Y = SpawnPosition.spawn_pos_Y(self.pt_Y, self.windowY)



    def screen(self):
        pygame.draw.rect(self.screen_window, self.color, (self.X - self.rect_dim / 2, self.Y - self.rect_dim / 2, self.rect_dim, self.rect_dim), 3)


