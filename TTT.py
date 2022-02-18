board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0

def welcome_screen():
  logo = '''
 ____  __  ___    ____  __    ___    ____  __  ____ 
(_  _)(  )/ __)  (_  _)/ _\  / __)  (_  _)/  \(  __)
  )(   )(( (__     )( /    \( (__     )( (  O )) _) 
 (__) (__)\___)   (__)\_/\_/ \___)   (__) \__/(____)
  '''
  print(logo)

# Prints the board
def print_board():
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol):
  board[row][col] = symbol

# Returns true when the game is over 
# Note: Just a stub. Doesn't work yet
def is_game_over():
  if is_game_draw() is True:
    return True 
  return False

def is_game_draw():
  for row in board:
   for item in row:
     if item == '_' :
       return False 
  return True

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2

welcome_screen()
while not is_game_over():
  # Print the board and whose turn it is
  print_board()
  print('Player {}'.format(turn+1))

  # Get the user input
  row_choice = int(input('Which row would you like to choose? '))
  col_choice = int(input('Which column would you like to choose? '))

  if (row_choice > 2 or row_choice < 0 or col_choice > 2 or col_choice < 0):
    print(f"({row_choice}, {col_choice}) is not on the grid. Please use row and column numbers from 0 to 2.")
    continue

  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn])

  # Next turn
  change_turn()
print_board()
if is_game_draw() is True:
  print("There are no space left in the board for you to fill.")