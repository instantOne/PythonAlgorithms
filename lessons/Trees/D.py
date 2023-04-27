import random


class Treap:
    class TreapNode:
        def __init__(self, key):
            self.key = key
            self.priority = random.randint(0, 1000000000)
            self.left = None
            self.right = None
            self.keysSum = key

    def __init__(self):
        self.root = None

    def update(self, node):
        if not node:
            return
        node.keysSum = node.key + self.get_keys_sum(node.left) + self.get_keys_sum(node.right)

    def insert(self, key):
        less, greater = self.split(self.root, key)
        equal, greater = self.split(greater, key + 1)
        if not equal:
            equal = self.TreapNode(key)
        self.root = self.merge(less, self.merge(equal, greater))

    def merge(self, a, b):
        if not a or not b:
            return a if a else b
        if a.priority > b.priority:
            a.right = self.merge(a.right, b)
            self.update(a)
            return a
        else:
            b.left = self.merge(a, b.left)
            self.update(b)
            return b

    def split(self, t, split_key):
        if not t:
            return None, None
        if t.key < split_key:
            a, b = self.split(t.right, split_key)
            t.right = a
            self.update(t)
            return t, b
        else:
            a, b = self.split(t.left, split_key)
            t.left = b
            self.update(t)
            return a, t



    def get_keys_sum(self, node):
        if node:
            return node.keysSum
        else:
            return 0

    def keysSum(self, keyL, keyR):
        less, greater = self.split(self.root, keyL)
        t_in, greater = self.split(greater, keyR + 1)
        result = self.get_keys_sum(t_in)
        self.root = self.merge(less, self.merge(t_in, greater))
        return result


treap = Treap()

queriesCount = int(input())
previous_result = 0
flag = False
for i in range(queriesCount):
    queryType, *queryArgs = input().split()
    if queryType == '+':
        key = int(queryArgs[0])
        treap.insert((key + previous_result) % int(10 ** 9))
        flag = False
        previous_result = 0
    else:
        keyL, keyR = map(int, queryArgs)
        previous_result = treap.keysSum(keyL, keyR)
        print(previous_result)
        flag = True
