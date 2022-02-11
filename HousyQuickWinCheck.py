#insta win game, contiution of ticket
import random
'''i=0
a=[]
for x in range(1,101):
  t=random.randint(1,100)
  if t not in a:
    a.append(t)
    i+=1
  if i==15:
    break
a.sort()
i=0
b=[]
for x in range(1,101):
  t=random.randint(1,100)
  if t not in b:
    b.append(t)
    i+=1
  if i==15:
    break
b.sort()'''
c=[]
for x in range(500):
  t=random.randint(1,100)
  k=0
  for y in c:
    if(y==t):
      k=1
  if(k!=1):
    c.append(t)
    if t in b:
      b.remove(t)
    if t in a:
      a.remove(t)
  if len(a)==0:
    print("player1 wins")
    break
  if len(b)==0:
    print("player2 wins")
    break
