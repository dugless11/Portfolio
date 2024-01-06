y=0
x=0
lastx=0
lasty=0
doory=0
doorx=0
level=0
key = False
dooropen = False
inventory = []
items = ["*","@","^"]
itemtypes = ["key","wall destoryer","useless item"]
levels = [
  [
    ["=","=","=","="],
    ["="," ","0","="],
    ["=","&"," ","="],
    ["=","=","=","="]
  ],
  [
    ["=","=","=","=","=","="],
    ["=","0","*","#"," ","="],
    ["="," "," ","=","&","="],
    ["=","=","=","=","=","="]
  ],
  [
    ["=","=","=","=","="],
    ["=","0","*"," ","="],
    ["=","=","=","#","="],
    ["=","&"," "," ","="],
    ["=","=","=","=","="]
  ],
  [
    ["=","=","=","=","=","=","="],
    ["=","0"," "," "," ","*","="],
    ["=","=","=","="," ","=","="],
    ["="," ","&","="," "," ","="],
    ["="," ","=","=","="," ","="],
    ["="," ","#"," "," "," ","="],
    ["=","=","=","=","=","=","="]
  ]
]
#print str(doory)+""+str(doorx)+""+str(type(key))
def value():
  global y
  global x
  global lastx
  global lasty
  global doorx
  global doory
  global dooropen
  for i in range(len(levels[level])):
    for q in range(len(levels[level][i])):
      if levels[level][i][q] == "0":
        y = i
        x = q
        lastx = x
        lasty = y
  for w in range(len(levels[level])):
    for s in range(len(levels[level][w])):
      if levels[level][w][s] == "#":
        doory = w
        doorx = s
  key = False
  dooropen = False
  
def update():
  global key
  global dooropen
  if inventory:
    print "You have have a",
    for i in range(len(inventory)):
      print inventory[i]
  if "key" in inventory:
    if not dooropen:
      levels[level][doory][doorx] = " "
    dooropen = True
  for i in range(len(levels[level])):
    for q in range(len(levels[level][i])):
      print levels[level][i][q],
    print ("")
def do(motion):
  global key
  global y
  global x
  global lastx
  global lasty
  global doorx
  global doory
  global level
  global dooropen
  global inventory
  if motion == "east" or motion == "west" or motion == "north" or motion == "south" or motion == "w" or motion == "a" or motion == "s" or motion == "d": 
    if motion == "east" or motion == "d":
      x = x+1
    elif motion == "west" or motion == "a":
      x = x-1
    elif motion == "north" or motion == "w":
      if y != 0:
        y = y-1
      else:
        y = lasty
        update()
    elif motion == "south" or motion == "s":
      if y+1 != len(levels[level]):
        y = y+1
      else:
        y = lasty
        update()
    if levels[level][y][x] == " ":
        levels[level][lasty][lastx] = " "
        levels[level][y][x] = "0"
        lastx = x
        lasty = y
        update()
    elif levels[level][y][x] == "*":
      levels[level][y][x] = "0"
      levels[level][lasty][lastx] = " "
      key = True
      print "You got a key"
      inventory.append("key")
      update()
      lasty = y
      lastx = x
    elif levels[level][y][x] == "&":
      if level+1 < len(levels):
        level = level+1
        key = False
        dooropen = False
        if inventory:
          inventory = []
          value()
          update()
        else:
          value()
          update()
      else:
        print "No more levels left you win"
        update()
    else:
      x = lastx
      y = lasty
      update()
  else:
    print "command unavailable"
update()
value()
print "get to the &, there will be #'s blocking your way but use the * to get past them"
while True:
  motion = str(input("north, east, south, west?"))
  do(motion)


