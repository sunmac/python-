# -*- coding: cp936 -*-
#a=[31,41,59,26,41,58]
#a=[8,2,7,1,3,5,6,4]
import random
a=[4, 2, 7, 1, 3, 5, 6, 8]
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
def rapartition(a,p,r):
    i=random.randint(p,r)
    t=a[i]
    a[i]=a[p]
    a[p]=t
    return partition(a,p,r)

def raquicksort(a,p,r):
    if p<r :
        q=rapartition(a,p,r)
        print "zhong",a
    #    print p,q,'A',a[q]
       # print 'q',q
        raquicksort(a,p,q-1)
        raquicksort(a,q+1,r)



        
raquicksort(a,0,7)
print a
