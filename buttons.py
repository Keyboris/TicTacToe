import pygame


class Button:
    def __init__(self, x_coor, y_coor, width, height, color = (0,0,0),text = None, click_handler = None, screen = None, clickable = True):
        self.x = x_coor
        self.y = y_coor
        self.color = color
        self.width = width
        self.height = height
        self.text = text
        self.click_handler = click_handler
        self.screen = screen
        self.clickable = clickable

    def draw(self, screen):  #draws the button, text on the screen
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, button)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)
        
    def pointed_at(self):
        x,y = pygame.mouse.get_pos()
        temp = pygame.Rect(self.x, self.y, self.width, self.height)  #creates a rect object above the actual button and check for the hit
                                                                     #with this new rect object
        return temp.collidepoint(x,y)

    def place_x(self):
        pygame.draw.line(self.screen, (0,0,0), (self.x+3,self.y), (self.x+self.width-5, self.y+self.height-2), 8)
        pygame.draw.line(self.screen, (0,0,0), (self.x+self.width-5, self.y), (self.x+3, self.y+self.height-2), 8)

    def place_o(self):
        pygame.draw.circle(self.screen, (0,0,0), (self.x+self.width//2, self.y+self.height//2), self.width//2, 6)

    def action(self):
        if self.click_handler is not None:
            self.click_handler()
         
