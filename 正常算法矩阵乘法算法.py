# -*- coding: cp936 -*-
#import nampy
def squarematrix(a,b):
    n=int(len(a))
    c=[[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c
def square2(c,a,a1,a2,b,b1,b2):
    n=int(a2-a1+1)
    n2=int(b2-b1+1)
    if n==1:
        c[a1][a1]=a[a1][a1]*b[a1][a1]
        return c
    else:
        d1=square2(c,a,0,a1/2,b,0,b2/2)+square2(c,a,0,a1/2,b,1,b2)
        d2=square2(c,a,0,a1/2,b,1,b2)+square2(c,a,1,a1,b,1,b2)

    return d1+d2

a=[[1,1],[1,1]]
b=[[1,1],[1,1]]
a=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
b=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
a=[[1,3],[7,5]]
b=[[6,8],[4,2]]
#print a[0][0],len(a)
a=[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
b=[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
print '��ȷ',squarematrix(a,b)


