 # -*- coding: cp936 -*-
class tree(object):
    def __init__(self):
        self.root=node()
        self.nil=node()
        self.root.rchild=self.nil
        self.root.lchild=self.nil
        self.nil.color='black'

    def printtree(self,a):
        if a.elem!=-1:
            print a.elem,a.color
        if a.rchild!=None :
            self.printtree(a.rchild)
           # print '右'
        if a.lchild!=None :
            self.printtree(a.lchild)
          #  print '左'
        return

    def lterativetreesearch(self,root1,key):
        while root1.elem!=-1 and root1.elem!=key:
            if root1.elem<key:
                root1=root1.rchild
            else:
                root1=root1.lchild
                
            root2=root1
       #     print root1.elem
        if root1.elem==key:
            root2=root1
        if root2.elem!=key:
             print key, '找不到'
        else:return root2

    def parent(self,root1,key):
        if root1.elem==key:
            a=-1
          #  print a
            return self.nil
        while root1.elem!=-1 and root1.elem!=key:
            if root1.elem<key:
                proot=root1
                root1=root1.rchild
            else:
                proot=root1
                root1=root1.lchild
            
            root2=root1
       #     print root1.elem
        if root1.elem==key:
            root2=root1
        if root2.elem!=key:
             print  key,'找不到父母'
        else:return proot
        

    def leftrotate(self,t,num):
        x=self.lterativetreesearch(self.root,num)
        xparent=self.parent(self.root,num)
        y=x.rchild
        yparent=self.parent(self.root,y.elem)
        x.rchild=y.lchild
        if y.lchild!=t.nil:
            ylparent=self.parent(self.root,y.lchild.elem)
            ylparent=x
        
        yparent=xparent
        if xparent==t.nil:
            t.root=y
        elif x==xparent.lchild:
            xparent.lchild=y
        else:
            xparent.rchild=y
        y.lchild=x
        xparent=y
    def rightrotate(self,t,num):
        x=self.lterativetreesearch(self.root,num)#明天改
        xparent=self.parent(self.root,num)
        y=x.lchild
        yparent=self.parent(self.root,y.elem)
        x.lchild=y.rchild
        if y.rchild!=t.nil:
            yrparent=self.parent(self.root,y.rchild.elem)
            yrparent=x
        
        yparent=xparent
        if xparent==t.nil:
            t.root=y
        elif x==xparent.rchild:
            xparent.rchild=y
        else:
            xparent.lchild=y
        y.rchild=x
        xparent=y
    def rbinsert(self,t,key):
        y=t.nil
        x=t.root
        if t.root.elem==-1:
            t.root.elem=key
            t.root.color='black'
            return
        while x!=t.nil:
            y=x
            if key<x.elem:
                x=x.lchild
            else :
                x=x.rchild
            
        if y.elem>key:
            y.lchild=node()
            y.lchild.elem=key
            y.lchild.rchild,y.lchild.lchild=t.nil,t.nil
            y.lchild.color='red'
        else:
            y.rchild=node()
            y.rchild.elem=key
            y.rchild.rchild,y.rchild.lchild=t.nil,t.nil
            y.rchild.color='red'
        if y==t.nil:
            t.root.elem=key
            t.root.lchild,t.root.rchild=t.nil


        t.rbinsertfixup(t,key)
    def rbinsertfixup(self,t,key):
        aparent=t.parent(t.root,key)
        a=self.lterativetreesearch(t.root,key)
        preaparent=self.parent(t.root,aparent.elem)
        while aparent.color=='red':            
            a=self.lterativetreesearch(t.root,a.elem)
            aparent=t.parent(t.root,a.elem)
            preaparent=self.parent(t.root,aparent.elem)
            if aparent==preaparent.lchild:
                y=preaparent.rchild
                if y.color == 'red':
                    aparent.color='black'
                    y.color='black'
                    preaparent.color='red'
                    a=preaparent
                                      
                else:
                    if a==aparent.rchild:
                        a=aparent
                        self.leftrotate(self,a.elem)
                    aparent=t.parent(t.root,a.elem)
                    preaparent=self.parent(t.root,aparent.elem)                       
                    aparent.color='black'
                    preaparent.color='red'
                    self.rightrotate(self,preaparent.elem)
            else:
                if aparent==preaparent.rchild:
                    y=preaparent.lchild
                    if y.color == 'red':
                        aparent.color='black'
                        y.color='black'
                        preaparent.color='red'
                        a=preaparent
                    else:
                        if a==aparent.lchild:
                            a=aparent
                            aparent=t.parent(t.root,a.elem)
                            preaparent=self.parent(t.root,aparent.elem)
                            self.rightrotate(self,a.elem)
                        aparent.color='black'
                        preaparent.color='red'
                        self.leftrotate(t,preaparent.elem)
            aparent=t.parent(t.root,a.elem)
            

        t.root.color='black'
    def treemin(self,x):
        x=self.lterativetreesearch(self.root,x)
        while x.lchild!=self.nil:
            x=x.lchild
        return x
    def rbtransplant(self,t,ukey,vkey):
        uparent=self.parent(self.root,ukey)
        vparent=self.parent(self.root,vkey)
        u=self.lterativetreesearch(self.root,ukey)
        v=self.lterativetreesearch(self.root,vkey)
        if uparent==t.nil:
            t.root=v
        elif u==uparent.lchild:
            uparent.lchild=v
        else:
            uparent.rchild=v
        vparent=uparent
    def rbdelete(self,t,z):
        z=self.lterativetreesearch(t.root,z)
        y=z
        yoriginalcolor=y.color
        if z.lchild==t.nil:
            x=z.rchild
            self.rbtransplant(t,z.elem,z.rchild.elem)
        elif z.rchild==t.nil:
            x=z.lchild
            self.rbtransplant(t,z.elem,z.lchild.elem)
        else:
            y=self.treemin(z.rchild.elem)
            yoriginalcolor=y.color
            x=y.rchild
            yparent=self.parent(t.root,y.elem)
            if yparent==z:
                xparent=self.parent(t.root,x.elem)
                xparent=y
            else:
                print t.root,y.elem,y.rchild.elem#
                self.printtree(self.root)
                self.rbtransplant(self,y.elem,y.rchild.elem)#
                print
                self.printtree(self.root)
                y.rchild=z.rchild
                yrchildparent=self.parent(self.root,y.rchild.elem)
                print 's3',y.elem,yrchildparent,self.root
                yrchildparent.elem=y.elem
                yrchildparent.color=y.color
                yrchildparent.rchild=y.rchild
                #yrchildparent.lchild=y.lchild
       
            self.rbtransplant(self,z.elem,y.elem)
            y.lchild=z.lchild
        #    print self.root
            ylchildparent=self.parent(t.root,y.lchild.elem)
     #       print ylchildparent
            ylchildparent=y
        if yoriginalcolor=='black':
            self.printtree(self.root)
    def rbdeletefixpu(self,t,x):
        while x!=self.root and x.color=='black':
            xparent=self.parent(t.root,x.elem)
            if x==xparent.lchild:
                w=xparent.rchild

                if w.color=='red':
                    w.color='black'
                    xparent.color='red'
                    self.leftrotate(t,xparent.elem)
                    w=xparent.rchild
                if w.lchild.color=='black' and w.rchild.color=='black':
                    w.color='red'
                    x=xparent
                else:
                    if w.rchild.color=='black':
                        w.lchild.color='black'
                        w.color='red'
                        self.rightrotate(t,w.elem)
                        w=xparent.rchild
                    w.color=xparent.color
                    xparent.color='black'
                    w.rchild.color='black'
                    self.leftrotate(t,xparent.elem)
                    x=t.root
            else:
                w=xparent.lchild
                if w.color=='red':
                    w.color='black'
                    xparent.color='red'
                    self.rightrotate(t,xparent.elem)
                    w=xparent.lchild
                if w.rchild.color=='black' and w.lchild.color=='black':
                    w.color='red'
                    x=xparent
                else:
                    if w.lchild.color=='black':
                        w.rchild.color='black'
                        w.color='red'
                        self.leftrotate(t,w.elem)
                        w=xparent.lchild
                    w.color=xparent.color
                    xparent.color='black'
                    w.lchild.color='black'
                    self.rightrotate(t,xparent.elem)
                    x=t.root
                
            
                
class node(object):
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem=elem
        self.lchild = lchild
        self.rchild = rchild
        self.color=''
    


a=tree()
#print type(a.root),a.root.elem
a.rbinsert(a,11)
a.rbinsert(a,2)
a.rbinsert(a,14)

a.rbinsert(a,1)

a.rbinsert(a,7)
a.rbinsert(a,15)
a.rbinsert(a,8)
a.rbinsert(a,5)
a.rbinsert(a,4)
a.printtree(a.root)
print 
a.rbdelete(a,7)
print
a.printtree(a.root)
print



