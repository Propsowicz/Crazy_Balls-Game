import pygame
import SpawnPosition

class Player_ball:
    def __init__(self, screen_window, windowX, windowY, radius, X, Y, velocity):
        self.screen_window = screen_window
        self.windowX = windowX
        self.windowY = windowY

        self.radius = radius
        self.X = X
        self.Y = Y
        self.velocity = velocity

        self.color = (255, 255, 255)

        self.game_over = False

    def screen(self):
        if self.game_over:
            pass

        else:
            pygame.draw.circle(self.screen_window, self.color, (self.X, self.Y), self.radius)





    def movement(self, key_presses):

        if key_presses[pygame.K_UP] and self.Y > (0 + self.radius):
            self.Y -= self.velocity

        if key_presses[pygame.K_DOWN] and self.Y < (self.windowY - self.radius):
            self.Y += self.velocity

        if key_presses[pygame.K_RIGHT] and self.X < (self.windowX - self.radius):
            self.X += self.velocity

        if key_presses[pygame.K_LEFT] and self.X > (0 + self.radius):
            self.X -= self.velocity





