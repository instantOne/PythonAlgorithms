import random

class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class CartesianTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        priority = random.randint(0, 1000000)
        node = Node(key, priority)
        if not self.root:
            self.root = node
            return
        curr = self.root
        parent = None
        while curr:
            if curr.key == key:
                return
            parent = curr
            if curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.__rebalance(node)

    def search(self, key, flag):
        curr = self.root
        while curr:
            if curr.key == key:
                return curr.key
            elif curr.key < key:
                curr = curr.right
            else:
                curr = curr.left
        if not flag:
            return self.__find_min_greater(key)
        else:
            return False

    def __find_min_greater(self, key):
        curr = self.root
        min_greater = None
        while curr:
            if curr.key > key:
                if not min_greater or curr.key < min_greater.key:
                    min_greater = curr
                curr = curr.left
            else:
                curr = curr.right
        if min_greater == None:
            return -1
        return min_greater.key

    def __rebalance(self, node):
        curr = node
        parent = None
        while curr:
            parent = curr
            if curr.left and curr.left.priority > curr.priority:
                curr = self.__rotate_right(curr)
            elif curr.right and curr.right.priority > curr.priority:
                curr = self.__rotate_left(curr)
            else:
                break
        if not parent:
            self.root = curr

    def __rotate_left(self, node):
        child = node.right
        node.right = child.left
        child.left = node
        return child

    def __rotate_right(self, node):
        child = node.left
        node.left = child.right
        child.right = node
        return child

a = CartesianTree()
n = int(input())
flag = False
for i in range(n):
    op, num = input().split(' ')
    num = int(num)
    if op == "+" and flag == True:
        if a.search((num + prev_result) % (10 ** 9), True) == False:
            a.insert((num + prev_result) % (10 ** 9))
        flag = False
    elif op == "+":
        if a.search(num, True) == False:
            a.insert(num)
    else:
        prev_result = a.search(num, False)
        print(prev_result)
        flag = True
