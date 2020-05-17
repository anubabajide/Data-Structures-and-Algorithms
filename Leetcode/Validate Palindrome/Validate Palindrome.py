def is_palindrome(s):
	#Remove whitespaces, convert to lower case, and store in two lists
	l = x = list("".join(s.split()).lower())
	#reverse one of the lists
	for i in range((len(l)/2)):
		temp = l[i]
		l[i] = l[-(i+1)]
		l[-(i+1)] = temp
	#check if two lists are identical
	if x == l:
		return True
	else:
		return False
