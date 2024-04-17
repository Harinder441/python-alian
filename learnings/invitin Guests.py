l=['ravi','deep','akash']
print(l)
#d= l.pop(1)
#l.remove('deep')
print(l)
l[1]='sahil'
#l.append('sahil')
print(l)
#. More Guests:
l.insert(0,'basant')
l.insert(2,'pooja')
l.append("deep")
print(l)
# i can invite only two people for dinner
r1=l.pop()
print("sorry "+r1)
r2=l.pop()
print("sorry "+r2)
r3=l.pop()
print("sorry "+r3)
r4=l.pop()
print("sorry "+r4)
print(l)
print("you are still invited " +l[0]+ " and " +l[1])
del l[0]
del l[0]
print(l)
#tuple vs list
t=('ravi','deep','akash')
for i in t:
    print(i)
#changing one element
#t[1]='pooja'  #this will give error
t=('ravi','pooja','akash')
