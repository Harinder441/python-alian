'''class comp:
    def __init__(self,c,r):
        self.c=c
        self.r=r
    def cf(self):
        print("cf=",self.c,self.r)
c1=comp(1,2)
c1.cf()'''
'''import numpy as np
l1=[1,2,3]
l2=[2,3,5]
d=[]

for i in l1:
    for j in l2:
        diff = np.abs(i-j)
        d.append(diff)
        if min(d)==diff:
            l_d=diff
            x=i
            y=j
print(d)
print(l_d)
print(x,y)
print(min(d))'''

'''import numpy as np
l1=[1,2,3]
l2=[2,3,5]
d=[]

for i in range (0,len(l1)):
    diff = np.abs(l1[i]-l2[i])
    d.append(diff)
print(d)
print(min(d))
'''
