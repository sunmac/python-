# -*- coding: cp936 -*-

def findmaxcross(a,low,mid,high):
    leftsum=-1000
    sum1=0
    maxleft=-100
    for i in xrange(mid-1,low,-1):
        sum1=sum1+a[i]
        print i,sum1
        if sum1> leftsum:
            leftsum=sum1
            maxleft=i
        #    print leftsum
    rightsum=-1000
    sum1=0
    for i in xrange(mid,high):
        sum1=sum1+a[i]
        if sum1>rightsum:
            rightsum=sum1
            maxright=i

    return maxleft,maxright,leftsum+rightsum

a=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#print a
b,c,d=findmaxcross(a,0,int(len(a))/2,len(a))
print b,c,d
