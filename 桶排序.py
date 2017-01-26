# -*- coding: cp936 -*-
def insert(a):
    for i in xrange(1,len(a)):
        key =a[i]
        j=i-1
        while j>-1 and a[j]>key:#改a【j】大于小于key就可以改升序降须
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    
def buckersort(a):
    n=len(a)#把桶建好，有多少个桶板才是主要的
    b=[[] for i in xrange(len(a))]
    for i in xrange(len(a)):

        b[int(10*a[i])].append(a[i])
    for i in xrange(len(a)):
        if len(b[i])>0:
            insert(b[i])

    c=[]
    for i in xrange(len(a)):
        for j in xrange(len(b[i])):
            if len(b[i])>0:
                c.append(b[i][j])

    for i in xrange(len(a)):
        a[i]=c[i]
    

a=[0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
buckersort(a)
print a

