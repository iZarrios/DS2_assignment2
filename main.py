import colored

# data structure that represents a node in the tree


class Node():
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 0 Black, 1 Red


# class RedBlackTree implements the operations in Red Black Tree
class RedBlackTree():
    def __init__(self):
        # rbt tree  begins with no nodes (TNULL  node)
        self.TNULL = Node(0)
        self.TNULL.color = 0  # black color as from the rules of RBTree is for the node to be black
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
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        return max(lheight, rheight) + 1

    def size(self, node):
        if node == self.TNULL:
            return 0
        return self.size(node.left) + self.size(node.right) + 1


if __name__ == "__main__":
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple

    rbt = RedBlackTree()

    try:
        dictf = open('EN-US-Dictionary.txt', 'r')
        print("Loaded Dictionary Successfully")
    except:
        print(R+"\nCouldn't open dictionary\n"+W)
        exit(1)

    dictionary = dictf.read()
    # print(dictionary)
    # exit(0)
    for key in dictionary:
        rbt.insert(key)
    while True:
        print("1-Search\n2-Insert\n3-Tree Height\n4-Tree Size\n5-Exit")
        choice = input("> ")
        if choice.lower() == 'search' or choice.lower() == "1":
            key = input("Search for Key: ")
            if key == '':
                continue
            if rbt.searchTree(key) == 0:
                print("NO")
            else:
                print("YES")
        elif choice.lower() == 'insert' or choice.lower() == "2":
            # print(f"Tree Height before Insertion: {rbt.height(rbt.get_root())}")
            # print(f"Tree Size before insertion: {rbt.size(rbt.get_root())}")
            key = input("Insert Key: ")
            if rbt.searchTree(key) == 0:
                rbt.insert(key)

                print(f"{key} Inserted!")
                # print("Tree Height after Insertion: {rbt.height(rbt.get_root())}")
                # print(f"Tree Size after insertion: {rbt.size(rbt.get_root())}")
            else:
                print("Word already Exists!")
        elif choice.lower() == 'tree height' or choice.lower() == "3":
            print(f"Tree Height: {rbt.height(rbt.get_root())}")
        elif choice.lower() == 'tree size' or choice.lower() == "4":
            print(f"Tree Size: {rbt.size(rbt.get_root())}")
            # ".format(rbt.size(rbt.get_root())))

        elif choice.lower() == 'exit' or choice.lower() == "5":
            print("------Terminating Program------")
            exit(0)
        else:
            print("Not a Valid Choice!")
