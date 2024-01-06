import random
#SHARD = stamina, health, attack, recovery, defense
maxS = 10
maxH = 100
sp = 10
hp = 100
attack = 10
recovery = 10
defense = 10
defending = False
#weapons,  ring/amulet, armour/shield,
inventory = [[],[],[]]
equip = ["Fists: 0","Basic ring: 0","Arm: 0"]
diff = 1
def findStat(item):
  colonIndex = 0
  for i in range(len(item)):
    if item[i] == ":":
      colonIndex = i
  return int(item[colonIndex+1:len(item)])
def changeEquip():
  global equip
  global inventory
  global attack
  global defense
  global recovery
  #display curent equipment
  print("Weapon(strength): "+equip[0])
  print("Accesory(recovery): "+equip[1])
  print("Defense(defense): "+equip[2])
  #loop for changing
  done = False
  while done != True:
    print "inventory: "+str(inventory)
    i = input("What do you want to switch? (weapon, accesory, shield)")
    while i != "weapon" and i != "accesory" and i != "shield":
      print "input not understood"
      i = input("What do you want to switch? (weapon, accesory, shield)")
      #weapon change
    if i=="weapon":
      print(inventory[0])
      i = int(input("enter index of which weapon you want to use"))
      while not(isinstance(i, int)) or i>len(inventory[0]):
        print "input not available"
        i = int(input("enter index of which weapon you want to use"))
        #stat correction
      attack -= findStat(equip[0])
      equip[0] = inventory[0][i]
      attack += findStat(equip[0])
      print("Weapon:"+equip[0])
      #accesory change
    elif i=="accesory":
      print(inventory[1])
      i = int(input("enter index of which accesory you want to use"))
      while not(isinstance(i, int)) or i>len(inventory[1]):
        print "input not available"
        i = int(input("enter index of which accesory you want to use"))
        #stat correction
      recovery -= findStat(equip[1])
      equip[1] = inventory[1][i]
      recovery += findStat(equip[1])
      print("Accesory:"+equip[1])
      #shield change
    elif i=="shield":
      print(inventory[2])
      i = int(input("enter index of which shield you want to use"))
      while not(isinstance(i, int)) or i>len(inventory[2]):
        print "input not available"
        i = int(input("enter index of which shield you want to use"))
        #stat correction
      defense -= findStat(equip[2])
      equip[2] = inventory[2][i]
      defense += findStat(equip[2])
      print("Shield:"+equip[2])
    done = (input("Are you done now?")=="yes")
  
def stat(char,s,h,a,r,d,maxS,maxH):
    print
    print(char+" Stamina:"+str(s)+"/"+str(maxS))
    print(char+" Health:"+str(h)+"/"+str(maxH))
    print(char+" Attack:"+str(a))
    print(char+" Recovery:"+str(r))
    print(char+" Defense:"+str(d))
def fight(diff):
  global maxS
  global maxH
  global sp
  global hp
  global attack
  global recovery
  global defense
  global defending
  global inventory
  enemyType = random.choice(["Goblin","Slime","Imp","Demon","Werewolf","Vampire","Zombie","Plant","Ghost","Spirit","Abomination","Worm"])
  if diff%5 == 0:
    monS = int(2*(int(diff/5)+1)*random.uniform(1,5))
    monH = int(40*(int(diff/5)+1)*random.uniform(1,5))
    monA = int(2*(int(diff/5)+1)*random.uniform(1,5))
    monR = int(2*(int(diff/5)+1)*random.uniform(1,5))
    monD = int(2*(int(diff/5)+1)*random.uniform(1,5))
    monMaxS = monS
    monMaxH = monH
    monDef = False
    enemyType = "Boss "+enemyType
  else:
    #SHARD = stamina, health, attack, recovery, defense
    monS = int((int(diff/5)+1)*random.uniform(1,5))
    monH = int(20*(int(diff/5)+1)*random.uniform(1,5))
    monA = int((int(diff/5)+1)*random.uniform(1,5))
    monR = int((int(diff/5)+1)*random.uniform(1,5))
    monD = int((int(diff/5)+1)*random.uniform(1,5))
    monMaxS = monS
    monMaxH = monH
    monDef = False
    #fight loop
  print("A "+enemyType+" appears before you!\n")
  while monH >0 and hp > 0 :
    stat(enemyType,monS,monH,monA,monR,monD,monMaxS,monMaxH)
    stat("Your",sp,hp,attack,recovery,defense,maxS,maxH)
    #we attack
    choice = input("\nDo you Wait, Attack, Recover, Defend, or Run?:")
    while choice != "wait" and choice != "attack" and choice != "recover" and choice != "defend" and choice != "run":
      print("input not understood")
      choice = input("wait,attack,recover,defend,run:")
    print
    if choice == "wait":
      print "You waited"
      pass
    elif choice == "attack":
      if sp > 0:
        if monD+2*monD*monDef >= attack:
          monH -= 1
          hp -= 5
          print "You attacked ... unsuccessfully"
        else:
          monH = monH - (attack-(monD+2*monD*monDef))
          print("You attacked successfully and dealt " +str(attack-(monD+2*monD*monDef))+" damage")
        sp = sp - 1
      else:
        print "You didn't have enough stamina to attack"
        hp -= 5
    elif choice == "defend":
      if sp > 0:
        defending = True
        print "You defended and will take "+str(defense*3)+" less damage"
        sp -= 1
      else:
        print "You didn't have enough stamina to defend"
        hp -= 5
    elif choice == "recover":
      sp = sp+int(recovery*3/10)
      hp = hp+recovery
      if sp > maxS:
        sp = maxS
      if hp > maxH:
        hp = maxH
      print "You recovered "+str(int(recovery*3/10))+" stamina and "+str(recovery)+" health"
    elif choice == "run":
      if random.random()*maxH<hp*0.75:
        print "You ran away"
        print
        continue
      else:
        print "You failed to run away"
        pass
    #attack end
    monDef = False
    print
    #mon attack
    if monH <= 0:
      break
    choice = random.randint(1,4)
    if choice == 1:
      print "The "+enemyType+" waited"
      pass
    elif choice == 2:
      if defense+2*defense*defending > monA:
        print "The "+enemyType+" attacked unsuccessfully"
        hp = hp - 1
        monH -= 5
      else:
        print "The "+enemyType+" attacked successfully and dealt "+monA+" damage"
        hp -= monA
    elif choice == 3:
      print "The "+enemyType+" defended and will take "+str(monD*3)+" less damage"
      monDef = True
    elif choice == 4:
      print "The "+enemyType+" recovered"
      monS = monS+int(monR*3/10)
      monH = monH+monR
      if monS > monMaxS:
        monS = monMaxS
      if monH > monMaxH:
        monH = monMaxH
    #after monster turn
    defending = False
  print("The fight is over now")
while True:
  fight(diff)
  diff += 1
  #between fights
  type = random.randint(0,2)
  quality = ["iron","steel","wrought iron","silver","gold","gilded","platinum","bejeweled","enchanted","magic","wooden","living"]
  weapons = ["sword","shortsword","longsword","daggers","knife","knives","spear","axe","halberd","staff"]
  accesories = ["amulet","ring","circlet","bracers","bracelet","earings","hoops","tiara","crown"]
  shields = ["shield","bulwark","skin","aura","wall","enchantment","defense"]
  
  if type == 0:
    inventory[0].append(random.choice(quality)+" "+random.choice(weapons)+": "+str(random.randint(1,3)*diff))
  elif type == 1:
    inventory[1].append(random.choice(quality)+" "+random.choice(accesories)+": "+str(random.randint(1,3)*diff))
  elif type == 2:
    inventory[2].append(random.choice(quality)+" "+random.choice(shields)+": "+str(random.randint(1,3)*diff))
  choice = input("\nDo you wish to rest, change equipment, or continue ahead?:")
  while choice != "continue" and choice != "change" and choice != "rest" and choice != "continue ahead" and choice != "change equipment":
    print("input not understood")
    choice = input("Do you wish to rest, change equipment, or continue ahead?:")
  if choice == "continue" or choice == "continue ahead":
    continue
  elif choice == "rest":
    sp = maxS
    hp = maxH
  elif choice == "change" or choice == "change equipment":
    #print "test"
    changeEquip()
  
