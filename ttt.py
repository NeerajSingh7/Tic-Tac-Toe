
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

gamestillgoing=True
winner=None

currplayer="X"

def displayboard():
   print(board[0]+" | "+board[1]+" | "+board[2])
   print(board[3]+" | "+board[4]+" | "+board[5])
   print(board[6]+" | "+board[7]+" | "+board[8])
  

def playgame():
   
  displayboard()
  while gamestillgoing:

      handleturn(currplayer)

      checkifgameover()

      flipplayer()
  
  if winner=="X" or winner=="O":
      print(winner+" won")
  elif winner==None:
      print("Tie")



def handleturn(player):
  print(player+"'s turn")
  location=int(input("enter location from 1-9:"))
  valid=False
  while not valid: 
    while location not in [1,2,3,4,5,6,7,8,9]:
        location=int(input("Invalid input! enter location from 1-9:"))
    location=location-1

    if board[location]=="-":
        valid=True
    else:
        print("you can't go there! Go again")
    board[location]=player
    displayboard()


def checkifgameover():
  checkifwin()
  checkiftie()


def checkifwin():

  global winner
  rowwinner=winrow()
  columnwinner=wincolumn()
  diagonalwinner=windiagonal()

  if(rowwinner):
      winner=rowwinner
  elif(columnwinner):
      winner=columnwinner
  if(diagonalwinner):
      winner=diagonalwinner




def winrow():
    global gamestillgoing
    row1=board[0]==board[1]==board[2]  !="-"
    row2=board[3]==board[4]==board[5]  !="-"
    row3=board[6]==board[7]==board[8]  !="-"

    if row1 or row2 or row3:
        gamestillgoing=False
    
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def wincolumn():
    global gamestillgoing
    column1=board[0]==board[3]==board[6]  !="-"
    column2=board[1]==board[4]==board[7]  !="-"
    column3=board[2]==board[5]==board[8]  !="-"

    if column1 or column2 or column3:
        gamestillgoing=False
    
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def windiagonal():
    global gamestillgoing
    diagonal1=board[0]==board[4]==board[8]  !="-"
    diagonal2=board[2]==board[4]==board[6]  !="-"
    

    if diagonal1 or diagonal2:
        gamestillgoing=False
    
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return


def checkiftie():
    global gamestillgoing
    if "-" not in board:
        gamestillgoing=False
    return


def flipplayer():
    global currplayer
    if currplayer=="X":
        currplayer="O"
    elif currplayer=="O":
        currplayer="X"
    return

playgame()
