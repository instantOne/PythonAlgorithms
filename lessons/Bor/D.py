class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        node = self.root
        for char in key:
            index = int(char)
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

def find_infinite_sequence(node, path, forbidden):
    if node.is_end_of_word:
        return False

    if len(path) > len(max(forbidden, key=len)):
        return True

    for i in range(2):
        if node.children[i]:
            path.append(i)
            if find_infinite_sequence(node.children[i], path, forbidden):
                return True
            path.pop()

    return False

def main():
    n = int(input())
    forbidden = [input() for _ in range(n)]

    trie = Trie()
    for f in forbidden:
        trie.insert(f)

    if find_infinite_sequence(trie.root, [], forbidden):
        print("TAK")
    else:
        print("NIE")

if __name__ == "__main__":
    main()
