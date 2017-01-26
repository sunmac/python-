# -*- coding: cp936 -*-
def findmaxcross(a,low,mid,high):
    leftsum=-1000
    sum1=0
    maxleft=0
    maxright=0
    for i in xrange(mid,low,-1):
        sum1=sum1+a[i] 
        if sum1> leftsum:
            leftsum=sum1
            maxleft=i
        
    rightsum=-1000
    sum1=0
    for i in xrange(mid+1,high):
        sum1=sum1+a[i]
        if sum1>rightsum:
            rightsum=sum1
            maxright=i
    print low,high
    return maxleft,maxright,leftsum+rightsum



def findmaxsub(a,low,high):
    crosslow,crosshigh,crosssum=0,0,0
    if high==low:
        return low,high,a[low]
    else:
        mid=(low+high)/2
        leftlow,lefthigh,leftsum=findmaxsub(a,low,mid)
        rightlow,righthigh,rightsum=findmaxsub(a,mid+1,high)
        crosslow,crosshigh,crosssum=findmaxcross(a,low,mid,high)
       # print crosslow,crosshigh,crosssum
        if leftsum>=rightsum and leftsum>=crosssum:
           # print '1左',leftlow,lefthigh,leftsum
           # print '1右',rightlow,righthigh,rightsum
           # print '返回',leftlow,lefthigh,leftsum
            return leftlow,lefthigh,leftsum
        elif rightsum>=leftsum and rightsum >=crosssum :
           # print '2左',leftlow,lefthigh,leftsum
           # print '2右',rightlow,righthigh,rightsum
           # print '返回',rightlow,righthigh,rightsum
            return rightlow,righthigh,rightsum
        else:
            #print '3',crosslow,crosshigh,crosssum
           # print leftlow,lefthigh,leftsum
           # print rightlow,righthigh,rightsum
            return crosslow,crosshigh,crosssum

    
a=[0,13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7,0]
a1=[0,13,-3,-25,20,-3]
print len(a)
c=findmaxsub(a,1,len(a)-1)
print c
#c=findmaxsub(a1,1,len(a1)-1)
#print c

