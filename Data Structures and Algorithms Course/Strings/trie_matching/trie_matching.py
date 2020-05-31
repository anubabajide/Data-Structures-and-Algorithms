# python3
import sys

NA = -1

class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.endofword = False
		# self.word = ''
		
class Trie:
	def __init__(self):
		self.root = TrieNode()
		self.seen = set()
	
	def charToIndex(self, ch):
		return ord(ch)-ord('A')
	
	def insert(self, word):
		temp = self.root
		for val in word:
			index = self.charToIndex(val)
			if not temp.children[index]:
				temp.children[index] = TrieNode()
			temp = temp.children[index]
		temp.endofword = True
		# temp.word = word
	
	def search(self, text):
		self.seen.clear()
		for i in range(len(text)):
			j = i
			temp = self.root
			while j < len(text):
				index = self.charToIndex(text[j])
				if not temp.children[index]: 
					break
				if temp.children[index].endofword:
					self.seen.add(i)
					break
				temp = temp.children[index]
				j += 1
		return list(self.seen)
			
			
def solve (text, n, patterns):
	
	new_trie = Trie()
	for pattern in patterns:
		new_trie.insert(pattern)
	result = new_trie.search(text)
	result.sort()
	return result

if __name__ == "__main__":
	text = sys.stdin.readline ().strip ()
	n = int (sys.stdin.readline ().strip ())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline ().strip ()]

	ans = solve(text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
