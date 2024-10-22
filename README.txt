#Tic-Tac-Toe, The Game

This is my version of tic-tac-toe, which allows a player to play against a computer.


#INSTALLATION + USAGE

The game does not need any additional installation. It is crucial to have Python installed on your machine. Just start the "interface.py"
file and play the game!
The game runs on PyGame library, which isn`t a built in library, so please make sure to install it, the command using pip is:

pip install pygame


For more documentation on PyGame, please visit their official website at:   www.pygame.org


#CONFIGURATION

Available configuration consists of changing game colors. All other changes will require re-writing some additional code.


#STRUCTURE

The project consists of 3 python files. "t_functions.py" includes some functions that are used for the game logic. It also has 
a minimax algorythm implemented. The minimax used is of one of the more simple version, alpha-beta pruning coming in the next game versions.

"buttons.py" has a Button class declaration. In this project buttons have some additional methods to them, such as "place_x" or 
"place_o", which indicate that someone has made a move on that spot.
Some of the importatant moments to be discussed:
The initializer is quite complex, but most of the non-standard attributes have default values. 
The ".draw" method will displaythe button as well as the text in the self.text attribute.
The buttons also support assigning click-handlers and excecuting them.

"interface.py" has everything that has to do with interface, as well as the game flow controls are also located there.
Some important momnets to be discussed:

The main global variable that controls the flow of the whole program - "game_started".
In the event handler, since no particular button was specified on line 63 and onwards, the game will react to any mouse button. 
Ths was done on purpose, however this feature may be deleted in the future updates, if the complexity of the game and some new features
will require that.
As it is said on line 122, instead of thinking of the third state of the game, the restart button is drawn directly on top of the play
button which was drawn there as soon as the game was stopped. Since they have exactly the same functionality, the restart button just
covers the play button without deleting it. To make this possible, the start button is always prepended to the list of buttons for
interface, so that it will be drawn first.
