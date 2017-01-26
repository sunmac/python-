# -*- coding: cp936 -*-


def countingsort(a,b):
    k=-100
    for i in xrange(len(a)):
        if k<a[i]:
            k=a[i]
    c=[0 for i in xrange(k+1)]

    for j in xrange(len(a)):

        c[a[j]]=c[a[j]]+1

    for i in xrange(k+1):
        if(i>0):
            c[i]=c[i]+c[i-1]
    print c,a
    for j in xrange(len(a)-1,-1,-1):
        print j,a[j],c[a[j]]
        b[c[a[j]]-1]=a[j]
        c[a[j]]=c[a[j]]-1
        print b,c
        



a=[4, 2, 7, 1, 3, 5, 6, 8]
b=[0 for i in xrange(len(a))]
print len(a)
countingsort(a,b)
print b


