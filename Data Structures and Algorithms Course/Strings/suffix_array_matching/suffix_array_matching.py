# python3
import sys

class Suffix_Array:
	def __init__(self, S):
		self.S = S
		self.n = len(self.S)

	def sort_characters(self):
		"""
		Take a String consisting of A, C, G, T character and one $ only
		Return the stable sort of the string as an array where
		array[i] = index of (i+1)-th letter in order
		"""
		self.order = [0] * self.n
		count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}

		for i in range(self.n):
			count[self.S[i]] += 1

		prev = None
		for j in count:
			if prev:
				count[j] += count[prev]
			prev = j

		for i in range(self.n-1, -1, -1):
			c = self.S[i]
			count[c] -= 1
			self.order[count[c]] = i

	def compute_char_classes(self):
		"""
		Take a String and its sorted order
		classify each character and return the class where
		char_class[i] = class of character S[i]
		two characters are in the same class iff they are the same
		"""
		self.char_class = [0] * self.n

		for i in range(1, self.n):
			if self.S[self.order[i]] != self.S[self.order[i-1]]:
				self.char_class[self.order[i]] = self.char_class[self.order[i-1]] + 1
			else:
				self.char_class[self.order[i]] = self.char_class[self.order[i-1]]

	def sort_doubled(self, L):
		"""
		sort the doubled suffixes of a string S and return the order

		args
		String - S,
		length of suffix - L,
		sorted order of suffixes of length L - order,
		character class of each suffix of length L - char_class

		return
		the new order of sorted suffixes of length 2L - newOrder
		"""

		count = [0] * self.n
		newOrder = [0] * self.n

		for i in range(self.n):
			count[self.char_class[i]] += 1

		for j in range(1, self.n):
			count[j] += count[j-1]

		for i in range(self.n-1, -1, -1):
			start = (self.order[i] - L + self.n) % self.n  # Get position of next suffix character in cyclic shift of length 2L
			cl = self.char_class[start]
			count[cl] -= 1
			newOrder[count[cl]] = start

		self.order = newOrder

	def update_classes(self, L):
		"""
		Update the classes of sorted suffixes of length 2L and return
		updated order

		args
		order of sorted suffixes of length 2L - newOrder
		character class of each suffix of length L - char_class
		length of suffix - L
		"""
		n = self.n
		newClass = [0] * n

		for i in range(1, n):
			cur = self.order[i]
			prev = self.order[i-1]
			mid = (cur + L) % n
			mid_prev = (prev + L) % n
			if (self.char_class[cur] != self.char_class[prev]) or (self.char_class[mid] != self.char_class[mid_prev]):
				newClass[cur] = newClass[prev] + 1
			else:
				newClass[cur] = newClass[prev]

		self.char_class = newClass


	def build_suffix_array(self):
		"""
		Build suffix array of the string text and
		return a list result of the same length as the text
		such that the value result[i] is the index (0-based)
		in text where the i-th lexicographically smallest
		suffix of text starts.
		"""
		self.sort_characters()
		self.compute_char_classes()
		L = 1

		while L < self.n:
			self.sort_doubled(L)
			self.update_classes(L)
			L *= 2

		return self.order


class BWT:
	def __init__(self, suffix_array, S):
		self.suffix_array = suffix_array
		self.S = S
		self.n = len(S)
		self.build_bwt()
		self.PreprocessBWT()
		
	def build_bwt(self):
		self.bwt = ''
		self.starts = {}

		for i in range(len(self.suffix_array)):
			self.bwt += self.S[self.suffix_array[i]-1]
			if self.S[self.suffix_array[i]] not in self.starts:
				self.starts[self.S[self.suffix_array[i]]] = i

	def PreprocessBWT(self):
		"""
		Preprocess the Burrows-Wheeler Transform bwt of some text
		and compute as a result:
			* starts - for each character C in bwt, starts[C] is the first position
				of this character in the sorted array of
				all characters of the text.
			* occ_count_before - for each character C in bwt and each position P in bwt,
				occ_count_before[C][P] is the number of occurrences of character C in bwt
				from position 0 to position P inclusive.
		"""
		 
		self.occ_counts_before = {c:[0]*(self.n + 1) for c in self.starts}

		for i in range(self.n):
			self.occ_counts_before[self.bwt[i]][i+1] += 1

		for c in self.occ_counts_before:
			for i in range(2, len(self.occ_counts_before[c])):
				self.occ_counts_before[c][i] += self.occ_counts_before[c][i-1]


	def CountOccurrences(self, pattern):
		"""
		Compute the number of occurrences of string pattern in the text
		given only Burrows-Wheeler Transform bwt of the text and additional
		information we get from the preprocessing stage - starts and occ_counts_before.
		"""
		top = 0
		bottom = self.n - 1
		pattern = list(pattern)
		while top <= bottom:
			if pattern:
				symbol = pattern.pop()
				if symbol in self.bwt[top:bottom+1]:
					top = self.starts[symbol] + self.occ_counts_before[symbol][top]
					bottom = self.starts[symbol] + self.occ_counts_before[symbol][bottom+1] - 1
				else:
					return []
			
			else:
				return [self.suffix_array[i] for i in range(top, bottom + 1)]
		return []


def find_occurrences(text, patterns):
	occs = set()

	S = text + '$'
	# Generate Suffix Array
	suffix_array = Suffix_Array(S).build_suffix_array()
	
	# Generate BWT from Suffix Array 
	# # Generate starts and occurences of count before array from BWt
	bwt = BWT(suffix_array, S)
	
	# Use Info to count occurences
	for pattern in patterns:
		occs.update(bwt.CountOccurrences(pattern))

	return occs

if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	pattern_count = int(sys.stdin.readline().strip())
	patterns = sys.stdin.readline().strip().split()
	occs = find_occurrences(text, patterns)
	print(" ".join(map(str, occs)))