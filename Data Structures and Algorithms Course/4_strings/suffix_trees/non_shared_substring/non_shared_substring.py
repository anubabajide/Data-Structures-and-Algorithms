# python3
import sys

sys.setrecursionlimit(4000)

def solve (p, q):
	global trie, result, text
	result = p
	text = p + '#' + q + '$'
	trie = {0:{}}
	node = 1
	n = len(text)
	for i in range(n):
		nex = 0
		j = i
		while j < n:
			match = sub_fin = text_fin = False
			for val in trie[nex]:
				length, point_to = trie[nex][val]
				pos = val
				if text[j] == text[pos]: 
					match = True
					cur = nex
					nex = point_to
					while text[j] == text[pos]:
						# Keep on checking matching characters till either
						# 1. there is a mismatch
						# 2. Text ends for either of the compared values
						j += 1
						pos += 1
						if (j >= n) or (pos >= length):
							if (j >= n):
								sub_fin = True
							if (pos >= length):
								text_fin = True
							break
					break
			if not match:
				trie[nex][j] = (n, node)
				trie[node] = {}
				node += 1
				break
			else:
				if not (sub_fin or text_fin):
					trie[cur][val] = (pos, node)
					trie[node] = {}
					trie[node][pos] = (length, nex)
					nex = node
					node += 1

	# print(trie)
	# {0:{'A':1,'T':2},1:{'C':3}}
	def unique(node, c, path):
		global result, trie, text
		# print(path)
		children = trie[node][c][1]
		if len(trie[children]) == 0:
			if ('#' in text[c:trie[node][c][0]]): 
				if (text[c] != '#'):
					result = path+text[c] if len(path+text[c]) < len(result) else result
				return True
			return False
		else:
			seen = True
			new_path = path+text[c:trie[node][c][0]]
			# print(path, new_path)
			for child in trie[children]:
				seen *= unique(children, child, new_path)
			if seen == 1:
				result = new_path if len(new_path) < len(result) else result
				return True
			return False

	for c in trie[0]:
		unique(0, c, '')
	return result

if __name__ == "__main__":
	p = sys.stdin.readline ().strip ()
	q = sys.stdin.readline ().strip ()

	ans = solve (p, q)
	sys.stdout.write (ans + '\n')
