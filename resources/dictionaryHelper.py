import sys, pickle

DEFAULT_PICKLE_PATH = "resources/dictionary.pk"
DEFAULT_WORD_LIST = "resources/Collins Scrabble Words (2019).txt"

class Leaf():
	def __init__(self, word, isEnd=False):
		self.isWordEnd = isEnd
		self.word = word
		self.children = {}
	def addWord(self, word, wholeWord):
		if len(word) < 1:
			return
		firstLetter = word[0]
		if firstLetter in self.children:
			n = self.children[firstLetter]
		else:
			n = Leaf(wholeWord)
			self.children[firstLetter] = n
		if len(word) == 1:
			n.isWordEnd = True
		else:
			n.addWord(word[1:], wholeWord)

class DictTree():
	def __init__(self, words=[]):
		print("Initializing new dictionary")
		self.root = Leaf("")
		for word in words:
			self.root.addWord(word, word)

	def addWord(self, word):
		word = word.strip()
		self.root.addWord(word, word)

	def findAll(self, pool, root=None):
		if root is None:
			root = self.root
		words = []
		for c in pool:
			if c in root.children:
				if root.children[c].isWordEnd:
					words.append(root.children[c].word)
				if len(pool) > 1:
					words.extend(self.findAll(pool.replace(c, "", 1), root.children[c]))
		return words

def prepFromFile(filePath):
	fullDict = DictTree()
	with open(filePath, "r") as f:
		for line in f:
			word = line.strip()
			fullDict.addWord(word)
	return fullDict

def stash(picklePath, tree):
	with open(DEFAULT_PICKLE_PATH, 'wb') as f:
		pickle.dump(tree, f, pickle.HIGHEST_PROTOCOL)

def unstash(picklePath):
	with open(DEFAULT_PICKLE_PATH, 'rb') as f:
		return pickle.load(f)

def findAllFromDefaultDictionary(pool):
	try:
		tree = unstash(DEFAULT_PICKLE_PATH)
	except Exception as e:
		print(e)
		tree = prepFromFile(DEFAULT_WORD_LIST)
		stash(DEFAULT_PICKLE_PATH, tree) # for next time
	return tree.findAll(pool.upper())

if __name__ == "__main__":
	wordListPath = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_WORD_LIST
	picklePath = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_PICKLE_PATH
	tree = prepFromFile(wordListPath)
	stash(picklePath, tree)
