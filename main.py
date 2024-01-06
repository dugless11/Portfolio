import math
#file = open("prime.txt","a")
#print file.read()'
def primeTest(num):
  for i in range(2,int(math.sqrt(num))):
    if num%i == 0:
      return False
  return True
def findPrimes():
  prime = 2
  while True:
    if primeTest(prime):
      yield prime
    prime += 1
  """
  for i in primes:
    #print str(i) +" : "+ str(file.read().count("\n"+str(i)+"\n"))
    if file.read().count("\n"+str(i)+"\n")==0:
      file.write(str(i)+"\n")"""
def primeFac(number):
  fac = []
  if number == 1:
    return [number]
  elif number == 0:
    return None
  else:
    for i in findPrimes():
      if number%(int(i)) == 0:
        #print int(i)
        fac.append(int(i))
        #print int(number/int(i))
        #print "t1"
        #print primeFac(int(number/int(i)))
        #print "t2"
        fac = fac + primeFac(int(number/int(i)))
        break
      #else:
      #  if int(i)*int(i) > number:
          
  return fac
def formatPrimes(list):
  uniqueP = []
  numberP = []
  if list == None or list == [1]:
    print "No Factors"
  else:
    for i in list:
      if not(i in uniqueP):
        if not(i==1):
          uniqueP.append(i)
          numberP.append(list.count(i))
    for i in range(len(uniqueP)-1):
      print str(uniqueP[i]) + "^" +str(numberP[i])+" *",
    print str(uniqueP[-1])+"^"+str(numberP[-1])
  #print "\n"
def findFac(number):
  facList = []
  list = range(2,number+1)
  return [str(i) for i in filter(lambda x: number%x == 0,list)]
while True:
  i = int(input("Enter the number to prime factorize:"))
#print primeFac(i)
  formatPrimes(primeFac(i))
#print ', '.join(findFac(i))
#print file.readlines()