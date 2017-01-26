# -*- coding: cp936 -*-
import random
def randomselect(a,p,r,i):
    if p==r:
        return a[p]
    q=rapartition(a,p,r)
    k=q-p+1
    if i==k:
        return a[q]
    elif i<k:
        return randomselect(a,p,q-1,i)
    else:
        return randomselect(a,q+1,r,i-k)

def rapartition(a,p,r):
    i=random.randint(p,r)
    t=a[i]
    a[i]=a[p]
    a[p]=t
    return partition(a,p,r)
def partition(a,p,r):
    
    x=a[p]
  #  print p,r,x
    i=p
    for j in xrange(p+1,r+1):
        if a[j]<=x:
            i=i+1
            t=a[j]
            a[j]=a[i]
            a[i]=t
            
    t=a[i]
    a[i]=a[p]
    a[p]=t

    return i
a=[31,41,59,26,41,58]
print randomselect(a,0,len(a)-1,len(a))
