from QueuesLinked import QueuesLinked

class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, e, left, right):
        self._root = _Node(e,left._root,right._root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

    def preorder(self,troot):
        if troot:
            print(troot._element,end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x+y+1
        return 0



    def levelorder(self):
        Q = QueuesLinked()
        t = self._root
        print(t._element, end=" ")
        Q.enqueue(t)
        while not Q.isempty():
            t = Q.dequeue()
            if t._left:
                print(t._left._element, end=" ")
                Q.enqueue(t._left)
            if t._right:
                print(t._right._element, end=" ")
                Q.enqueue(t._right)


    def height(self,troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
x.maketree(40,a,a)
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,a)
s.maketree(30,r,y)
t.maketree(10,z,s)
print('Inorder Traversal')
t.inorder(t._root)
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print()
print('Levelorder Traversal')
t.levelorder()
print()
print('Height :-> ', t.height(t._root)-1)
print('count :-> ', t.count(t._root))

