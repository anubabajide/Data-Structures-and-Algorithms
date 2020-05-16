def find_duplicates(s):
	#make all alphabets lower case and remove all spaces
	s=s.lower().split(" ") 
	seen =set()
	#iterate through list
	for i in s:
		#if item is in set, it is a duplicate
		if i in seen:
			result.append(i)
		#if item is not in set, add it to set
		else:
			seen.add(i)
	return result