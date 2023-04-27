import random

class Node:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(0, 10**9)
        self.l = None
        self.r = None
        self.size = 1

def add(tree, v):
    l, r = split(tree, v.x)
    return merge(merge(l, v), r)

def split(tree, x):
    if not tree:
        return None, None
    elif tree.x > x:
        l, tree.l = split(tree.l, x)
        r = tree
    else:
        tree.r, r = split(tree.r, x)
        l = tree
    new_size(tree)
    return l, r

def merge(l, r):
    if not l or not r:
        return l or r
    elif l.y > r.y:
        l.r = merge(l.r, r)
        new_size(l)
        return l
    else:
        r.l = merge(l, r.l)
        new_size(r)
        return r


def size(tree):
    return tree.size if tree else 0

def new_size(tree):
    if tree:
        tree.size = 1 + size(tree.l) + size(tree.r)


def find_max(tree, k):
    if not tree:
        return None
    leftsize = size(tree.l)
    if leftsize == k:
        return tree.x
    elif leftsize > k:
        return find_max(tree.l, k)
    else:
        return find_max(tree.r, k - leftsize - 1)


def remove(tree, x):
    if not tree:
        return None
    if tree.x == x:
        return merge(tree.l, tree.r)
    elif x < tree.x:
        tree.l = remove(tree.l, x)
    else:
        tree.r = remove(tree.r, x)
    new_size(tree)
    return tree


def print_full(tree):
    if not tree:
        return
    print_full(tree.l)
    print(f'({tree.x},{tree.size})\t', end='')
    print_full(tree.r)

if __name__ == '__main__':
    n = int(input())
    tree = None
    len = 0

    for i in range(n):
        operation, x = map(int, input().split())
        if operation == 1:
            node = Node(x)
            tree = add(tree, node)
            len += 1
        elif operation == 0:
            print(find_max(tree, len - x))
        elif operation == -1:
            tree = remove(tree, x)
            len -= 1
