# -*- coding: cp936 -*-
def stablesort(a,d,r):
    b=[]
    for i in xrange(r):
        for j in xrange(len(a)):
            c=a[j]%d/(d/10)
            if c==i:
                b.append(a[j])
    for j in xrange(len(b)):
        a[j]=b[j]

def padixsort(a,d):
    for i in xrange(1,d+1):
        r=10  #r=lg d 时，时间复杂度最低
        stablesort(a,pow(10,i),r)
        
a=[329,457,657,839,436,720,355,297]
padixsort(a,3)
print a


