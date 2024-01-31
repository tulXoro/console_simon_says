from time import sleep
from replit import clear
from random import randint
from readchar import readkey

# Constants
BLANK = "⬜"
T_RIGHT = "🟨"
T_LEFT = "🟦"
B_RIGHT = "🟥"
B_LEFT = "🟩"
WRONG = "❎"

# global vars
board = [[BLANK, BLANK], 
         [BLANK, BLANK]]
c_pos = [[T_RIGHT, T_LEFT], 
         [B_RIGHT, B_LEFT]]
square_queue = []
player_turn = 0 # current num player is on
player_buffer = 0 # convert player's input into squares
player_input = False # flag to check if it is the player's turn

# functions
def show_board():
  clear()
  for i in board:
    print(" ".join(i))

  if player_input:
    print("YOUR TURN!")
  else:
    print("WATCH!")

# activate a square
def act_square(pos1, pos2, reset = False):
  global board
  board[pos1][pos2] = BLANK if reset else c_pos[pos1][pos2]

# change a square and show it
def change_board(pos1, pos2):
  if not player_input:
    act_square(pos1, pos2)
    show_board()
    sleep(1)
    act_square(pos1, pos2, True)
  else:
    # make player's turn faster
    act_square(pos1, pos2)
    show_board()
    sleep(0.5)
    act_square(pos1, pos2, True)
  show_board()

# take user's input
def handle_key(k):
  global player_buffer
  res = 0
  match k:
    case "q":
      player_buffer = 0
      res = change_board(0, 0)
      return res
    case "w":
      player_buffer = 1
      res = change_board(0, 1)
      return res
    case "a":
      player_buffer = 2
      res = change_board(1, 0)
      return res
    case "s":
      player_buffer = 3
      res = change_board(1, 1)
      return res
    case _:
      return -1

# show squares the player should enter and adds a new one
def show_squares():
  for i, square in enumerate(square_queue):
    match square:
      case 0:
        change_board(0, 0)
      case 1:
        change_board(0, 1)
      case 2:
        change_board(1, 0)
      case 3:
        change_board(1, 1)
    show_board()
    sleep(1)

  # add a new square
  val = randint(0, 3)
  match val:
    case 0:
      change_board(0, 0)
    case 1:
      change_board(0, 1)
    case 2:
      change_board(1, 0)
    case 3:
      change_board(1, 1)
  square_queue.append(val)
  show_board()

# init game
print("🇶  🇼")
print("🇦  🇸")

print("Use these keys on your keyboard.")
print("Press any key to continue...")
readkey()

# game loop
while True:
  show_board()
  sleep(1)
  # SHOW SQUARES IN ORDER
  show_squares()
  # LET PLAYER SELECT SQUARES IN ORDER
  player_input = True
  show_board()
  for i, square in enumerate(square_queue):
    k = readkey()
    handle_key(k)
    # set all squares to wrong when player enters the wrong square
    if square_queue[player_turn] != player_buffer:
      for j in range(2):
        for k in range(2):
          board[j][k] = WRONG
      show_board()
      exit()
    else:
      player_turn += 1
  player_turn = 0
  player_input = False
  