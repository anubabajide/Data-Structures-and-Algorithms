def find_duplicates(s):
	#make all alphabets lower case and remove all spaces
	s=s.lower().split(" ") 
	dupes =[]
	for i in range(len(s)):
		for j in range((i+1), len(s)):
			if l[i] == l[j]:
			dupes.append(l[i])
	return dupes
