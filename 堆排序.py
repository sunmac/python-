# -*- coding: cp936 -*-
a=[31,41,59,26,41,58]
def parent(i):
    return i/2
def left(i):
    return 2*i
def right(i):
    return 2*i+1

def maxheap(a,i,heapsize):
    i=i
    l=left(i)
    r=right(i)
   # print i,l,r
    if l<=heapsize and a[l-1]>a[i-1]:
        largest=l
    else:
        largest=i
    if r<=heapsize and a[r-1]>a[largest-1]:
        largest=r

    if largest!=i:
        t=a[i-1]
        a[i-1]=a[largest-1]
        a[largest-1]=t
        maxheap(a,largest,heapsize)
def buildmaxheap(a):
    for i in xrange(len(a),0,-1):
        maxheap(a,i,len(a))

def heapsort(a):
    heapsize=len(a)
    buildmaxheap(a)
    for i in xrange(len(a)-1,0,-1):
     #   print i
        t=a[0]
        a[0]=a[i]
        a[i]=t
       # print t,a[0],a[i]

        heapsize=heapsize-1
        maxheap(a,1,heapsize)
        print a
def heapmaximum(a):
    return a[0]
def heapextractmax(a,heapsize):
    if heapsize<0:
        return 'error'
    max1=a[0]
    a[0]=a[heapsize]
    heapsize=heapsize-1
    maxheap(a,1,heapsize)
    return max1

def heapincreasekey(a,i,key):
    
    if key<a[i-1]:
        return  'error'
    a[i-1]=key
    print a,i
    while i>=0 and a[parent(i)-1]<a[i-1]:
        t=a[i-1]
        a[i-1]=a[parent(i)-1]
        a[parent(i)-1]=t
        i=parent(i)
        print a,i

def maxheapinsert(a,key,heapsize):
   heapsize=heapsize+1
   a.append(-1000)
   heapincreasekey(a,heapsize,key)

a=[16,14,10,8,7,9,3,2,4,1]
#b=[23,17,14,6,13,10,1,5,7,12]
#b=[16,4,10,14,7,9,3,2,8,1]
b=[4,1,3,2,16,9,10,14,8,7]
buildmaxheap(b)
print '123',b
#heapsort(b)

#print heapextractmax(b,len(b)-1)
#print b
#print heapincreasekey(b,9,15)
maxheapinsert(b,15,len(b))
print b
