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

#checks number of X and O in board and holds a counter value, when 3 values are found then stop game and run game over screen 
#Check Diagonals
#if board[0][0]+ board[1][1]+board[2][2]=='XXX':
      #print("Player 1 wins!")
      #quit()

def check_win_screen():
  x_counter=0
  o_counter=0
  # Horizontal Checks 
  for j in board:
    #Horizontal checks in row 0
    if board[0][0]+ board[0][1]+board[0][2]=='XXX':
      print_board()
      print("Player 1 wins!")
      quit()
    if board[0][0]+board[0][1]+board[0][2]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit()
    #Horizontal Checks in row 1 
    if board[1][0]+board[1][1]+board[1][2]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit()
    if board[1][0]+board[1][1]+board[1][2]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit
    #Horizontal Checks in row 2
    if board[2][0]+board[2][1]+board[2][2]=="XXX":
      print_board()
      print("Player 1 win!")
      quit()
    if board[2][0]+board[2][1]+board[2][2]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit()
    #Vertical Checks in column 0 
    if board[0][0]+board[1][0]+board[2][0]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit() 
    if board[0][0]+ board[1][0] + board[2][0]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit() 
    #Vertical checks in column 1
    if board[0][1]+board[1][1]+board[2][1]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit() 
    if board[0][1]+board[1][1]+board[2][1]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit() 
    #Vertical Checks for Column 2 
    if board[0][2]+board[1][2]+board[2][2]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit()
    if board[0][2]+board[1][2]+board[2][2]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit() 
    #Diagonal Checks from Right to left 
    if board[0][2]+board[1][1]+board[2][0]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit()
    if board[0][2]+board[1][1]+board[2][0]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit() 
    # Diagonal Checks for Left to Right 
    if board[0][0]+board[1][1]+board[2][2]=="XXX":
      print_board()
      print("Player 1 wins!")
      quit() 
    if board[0][0]+board[1][1]+board[2][2]=="OOO":
      print_board()
      print("Player 2 wins!")
      quit()  


       
  


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
  return False

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

  # Check for Win
  check_win_screen()
