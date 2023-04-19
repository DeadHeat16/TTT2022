import os

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0
p1_name = 'Player 1'
p2_name = 'Player 2'

def check_win_screen(game_board):
  # Horizontal Checks
  for j in game_board:
    #Horizontal checks in row 0
    if game_board[0][0] + game_board[0][1] + game_board[0][2] == 'XXX':
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][0] + game_board[0][1] + game_board[0][2] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Horizontal Checks in row 1
    elif game_board[1][0] + game_board[1][1] + game_board[1][2] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[1][0] + game_board[1][1] + game_board[1][2] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Horizontal Checks in row 2
    elif game_board[2][0] + game_board[2][1] + game_board[2][2] == "XXX":
      print_board(game_board)
      print("Player 1 win!")
      playAgain()
    elif game_board[2][0] + game_board[2][1] + game_board[2][2] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Vertical Checks in column 0
    elif game_board[0][0] + game_board[1][0] + game_board[2][0] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][0] + game_board[1][0] + game_board[2][0] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Vertical checks in column 1
    elif game_board[0][1] + game_board[1][1] + game_board[2][1] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][1] + game_board[1][1] + game_board[2][1] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Vertical Checks for Column 2
    elif game_board[0][2] + game_board[1][2] + game_board[2][2] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][2] + game_board[1][2] + game_board[2][2] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    #Diagonal Checks from Right to left
    elif game_board[0][2] + game_board[1][1] + game_board[2][0] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][2] + game_board[1][1] + game_board[2][0] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()
    # Diagonal Checks for Left to Right
    elif game_board[0][0] + game_board[1][1] + game_board[2][2] == "XXX":
      print_board(game_board)
      print("Player 1 wins!")
      playAgain()
    elif game_board[0][0] + game_board[1][1] + game_board[2][2] == "OOO":
      print_board(game_board)
      print("Player 2 wins!")
      playAgain()

# Prints the board
def print_board(game_board):
  ro = -1
  print("  0 1 2")
  for row in game_board:
    ro += 1
    print(ro, end=" ")
    for col in row:
      # Now prints the coords of each position of the board, per request of Bryan's and Markus's request #
      print(col, end=" ")
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol, game_board):
  if (game_board[row][col] == "_"):
    game_board[row][col] = symbol
  else:
    print("already chosen!")

# Changes to next turn
def change_turn():
  global turn
  turn += 1
  if turn % 2 == 0:
    print("\033[1;34;40m \n")
  else:
    print("\033[1;32;40m \n")

def player_in():
  while True:
    try:
      row_choice = int(input('Which row would you like to choose? '))
      col_choice = int(input('Which column would you like to choose? '))
    except:
      print("Not a valid option, please try again.")
    else:
      if row_choice <= 2 and col_choice <= 2:
        return row_choice, col_choice
      else:
        print("Not a valid option, please try again.")

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)

def show_name():
  if turn % 2 == 0:
    print(f"Player 1: {p1_name}")
  else:
    print(f"Player 2: {p2_name}")

# Function that creates and starts the game.
def playgame():
  board = [['_','_','_'],
            ['_','_','_'],
            ['_','_','_']]
  while turn <= 9:
  
  # Print the board and whose turn it is
    print_board(board)
    show_name()

    if turn % 2 == 0:
      print("\033[1;34;40m \n")
    else:
      print("\033[1;32;40m \n")
  
  # Get the user input
    row_choice, col_choice = player_in()

    print("\033[1;34;40m \n")

  # Put their move on the board
    make_move(row_choice, col_choice, symbols[turn], board)
  # Clear the console from previous turn
    clearConsole()
  # Next turn
    change_turn()

  # Check for Win
    check_win_screen(board)
  
  print_board(board)
  print("There are no space left in the board to fill, the game is a draw")
  playAgain()

# Executed after game is finished. Asks the user to input 1 to play another game and 2 to end the program.
def playAgain():
  choice = "-1"
  # Asks for input
  print("Would you like to play again? Select 1 to play again, select 2 to end game. ")
  choice = str(input())
  # if input is not 1 or 2 then ask user to re-input 1 or 2. Will repeat until 1 or 2 is inputted.
  while choice != "1" and choice != "2":
    print("Please select 1 or 2. Would you like to play again? ")
    choice = str(input())
  # if input is 1 then replay.
  if choice == "1":
    clearConsole()
    playgame()
  # if input is 2 then end the program
  elif choice == "2":
    print("Thanks for playing!")
    quit()

# Begin the program
print('''
 ____  __  ___    ____  __    ___    ____  __  ____ 
(_  _)(  )/ __)  (_  _)/ _\  / __)  (_  _)/  \(  __)
  )(   )(( (__     )( /    \( (__     )( (  O )) _) 
 (__) (__)\___)   (__)\_/\_/ \___)   (__) \__/(____)
  ''')

p1_name = input('Player 1, what is your name? ')
p2_name = input('Player 2, what is your name? ')

playgame()
