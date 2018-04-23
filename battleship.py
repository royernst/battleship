from random import randint
from time import sleep

board = {}
player = {
  "carrier": {"size": 5},
  "battleship": {"size": 4},
  "submarine": {"size": 3},
  "cruiser": {"size": 3},
  "destroyer": {"size": 2}
}
computer = {
  "carrier": {"size": 5},
  "battleship": {"size": 4},
  "submarine": {"size": 3},
  "cruiser": {"size": 3},
  "destroyer": {"size": 2}
}
"""
  Possible glyphs: O = free, H = hit, M = miss, X = player ship
  possible flags: free, hit, miss, ship
"""
grid = int(raw_input("How big of a grid would you like to play on (standard grid is 10x10)"))
for x in range(0, grid):
  board.update([{
    "glyph": "O",
    "flag": "free"
    }] * grid)

def ship_place(this_player):
  for ship in this_player:
    range_upper = ship["size"]
    print range_upper
    for i in range(0, range_upper):
      ship.update({"slot%d" % i + 1: {"x":0, "y": 1}})
  print this_player

ship_place(player)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

print("Placing ships...")
sleep(2)

comp_ship_row = random_row(board)
comp_ship_col = random_col(board)
print ship_row
print ship_col

last_row = 0
last_col = 0
def comp_guess():
  if was_hit == True:
    guess_row = "X"
  else:
    guess_row = random_row(board)
    guess_col = random_col(board)
    if board[guess_row][guess_col] == "X":
      comp_guess()
    elif board[guess_row][guess_col] == board[player_ship_row][player_ship_col]:
      board[guess_row][guess_col] = "X"
      was_hit = True
    else:
      board[guess_row][guess_col] = "X"
      was_hit = False
  last_row = guess_row
  last_col = guess_col

for turn in range(4):
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print "Game Over"
    print (turn + 1)
    print_board(board)