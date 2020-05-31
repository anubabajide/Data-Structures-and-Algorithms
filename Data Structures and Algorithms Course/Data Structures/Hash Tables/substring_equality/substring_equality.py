# python3

import sys, random

class Solver:
	_h1_ = []
	_h2_ = []
	_m1_ = 10 ** 9 + 7
	_m2_ = 10 ** 9 + 9
	_x_ = 256

	def __init__(self, s):
		self.s = s
		self._h1_ = self._poly_hash_(self._m1_, self._x_)
		self._h2_ = self._poly_hash_(self._m2_, self._x_)

	def ask(self, a, b, l):
		x_1 = pow(self._x_, l, self._m1_)
		x_2 = pow(self._x_, l, self._m2_)
		hash_a_1 = ((self._h1_[a+l] - x_1*(self._h1_[a])) + self._m1_) % self._m1_
		hash_b_1 = ((self._h1_[b+l] - x_1*(self._h1_[b])) + self._m1_) % self._m1_
		hash_a_2 = ((self._h2_[a+l] - x_2*(self._h2_[a])) + self._m1_) % self._m2_
		hash_b_2 = ((self._h2_[b+l] - x_2*(self._h2_[b])) + self._m1_) % self._m2_
		return ((hash_a_1 == hash_b_1) and (hash_a_2 == hash_b_2))

	def _poly_hash_(self, p, x):
		val_len = len(self.s)
		hash_value = [0] * (val_len +1)
		for i in range(1, val_len + 1):
			#hash_value[i] = (hash_value[i-1] + ((ord(self.s[i-1]) * x**(val_len-1-(i-1)))) % p) % p
			hash_value[i] = (x*hash_value[i-1] + ord(self.s[i-1])) % p
		return hash_value

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
