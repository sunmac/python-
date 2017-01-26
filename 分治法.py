# -*- coding: cp936 -*-
def merge(a,p,q,r1):
    n1=q
    n2=len(a)
    r=[]
    l=[]
    for i in xrange(0,n1):
        l.append(a[i])
    for j in xrange(i+1,n2):
        r.append(a[j])
    l.append(1000)
    r.append(1000)
    i=0
    j=0
    print l,r
    for k in xrange(0,len(a)):
        if l[i]<=r[j]:
            a[k]=l[i]
            i=i+1
        else:
            a[k]=r[j]
            j=j+1
    return a
a=[2,4,5,7,1,2,3,6]
a=merge(a,8,4,8)
print a
