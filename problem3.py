import sys
class TreeError(Exception):
    pass  # make it fancier if you want :)

class BinarySearchTree:
    class Node:
        def __init__(self,key=None):
            self.key = key
            self. parent = None
            self.child = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root=None
        self.size=0

    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def remove(self,T, z):
        z = self.search(T.root,z.key)
        if z == None:
            raise("TreeError")
        else:
            if z.left == None:
                T.transplant(z,z.right)
            elif z.right == None:
                T.transplant(z,z.left)
            else:
                y =T.min(z.right)
                if y.parent != z:
                    T.transplant(y,y.right)
                    y.right = z.right
                    y.right.parent = y
                T.transplant(z,y)
                y.left = z.left
                y.left.parent = y
            self.size-=1

    def min(self, x):
        if self.size == 0:
            raise("TreeError")
        else:
            while x.left != None:
                x = x.left
            return x

    def max(self,x):
        if self.size == 0:
            raise("TreeError")
        else:
            while x.right != None:
                x = x.right
            return x

    def search(self,x,k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inprint(self,x,p):
        if self.size == 0:
            raise("Empty")
        elif x != None:
            self.inprint(x.left,p)
            p.append(x.key)
            self.inprint(x.right,p)
        return p

    def preprint(self,x,p):
        if self.size == 0:
            raise("Empty")
        elif x != None:
            p.append(x.key)
            self.preprint(x.left,p)
            self.preprint(x.right,p)
        return p

    def postprint(self,x,p):
        if self.size == 0:
            raise("Empty")
        elif x != None:
            self.postprint(x.left,p)
            self.postprint(x.right,p)
            p.append(x.key)
        return p


    def insert(self,z):
        z = self.Node(z)
        y = None
        x = self.root
        while x != None:
            y=x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.size +=1


def driver():
    T = BinarySearchTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                T.insert(value)
            elif action == "remove":
                try:
                    node = T.Node(int(value_option[0]))
                    T.remove(T,node)
                except:
                    print("TreeError")
            elif action == "search":
                s = T.search(T.root, int(value_option[0]))
                if s != None:
                    print("Found")
                else:
                    print("Not Found")
            elif action == "max":
                try:
                    print(T.max(T.root).key)
                except:
                    print("Empty")
            elif action == "min":
                try:
                    print(T.min(T.root).key)
                except:
                    print("Empty")
            elif action == "preprint":
                try:
                    p = map(str, T.preprint(T.root,[]))
                    print(' '.join(p))
                except:
                    print("Empty")
            elif action == "inprint":
                try:
                    p = map(str, T.inprint(T.root,[]))
                    print(' '.join(p))
                except:
                    print("Empty")
            elif action == "postprint":
                try:
                    p = map(str, T.postprint(T.root,[]))
                    print(' '.join(p))
                except:
                    print("Empty")

# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
