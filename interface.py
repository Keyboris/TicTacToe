import pygame
import sys
from buttons import Button
import t_functions

def display_text(text, x, y, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

#FUNCTIONS FOR CLICK HANDLERS
def play_func():
    screen.fill((0,0,0))
    global game_started
    game_started = True
    global Buttons_for_interface
    Buttons_for_interface = []


def grid():
        Black_square = pygame.Rect(screen.get_width()//4, screen.get_height()//4, 500,500)
        pygame.draw.rect(screen, (0,0,0), Black_square)
        global Buttons_for_grid
        Buttons_for_grid = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                Buttons_for_grid[i][j] = Button(Black_square.x+170*j, Black_square.y+170*i, 160,160, (125, 111, 134), text = None, click_handler= None,screen = screen)
                Buttons_for_grid[i][j].draw(screen)




#INITIALIZING EVERYTHING 
pygame.init()

screen = pygame.display.set_mode((1024, 720))
display_width, diplay_height = screen.get_size()
running = True
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Tic Tac Toe, The Game")

# Game variables
game_started = False

Buttons_for_interface = []   #this array will be used for all functioning buttons, that are not cells in the actual grid (play, restart, etc.)

Buttons_for_grid = [] #this array will be used only for cells on the grid of the game itself

#STATE MANAGER

win = False

moves = 0

screen.fill((255, 250, 251))
display_text("Tic Tac Toe, The Game", 380, 200, (0, 5, 5))

# EVENT HANDLER + GAME STATES
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if not game_started:   #if the game is not started, then we only care about the usesul UI buttons from the buttons_for_interface array
                for button in Buttons_for_interface:
                    if button.pointed_at() and button.click_handler == play_func:
                        button.action()
                        

            else:  #if the game is started, we only care about the buttons on the grid
                for index_i, row in enumerate(Buttons_for_grid):
                    for index_j, button in enumerate(row):
                        if button.pointed_at() and button.clickable:
                            button.place_x()
                            button.clickable = False
                            board[index_i][index_j] = "X"
                            moves += 1
                            pygame.display.flip()
    #GAME STATES

    if game_started:

        if moves == 0:  #Initialize the scene before the first move
            win = False 

            board = [[' ' for _ in range(3)] for _ in range(3)]
            
            screen.fill((255, 250, 251))

            text_width, text_height = font.size("the game has started")
            x = (screen.get_width() - text_width)//2
            y = (screen.get_height() - text_height)//6
            display_text("The Game Is ON!", x, y, (0, 5, 5))

            result = False
            state = 0

            grid()

            pygame.display.flip()

            moves += 1

        state = t_functions.scanVic(board)  #Get the state of the game
        result, sign = state

        if result:     #If the game is over:
            grey_square = pygame.Rect(x, y, 300, 40)
            pygame.draw.rect(screen, (255, 250, 251), grey_square)  #the grey square is needed to cover up "the game is on!!"

            display_text("The Game is OVER!",x,y,(0, 5, 5))
            win = True
            game_started = False
            moves = 0
            for i in range(3):
                for j in range(3):
                    Buttons_for_grid[i][j].clickable = False
            Buttons_for_interface = [Button(display_width//2-150, 500, 300, 100, (104, 166, 145), "RESTART", play_func, screen)]
            #when the game is finished, the game_started is set to False, which executes the else: block below. the "RESTART" button is drawn
            #above the "PLAY" button, which is now completely covered. this allows me to save some lines of code and not think of the
            #3rd state of the program, the restart state.

        elif moves == 10:  #If the game is a draw
            display_text("the game is over!!", x,y,(0,0,0))
            game_started = False
            moves = 0
            win = False
            Buttons_for_interface = [Button(412, 500, 200, 100, (134, 31, 124), "RESTART", play_func, screen)]
            #the same goes here

        elif moves % 2 == 1 and not win:   #Player moves
            pass

        elif moves % 2 == 0 and not win: #Computer moves
            i, j = t_functions.compMove(board)
            board[i][j] = "O"
            Buttons_for_grid[i][j].place_o()
            Buttons_for_grid[i][j].clickable = False
            pygame.display.flip()
            moves += 1

    else:  #The game has ended/ has not been started
        if len(Buttons_for_interface) <= 1:
            Buttons_for_interface = [Button(display_width//2-150, 500, 300, 100, (104, 166, 145), "PLAY", click_handler=play_func)] + Buttons_for_interface
            #i am prepending the buttons, and not appending them becuase the piece of code below will draw them first to last. this allows me to
            #save some lines and not make another case for restarting the game as opposed to starting it for the firt time by overlaying
            #the restart button on top of the play button
            for button in Buttons_for_interface:
                button.draw(screen)
        pygame.display.flip()


pygame.quit()
