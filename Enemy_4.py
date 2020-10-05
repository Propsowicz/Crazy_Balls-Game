import pygame
import random
import math
import SpawnPosition

class Enemy_4:
    def __init__(self, screen_window, windowX, windowY, spawn_X, spawn_Y, radius):
        self.screen_window = screen_window
        self.windowX = windowX
        self.windowY = windowY
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.radius = radius
        self.velocity_X = 2
        self.velocity_Y = 2



        self.color = (255, 255, random.randint(90, 150))

        self.X = SpawnPosition.spawn_pos_X(self.spawn_X, self.windowX)
        self.Y = SpawnPosition.spawn_pos_Y(self.spawn_Y, self.windowY)


        self.random_direction_1 = random.choice((-1, 1))
        self.random_direction_2 = random.choice((-1, 1))


    def screen(self, player_X, player_Y, rect_X, rect_Y):
        pygame.draw.circle(self.screen_window, self.color, (self.X, self.Y), self.radius)
        self.X += self.velocity_X
        self.Y += self.velocity_Y


        if rect_Y not in range(self.Y - 100, self.Y + 100) and rect_X not in range(self.X - 100, self.X + 100):


            if rect_X > self.X:
                self.velocity_X = 2
            elif rect_X < self.X:
                self.velocity_X = -2


            if rect_Y > self.Y:
                self.velocity_Y = 2
            elif rect_Y < self.Y:
                self.velocity_Y = -2






        if self.X >= (self.windowX - self.radius):
            self.velocity_X *= -1
        elif self.X <= (0 + self.radius):
            self.velocity_X *= -1
        elif self.Y >= (self.windowY - self.radius):
            self.velocity_Y *= -1
        elif self.Y <= (0 + self.radius):
            self.velocity_Y *= -1


