import pygame #A library has a set or collection of functions or properties for you to use it properly

pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((50,205,50))
cyan = (0,255,255)
pygame.display.update()

class Circle:
    def __init__(self, clr, radius, pos, width):
        self.circle_colour = clr
        self.circle_radius = radius
        self.circle_pos = pos
        self.circle_width = width
        self.circle_surface = screen
    
    def draw(self):
        self.draw_circle = pygame.draw.circle
        (
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width
        )

    def grow(self, r):
        self.circle_radius = self.circle_radius + r
        self.draw_circle = pygame.draw.circle
        (
            self.circle_surface,
            self.circle_colour,
            self.circle_pos,
            self.circle_radius,
            self.circle_width
        )