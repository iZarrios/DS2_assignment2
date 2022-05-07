# data structure that represents a node in the tree
class Node():
    def __init__(self, data):  # inialize node
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1  # 1 for red & 0 for black


# Implements RBT
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

    def fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:  # Case 1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:  # Case 2
                        k = k.parent
                        self.rightRotate(k)
                    # Case 3
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
            else:  # Exchange right & left
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def searchTree(self, k):
        return self.search(self.root, k)

    def leftRotate(self, x):
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

    def rightRotate(self, x):
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
        node.color = 1  # Insert red node not black to maintain bh

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

        self.fixInsert(node)

    def getRoot(self):
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

# Print level order traversal of tree


def printLevelOrder(root, h):
    for i in range(1, h+1):
        printCurrentLevel(root, i)
# Print nodes at a current level


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)


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
        dictionary = dictf.read().splitlines()
        for key in dictionary:
            rbt.insert(key.lower())
        print(P+"\nLoaded Dictionary Successfully"+W)
    except:
        print(R+"\nCouldn't open dictionary\n"+W)
        exit(1)

    while True:
        print('\n----------Kindly, Choose from the follwing options----------\n')
        print("1 - Search\n2 - Insert\n3 - Tree Height\n4 - Tree Size\n5 - Show (Level order traversal)\n6 - Exit")
        choice = input("> ")
        if choice.lower() == 'search' or choice.lower() == "1":
            key = input("Search for Key: ").lower()
            if rbt.searchTree(key) == 0:
                print("YES")
            else:
                print("NO")
        elif choice.lower() == 'insert' or choice.lower() == "2":
            print("Tree Height before Insertion: {}".format(
                rbt.height(rbt.getRoot())))
            print("Tree Size before insertion: {}".format(
                rbt.size(rbt.getRoot())))
            key = input("Insert Key: ").lower()
            if rbt.searchTree(key) == 0:
                rbt.insert(key)

                print("{} Inserted!".format(key))
                print("Tree Height after Insertion: {}".format(
                    rbt.height(rbt.getRoot())))
                print("Tree Size after insertion: {}".format(
                    rbt.size(rbt.getRoot())))
            else:
                print("ERROR: Word already in the dictionary!")
        elif choice.lower() == 'tree height' or choice.lower() == "3":
            print("Tree Height: {}".format(rbt.height(rbt.getRoot())))
        elif choice.lower() == 'tree size' or choice.lower() == "4":
            print("Tree Size: {}".format(rbt.size(rbt.getRoot())))

        elif choice.lower() == 'show' or choice.lower() == "5":
            printLevelOrder(rbt.getRoot(), rbt.height(rbt.getRoot()))
            break

        elif choice.lower() == 'exit' or choice.lower() == "6":
            print("----------Terminating Program----------")
            break
        else:
            print("Not a Valid Choice!")
