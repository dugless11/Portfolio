import turtle
import random
which = True
Screen = turtle.Screen()
t = turtle.Turtle()
t.speed(-1)
t.pu()
t.goto(-200,200)
t.pd()
t.hideturtle()
for i in range(2):
  for j in range(2):
    t.right(90)
    t.pu()
    t.fd(400/3)
    t.pd()
    t.left(90)
    t.fd(400)
    t.fd(-400)
  t.right(90)
  t.pu()
  t.fd(400/3)
  t.pd()
  t.left(180)
grid = [
  ["","",""],
  ["","",""],
  ["","",""]
  ]
def chooseO():
  global which
  global grid
  #print grid
  #win first
  # i = row
  #j = col
  move = []
  """for letter in ["o","x"]:
    for i in range(3):
      for j in range(3):
        if i == 0:
          if grid[1][j] == grid[2][j] and grid[1][j] != " ":
            move.append([j,0])
          #print "a"
        elif i == 1:
          if grid[0][j] == grid[2][j] and grid[0][j] != '':
            move.append([j,1])
            #print "b"
        elif i == 2:
          if grid[1][j] == grid[0][j] and grid[1][j] != '':
            move.append([j,2])
            #print "c"
        elif j == 0:
          if grid[i][1] == grid[i][2] and grid[i][1] != '':
            move.append([0,i])
            #print"d"
        elif j == 1:
          if grid[i][0]== grid[i][2]and grid[i][0] != '':
            move.append([1,i])
            #print"c"
        elif j == 2:
          if grid[i][1] == grid[i][0] and grid[i][1] != '':
            move.append([2,i])
            #print"f"
        #diagonal
        elif i+1<3 and j+1<3:
          if grid[i][j] == grid[i+1][j+1] and grid[i][j] != '' and i == j:
            if i-1>0:
              move.append([j-1][i-1])
            if i+2<3:
              move.append([j+2][i+2])
        #elif i+1<3 and 3-j>0:
        #   if grid[i][3-j] == grid[i-1][2-j] and grid[i][3-j] != '':
        #    if i-1>0:
        # this kinda broken
        #      move = [2-j][i-1]
        #    if i+2<3:
        #      move = [5-j][i+2]"""
  #print grid
  tempGrid = grid
  for sign in ["o","x"]:
    for i in range(3):
      for j in range(3):
        tem = tempGrid[i][j]
        if tempGrid[i][j] == '':
          print "t"
          tempGrid[i][j] = sign
        if check(tempGrid, False) == sign:
          move.append([i,j])
          #print grid
        tempGrid[i][j] = tem
  #print grid
  #print "a"
  if move == []:
    move.append([0,0])
    move.append([2,2])
    move.append([2,0])
    move.append([0,2])
    move.append([1,1])
    move.append([0,1])
    move.append([1,0])
    move.append([2,1])
    move.append([1,2])
  for i in range(len(move)):
    #print i
    #print len(move)
    #print grid
    #print grid[move[0][0]][move[0][1]]
    if grid[move[0][0]][move[0][1]] != '':
      #print "test"
      move.remove(move[0])
  if move == []:
    quit()
  #print move[0]
  #print move
  O(-200+move[0][1]*400/3,200-move[0][0]*400/3)
  grid[move[0][0]][move[0][1]] = "o"
  print grid
  #update(-166+move[0][0]*400/3,166-move[0][1]*400/3)
  #print str(int(-166+move[0][0]*400/3))+" "+str(int(166-move[0][1]*400/3))
  #print("test")
def X(x,y):
  t.pu()
  t.goto(x,y)
  t.pd()
  t.seth(315)
  t.fd(188.5618)
  t.fd(-94.2809)
  t.right(90)
  t.fd(94.2809)
  t.fd(-188.5618)
def O(x,y):
  t.pu()
  t.goto(x+200/3,y-400/3)
  t.pd()
  t.seth(0)
  t.circle(200/3)
  
def update(x,y):
  global which
  global grid
  col=0;
  row=0;
  if x<-67:
    col = 0;
  elif x>67:
    col=2;
  else:
    col=1;
  if y<-67:
    row = 2;
  elif y>67:
    row=0;
  else:
    row=1 
  if grid[row][col]=='':
    #print grid[row][col]
    grid[row][col] = "x"
    #print grid[row][col]
    #print grid
    #print "t"
    X(-200+col*400/3,200-row*400/3)
    chooseO()
    #print("choosen")
  #debug stuff V
  #print(grid)
  #print(which)
  #X(-200+col*400/3,200-row*400/3)
  #updateGrid()
  check(grid, True)
def check(grid, win):
  #print grid
  for i in range(3):
    #row test
    if grid[i][0]==grid[i][1] and grid[i][1] == grid[i][2] and grid[i][0]!='':
      if win:
        print(grid[i][0] + " has won")
      return grid[i][0]
    #column test
    elif grid[0][i]==grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i]!='':
      if win:
        print(grid[0][i] + " has won")
      return grid[0][i]
    #diag tests
    elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0]!='':
      if win:
        print(grid[0][0] + " has won")
      return grid[0][0]
    elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2]!='':
      if win:
        print(grid[2][0] + " has won")
      return grid[2][0]
    #tie test

      #all(test !=''for test in grid) dunno if this works
  if all(test[i] !=''for i in [0,1,2] for test in grid):
    if win:
      print("cat's game")
    quit()
  return -1
def updateGrid():
  #i=row j = col
  
  for i in range(3):
    for j in range(3):
      if grid[i][j] == "x":
        X(-200+j*400/3,200-i*400/3)
   
while True:
  Screen.onclick(update)
  #updateGrid()
