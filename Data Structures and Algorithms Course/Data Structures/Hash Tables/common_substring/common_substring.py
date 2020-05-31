# python3

import sys, random
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

class Solver:
	_s_h_ = {}
	_t_h_ = {}
	_m1_ = 10 ** 9 + 7
	_m2_ = 10 ** 9 + 9
	_x_ = random.randint(1, 10**9)

	def __init__(self, s, t, mid):
		self.mid = mid
		self._s_h_ = {}
		self._t_h_ = {}
		s_h1 = self.precompute_hashes(s, len(s), self.mid, self._m1_, self._x_)
		s_h2 = self.precompute_hashes(s, len(s), self.mid, self._m2_, self._x_)
		t_h1 = self.precompute_hashes(t, len(t), self.mid, self._m1_, self._x_)
		t_h2 = self.precompute_hashes(t, len(t), self.mid, self._m2_, self._x_)
		for i, val in enumerate(zip(s_h1, s_h2)):
			self._s_h_[val[0]] = (val[1], i)
		for i, val in enumerate(zip(t_h1, t_h2)):
			self._t_h_[val[0]] = (val[1], i)

	def poly_hash(self, string, p, x):
		hash_value = 0
		for i in range(len(string)-1, -1, -1):
			hash_value = (((hash_value * x + ord(string[i])) % p) + p) % p
		return hash_value

	def precompute_hashes(self, text, t_len, pat_len, p, x):
		h = [0] * (t_len - pat_len +1)
		s = text[(t_len-pat_len):]
		h[t_len - pat_len] = self.poly_hash(s, p, x)
		y = pow(x, pat_len, p)
		for i in range(t_len - pat_len -1, -1, -1):
			h[i] = ((((x * h[i+1] + ord(text[i])) % p - (y * ord(text[i + pat_len]) % p)) % p) + p) % p
		return h

	def ask(self):
		for i in self._t_h_.keys():
			if i in self._s_h_:
				if self._t_h_[i][0] == self._s_h_[i][0]:
					return (True, Answer(self._s_h_[i][1], self._t_h_[i][1], self.mid))
		return (False, Answer(0, 0, self.mid))


def solve(s, t):
	ans = Answer(0, 0, 0)

	def check(s, t, mid):
		temp = Solver(s, t, mid)
		return temp.ask()


	l = 0
	r = min(len(s), len(t))
	while l<=r:
		mid = (l+r)//2
		temp2 = check(s, t, mid)
		if temp2[0]:
			ans = temp2[1]
			l = mid + 1
		else:
			r = mid - 1

	return ans

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
