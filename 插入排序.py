# -*- coding: cp936 -*-
a=[31,41,59,26,41,58]
for i in xrange(1,len(a)):
    key =a[i]
    j=i-1
    while j>-1 and a[j]>key:#��a��j������С��key�Ϳ��Ը�������
        a[j+1]=a[j]
        j=j-1
    a[j+1]=key
    print a
