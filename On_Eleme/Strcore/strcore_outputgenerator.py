import timeit
import os

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


def main():

    timefile = open("/home/meric/PycharmProjects/strcore/runtimes.txt", "w")

    inputs = os.listdir("./input")
    for inp in inputs:
        start = timeit.default_timer()
        inputfile = open("/home/meric/PycharmProjects/strcore/input/" + inp, "r")
        number = inp[5:]
        outfile = open("/home/meric/PycharmProjects/strcore/output/output" + number, "w+")

        n = int(inputfile.readline().strip())
        keys = inputfile.readline().strip().split(" ")

        t = Trie()

        for key in keys:
            t.insert(key)

        t.root.initializeScore()

        for key in keys:
            print("current key:" ,key, "current score ", t.calculateScore(key))
            outfile.write(str(t.calculateScore(key)) + " ")


        stop = timeit.default_timer()
        print("Running time of" + number + "th input", stop - start, "\n", file=timefile)

if __name__ == '__main__':
    main()
