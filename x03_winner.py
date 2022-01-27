#!python3

"""
Create a function that will determine if one person is the winner (has 3 in a row)
inputs:
list board : the list that contains the board data

return:
str 'X' if X is the winner
str 'O' if O is the winner
None if there is no winner
"""

def whoWins(board):
  if board[0] == board[1] == board[2] and board[0] != 0:
    return str(board[0])
  elif board[0] == board[3] == board[6] and board[0] != 0:
    return str(board[0])
  elif board[2] == board[5] == board[8] and board[2] != 0:
    return str(board[2])
  elif board[1] == board[4] == board[7] and board[1] != 0:
    return str(board[1])
  elif board[3] == board[4] == board[5] and board[3] != 0:
    return str(board[3])
  elif board[6] == board[7] == board[8] and board[6] != 0:
    return str(board[6])
  elif board[0] == board[4] == board[8] and board[0] != 0:
    return str(board[0])
  elif board[2] == board[4] == board[6] and board[2] != 0:
    return str(board[2])
  else:
      return None
    
  
  return None


def main():
  board = [ 'O','X',0,'X','O',0,'X',0,'O']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','O','X','O','O','X']
  assert whoWins(board) == 'O'
  board = [ 'X','O',0,'X','X','O','O','X','O']
  assert whoWins(board) == None
  board = [ 'X','O',0,'X','X','X','O','O','X']
  assert whoWins(board) == 'X'

if __name__ == "__main__":
  main()
