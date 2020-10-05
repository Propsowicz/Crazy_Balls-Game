import pygame
import random
import math
import SpawnPosition

class Enemy_2:
    def __init__(self, screen_window, windowX, windowY, spawn_X, spawn_Y, radius):
        self.screen_window = screen_window
        self.windowX = windowX
        self.windowY = windowY
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.radius = radius
        self.velocity_X = 4
        self.velocity_Y = 1



        self.color = (150, 255, random.randint(0, 200))

        self.X = SpawnPosition.spawn_pos_X(self.spawn_X, self.windowX)
        self.Y = SpawnPosition.spawn_pos_Y(self.spawn_Y, self.windowY)


        self.random_direction_1 = random.choice((-1, 1))
        self.random_direction_2 = random.choice((-1, 1))


    def screen(self, player_X, player_Y, rect_X, rect_Y):
        pygame.draw.circle(self.screen_window, self.color, (self.X, self.Y), self.radius)
        self.X += round(math.sin(2) * self.velocity_X)
        self.Y += round((math.cos(math.pi/6)) * self.Y * 0.1) * self.velocity_Y

        if self.X >= (self.windowX - self.radius):
            self.velocity_X *= -1
        elif self.X <= (0 + self.radius):
            self.velocity_X *= -1
        elif self.Y >= (self.windowY - self.radius):
            self.velocity_Y *= -1
        elif self.Y <= (0 + self.radius):
            self.velocity_Y *= -1

