#!python3

""" 
Create a reliable method for storing and retrieving data for the game.
"""

def read(square,board):
  square -= 1
  if board[square] == 0:
    return 0
  if board[square] == "X":
    return "X"
  if board[square] == "O":
    return "O"
  
  return None

def write(square,board,player):
  square -= 1
  if board[square] == 0:
    board.pop(square)
    board.insert(square,player)
    return board
  else:
    return board
  

def mainRead():
  board = [ 0, 'X', 0, 'X', 'O', 'O', 0 , 0, 0]
  assert read(3,board) == None
  assert read(2,board) == 'X'
  assert read(5,board) == 'O'

def mainWrite():
  board = [ 0,0,0,0,0,0,0,0,0,0]
  assert write(1,board,'X') == [ 'X',0,0,0,0,0,0,0,0,0]
  assert write(5,board,'O') == [ 'X',0,0,0,'O',0,0,0,0,0]
  #next command should not do anything because square #5 is already occupied by an 'O'
  assert write(5,board,'X') == [ 'X',0,0,0,'O',0,0,0,0,0]
 
  
  
if __name__ == "__main__" :
  mainRead()
  mainWrite()
