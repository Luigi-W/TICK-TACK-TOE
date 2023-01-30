#--------GLOBAL VARIABLES


board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

game_is_still_going = True
winner = None
current_player = 'X'


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])



def play_game():
  display_board()

  while game_is_still_going:

    handle_turn(current_player)

    check_if_game_over()

    flip_player()


def handle_turn(player):
  print("You are " + player + "'s.")
  position = input("Please pick a position from 1-9 for your next move:")

  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Pick a number from 1-9 for your next turn:")
    position = int(position) -1
    if board[position] != '-':
      print ("You can't go there. Go again.")
    else: 
      valid = True

  board[position] = player
  display_board()


def check_if_game_over():
  check_win()
  check_draw()
  if winner == 'X' or winner == '0':
      print('Winner is ' + winner + '!!')
  if winner == None and game_is_still_going == False:
    print("It's a tie!!")
  return


def check_win():
  #set up global variables
  global winner
  #check rows, columns, and diagonals
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  #define winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  return


def check_rows():
  #set up global variables
  global game_is_still_going
  #check rows for win
  row1 = board[0] == board[1] == board[2] != '-'
  row2 = board[3] == board[4] == board[5] != '-'
  row3 = board[6] == board[7] == board[8] != '-'
  #if any rows is a match, flag that there is a win
  if row1 or row2 or row3:
    game_is_still_going = False
  if row1:
    return board[0]
  if row2:
    return board[3]
  if row3:
    return board[6]
  return 



def check_columns():
  #set up global variables
  global game_is_still_going
  #check columns for win
  column1 = board[0] == board[3] == board[6] != '-'
  column2 = board[1] == board[4] == board[7] != '-'
  column3 = board[2] == board[5] == board[8] != '-'
  #if any columns is a match, flag that there is a win
  #return winner as X or 0
  if column1 or column2 or column3:
    game_is_still_going = False
  if column1:
    return board[0]
  if column2:
    return board[1]
  if column3:
    return board[2]
  return 


def check_diagonals():
  #set up global variables
  global game_is_still_going
  #check diagonals for a win
  diagonal1 = board[0] == board[4] == board [8] != '-'
  diagonal2 = board[2] == board[4] == board[6] != '-'
  if diagonal1 or diagonal2:
    game_is_still_going = False
  if diagonal1:
    return board[4]
  if diagonal2:
    return board[4]
  return


def check_draw():
  #set up global variables
  global game_is_still_going
  #check that all places in the board has been occupied
  if '-' not in board:
    game_is_still_going = False
    return
  return


def flip_player():
#define global variables
  global current_player
  if current_player == 'X':
    current_player = '0'
  elif current_player == '0':
    current_player = 'X'
  return

play_game()
