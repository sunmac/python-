# -*- coding: cp936 -*-
#c=[[0 for i in xrange(len(a))] for i in xrange(len(b))]
def squarematrix(a,b):
    n=int(len(a))
    c=[[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c
def squareplus(a,b):
    n=len(a)
    c=c=[[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            c[i][j]=a[i][j]+b[i][j]
    return c
def squareminus(a,b):
    n=len(a)
    c=c=[[0 for i in xrange(n)] for i in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            c[i][j]=a[i][j]-b[i][j]
    return c
def square(a,a1,a2,b,b1,b2):
    n=a2-a1+1
    s1=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s2=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s3=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s4=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s5=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s6=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s7=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s8=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s9=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    s10=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    a11=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            a11[i][j]=a[i][j]
    a21=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            a21[i][j]=a[i+a2/2][j]
    a22=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            a22[i][j]=a[i+a2/2][j+a2/2]
    a12=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            a12[i][j]=a[i][j+a2/2]
    b11=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            b11[i][j]=b[i][j]
    b21=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            b21[i][j]=b[i+a2/2][j]
    b22=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            b22[i][j]=b[i+a2/2][j+a2/2]
    b12=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    for i in xrange(n/2):
        for j in xrange(n/2):
            b12[i][j]=b[i][j+a2/2]
    s1=squareminus(b12,b22)
    s2=squareplus(a11,a12)
    s3=squareplus(a21,a22)
    s4=squareminus(b21,b11)
    s5=squareplus(a11,a22)
    s6=squareplus(b11,b22)
    s7=squareminus(a12,a22)
    s8=squareplus(b21,b22)
    s9=squareminus(a11,a21)
    s10=squareplus(b11,b12)
    p1=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p2=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p3=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p4=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p5=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p6=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
    p7=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
#    print n
    if n/2==1:
        c=[[0 for i in xrange(2)] for i in xrange(2)]
        s1=b[0][1]-b[1][1]
        s2=a[0][0]+a[0][1]
        s3=a[1][0]+a[1][1]
        s4=b[1][0]-b[0][0]
        s5=a[0][0]+a[1][1]
        s6=b[0][0]+b[1][1]
        s7=a[0][1]-a[1][1]
        s8=b[1][0]+b[1][1]
        s9=a[0][0]-a[1][0]
        s10=b[0][0]+b[0][1]
        p1=a[0][0]*s1
        p2=s2*b[1][1]
        p3=s3*b[0][0]
        p4=a[1][1]*s4
        p5=s5*s6
        p6=s7*s8
        p7=s9*s10
        c[a1-1][a1-1]=p5+p4-p2+p6
        c[a1-1][a2-1]=p1+p2
        c[a2-1][a1-1]=p3+p4
        c[a2-1][a2-1]=p5+p1-p3-p7
        return c
    else:
        p1=square(a11,1,n/2,s1,1,n/2)
        p2=square(s2,1,n/2,b22,1,n/2)
        p3=square(s3,1,n/2,b11,1,n/2)
        p4=square(a22,1,n/2,s4,1,n/2)
        p5=square(s5,1,n/2,s6,1,n/2)
        p6=square(s7,1,n/2,s8,1,n/2)
        p7=square(s9,1,n/2,s10,1,n/2)
        c11=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
        c12=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
        c21=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
        c22=[[0 for i in xrange(n/2)] for i in xrange(n/2)]
        c=[[0 for i in xrange(n)] for i in xrange(n)]
        c11=squareminus(squareplus(squareplus(p5,p6),p6),p2)
        c12=squareplus(p1,p2)
        c21=squareplus(p3,p4)
        c22=squareminus(squareplus(p5,p1),squareplus(p3,p7))
        for i in xrange(n/2):
            for j in xrange(n/2):
                c[i][j]=c11[i][j]
        for i in xrange(n/2):
            for j in xrange(n/2):
                c[i+n/2][j]=c12[i][j]
        for i in xrange(n/2):
            for j in xrange(n/2):
                c[i+n/2][j+n/2]=c22[i][j]
        for i in xrange(n/2):
            for j in xrange(n/2):
                c[i][j+n/2]=c21[i][j]
        return c
        

a=[[1,1],[1,1]]
b=[[1,1],[1,1]]
a=[[1,3],[7,5]]
b=[[6,8],[4,2]]
#c=square2(a,1,len(a),b,1,len(b))

#a=[[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
a=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
b=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
c=[[0 for i in xrange(6)]for i in xrange(6)]
a=[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
b=[[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
c=square(a,1,len(a),b,1,len(b))
print 
print c

