# python3

import sys


class Solver:
	_t_h1_ = []
	_t_h2_ = []
	_p_h1_ = []
	_p_h2_ = []
	_m1_ = pow(10, 9) + 7
	_m2_ = pow(10, 9) + 9
	_x_ = 256

	def __init__(self, t, p):
		self.x_1 = [pow(self._x_, i, self._m1_) for i in range(len(p)+1)]
		self.x_2 = [pow(self._x_, i, self._m2_) for i in range(len(p)+1)]
		self._t_h1_ = self._poly_hash_(t, self._m1_, self._x_)
		self._t_h2_ = self._poly_hash_(t, self._m2_, self._x_)
		self._p_h1_ = self._poly_hash_(p, self._m1_, self._x_)
		self._p_h2_ = self._poly_hash_(p, self._m2_, self._x_)

	def ask(self, a, b, c):
		if a >= b:
			return True
		l = b - a

		hash_t_1 = ((self._t_h1_[b] - self.x_1[l]*(self._t_h1_[a])) + self._m1_) % self._m1_
		hash_t_2 = ((self._t_h2_[b] - self.x_2[l]*(self._t_h2_[a])) + self._m2_) % self._m2_
		hash_p_1 = ((self._p_h1_[l+c] - self.x_1[l]*(self._p_h1_[c])) + self._m1_) % self._m1_
		hash_p_2 = ((self._p_h2_[l+c] - self.x_2[l]*(self._p_h2_[c])) + self._m2_) % self._m2_
		return (hash_t_1 == hash_p_1) and (hash_t_2 == hash_p_2)

	def _poly_hash_(self, t, p, x):
		val_len = len(t)
		hash_value = [0] * (val_len +1)
		for i in range(1, val_len + 1):
			hash_value[i] = (x*hash_value[i-1] + ord(t[i-1])) % p
		return hash_value


def recurse(l, r, k, thresh, solver, c):
	if solver.ask(l,r,c):
		return thresh
	if l == r-1:
		return thresh + 1
	if thresh > k:
		return thresh
	mid = (l+r)//2
	thresh = recurse(l, mid, k, thresh, solver, c)
	if thresh > k:
		return thresh
	thresh = recurse(mid, r, k, thresh, solver, c+mid-l)
	return thresh


def solve(k, text, pattern):
	solver = Solver(text, pattern)
	result = []
	pat_len = len(pattern)
	for i in range(len(text) - pat_len +1):
		temp = recurse(i, i+pat_len, k, 0, solver, 0)
		if temp <= k:
			result.append(i)

	return result

for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
