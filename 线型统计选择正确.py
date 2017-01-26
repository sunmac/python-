# -*- coding: cp936 -*-
import random
def insert(a):
    for i in xrange(1,len(a)):
        key =a[i]
        j=i-1
        while j>-1 and a[j]>key:#改a【j】大于小于key就可以改升序降须
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
 
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
    b=[0 for i in xrange(5)]
    
    j=1
    jishuqi=0
    c=[]
    for i in xrange(p-1,r):
        if j%5==0:
            
            j=1
            insert(b)
            print b
            c.append(b[2])
            b=[0,0,0,0,0]
        j=j+1
        b[i%5]=a[i]
        
    
    insert(c)
   # print c,len(c),p,r,c[int((len(c)-1)/2)]
    t=c[int((len(c)-1)/2)]
    for i in xrange(p-1,r):
        if t==a[i]:
            break
    #print t
    a[i]=a[p]
    a[p]=t
   # print a
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
  #  print i
    return i


a=[0 for i in xrange(100)]
for i in xrange(100):
    a[i]=i
print a
#a=[1,2,3,4,5,6,7,8,9,10]
print randomselect(a,0,len(a)-1,5)
