# python3
import sys

class Suffix_Array:
	def __init__(self, S):
		self.S = S
		self.n = len(self.S)

	def sort_characters(self):
		self.order = [0] * self.n
		count = [0] * 5
		index = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}

		for i in range(self.n):
			count[index[self.S[i]]] += 1

		for j in range(1, len(count)):
			count[j] += count[j-1]
			
		for i in range(self.n-1, -1, -1):
			c = self.S[i]
			count[index[c]] -= 1
			self.order[count[index[c]]] = i

	def compute_char_classes(self):
		self.char_class = [0] * self.n

		for i in range(1, self.n):
			if self.S[self.order[i]] != self.S[self.order[i-1]]:
				self.char_class[self.order[i]] = self.char_class[self.order[i-1]] + 1
			else:
				self.char_class[self.order[i]] = self.char_class[self.order[i-1]]

	def sort_doubled(self, L):
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
		self.sort_characters()
		self.compute_char_classes()
		L = 1

		while L < self.n:
			self.sort_doubled(L)
			self.update_classes(L)
			L = (2*L)

		return self.order


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	print(" ".join(map(str, Suffix_Array(text).build_suffix_array())))
