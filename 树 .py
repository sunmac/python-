 # -*- coding: cp936 -*-
class tree(object):
    def __init__(self):
        self.root=node()
    def add(self,num,root1):
        if root1.elem==-1:
            root1.elem=num
            root1.rchild=node()
            root1.lchild=node()
            return
        else:
            if root1.rchild!=None:
                
                self.add(num,root1.rchild)
                return
            elif root1.lchild!=None:
                
                self.add(num,root1.lchild)
                return

    def printtree(self,a):
        if a.elem!=-1:
            print a.elem
        if a.rchild!=None :
            self.printtree(a.rchild)
           # print '右'
        if a.lchild!=None :
            self.printtree(a.lchild)
          #  print '左'
        return
    def searchtree(self,root1,key):
        if root1.elem==key:
            print key,r"搜索到"
        else:
            if root1.rchild!=None:
                self.searchtree(root1.rchild,key)
            if root1.lchild!=None:
                self.searchtree(root1.lchild,key)
    def lterativetreesearch(self,root1,key):
        while root1.elem!=-1 and root1.elem!=key:
            if root1.elem<key:
                root1=root1.rchild
            else:
                root1=root1.lchild
                
            root2=root1
       #     print root1.elem
        if root2.elem!=key:
             print  'sb'
        else:return root2
    def inserttree(self,t,num):
        y=None
        x=t.root
        while x.elem!=-1:
            y=x
           # print type(x)
            if num<x.elem  :
                
                x=x.lchild
                
            else:
                x=x.rchild


        if y==None:
            t.root.elem=num
            t.root.rchild=node()
            t.root.lchild=node()
        elif num<y.elem:

            y.lchild.elem=num
            x.lchild=node()
            x.rchild=node()
        else:

            y.rchild.elem=num
            x.lchild=node()
            x.rchild=node()
 #   def transplant(self,t,u,v):
   #     if u
    def deletetree(self,t,num):
        a=self.lterativetreesearch(self.root,num)

        if a.lchild.elem==-1:#看引用
            print a.elem
            a.elem=a.rchild.elem
            a.rchild=a.rchild.rchild
            print a.elem
        elif a.rchild.elem==-1:
          #  a=a.lchild
            a.elem=a.lchild.elem
            a.lchild=a.lchild.lchild
        else:
            parent=a
            min1=a.lchild
            while min1.lchild.elem!=-1:
                parent=min1
                min1=min1.lchild
            if a.lchild!=min1:
                parent.lchild=min1.rchild
            a.elem=min1.elem
            min1.elem=-1
       # print a.elem
            
                
            
            

class node(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild = lchild
        self.rchild = rchild  
    


a=tree()
#print type(a.root),a.root.elem

a.inserttree(a,12)

a.inserttree(a,5)

a.inserttree(a,18)

a.inserttree(a,2)

a.inserttree(a,9)

a.inserttree(a,15)

a.inserttree(a,19)

a.inserttree(a,13)
a.inserttree(a,17)

print 
a.printtree(a.root)
print 

a.deletetree(a,2)
print 
a.printtree(a.root)

