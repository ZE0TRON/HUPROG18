import timeit

class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
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

    # Trie data structure class
    def __init__(self):
        self.root = self.createNode()

    def createNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self,ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)-ord('a')


    def insert(self,key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.createNode()
                pCrawl.children[index].char = key[level]
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
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


# driver function
def main():

    start = timeit.default_timer()


    # Input keys (use only 'a' through 'z' and lower case)
    #keys = ["arabalar", "araba", "ara", "arama", "alma", "al", "almak"]

    inputfile = open("/home/meric/PycharmProjects/strcore/input/input1.txt", "r")
    outfile = open("/home/meric/PycharmProjects/strcore/output/output1.txt", "w")
    n = int(inputfile.readline().strip())
    keys = inputfile.readline().strip().split(" ")

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    t.root.initializeScore()
    #t.root.traverse()

    for key in keys:
        print("current key:" ,key, "current score ", t.calculateScore(key))
        outfile.write(str(t.calculateScore(key)) + " ")


    stop = timeit.default_timer()
    print("Running time ", stop - start)

if __name__ == '__main__':
    main()
