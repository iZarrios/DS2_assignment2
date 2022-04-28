import colored

# data structure that represents a node in the tree


class Node():
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def search(self, node, key):
        if node == self.TNULL or key == node.data:
            return node.data

        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def searchTree(self, k):
        return self.search(self.root, k)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return
        self.fix_insert(node)

    def get_root(self):
        return self.root

    def height(self, node):
        if node == self.TNULL:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def size(self, node):
        if node == self.TNULL:
            return 0
        else:
            return self.size(node.left) + self.size(node.right) + 1


if __name__ == "__main__":

    rbt = RedBlackTree()

    try:
        dictf = open('EN-US-Dictionary.txtr', 'r')
    except:
        print("Couldn't open dictionary")
        exit(1)

    dictionary = dictf.read().splitlines()
    for key in dictionary:
        rbt.insert(key)
    while True:
        print("1-Search\n2-Insert\n3-Tree Height\n4-Tree Size\n5-Exit")
        choice = input(">")
        if choice.lower() == 'search':
            key = input("Search for Key: ")
            if rbt.searchTree(key) == 0:
                print("Not Found!")
            else:
                print("Found!")
        elif choice.lower() == 'insert':
            print("Tree Height before Insertion: {}".format(
                rbt.height(rbt.get_root())))
            print("Tree Size before insertion: {}".format(
                rbt.size(rbt.get_root())))
            key = input("Insert Key: ")
            if rbt.searchTree(key) == 0:
                rbt.insert(key)

                print("{} Inserted!".format(key))
                print("Tree Height after Insertion: {}".format(
                    rbt.height(rbt.get_root())))
                print("Tree Size after insertion: {}".format(
                    rbt.size(rbt.get_root())))
            else:
                print("ERROR: Word already in the dictionary!")
        elif choice.lower() == 'tree height':
            print("Tree Height: {}".format(rbt.height(rbt.get_root())))
        elif choice.lower() == 'tree size':
            print("Tree Size: {}".format(rbt.size(rbt.get_root())))

        elif choice.lower() == 'exit':
            print("------Terminating Program------")
            break
        else:
            print("Not a Valid Choice!")
