class TrieNode:

    def __init__(self):
        self.children = [None]*26

        self.isEndOfWord = False
        self.score = 1
        self.char = None

    def initializeScore(self):
        for i in range(26):
            child = self.children[i]
            if(child is not None):
                self.score += child.initializeScore()
        return self.score

    def traverse(self):
        print("current char and score: ", self.char, self.score)
        for i in range(26):
            child = self.children[i]
            if(child is not None):
                child.traverse()

class Trie:

    def __init__(self):
        self.root = self.createNode()

    def createNode(self):

        return TrieNode()

    def _charToIndex(self,ch):

        return ord(ch)-ord('a')


    def insert(self,key):

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.createNode()
                pCrawl.children[index].char = key[level]
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True

    def calculateScore(self, key):
        pCrawl = self.root
        length = len(key)
        score = 0
        for level in range(length):
            index = self._charToIndex(key[level])
            pCrawl = pCrawl.children[index]
            score += pCrawl.score
        return score


def solution():

    n = int(input().strip())
    keys = input().strip().split(" ")

    t = Trie()

    for key in keys:
        t.insert(key)

    t.root.initializeScore()

    solution = ""
    for key in keys:
        solution += str(t.calculateScore(key)) + " "
    print(solution)

solution()
