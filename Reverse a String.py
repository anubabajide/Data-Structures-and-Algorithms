def reverse_string(str1):
	#string is immutable, change to list
	l = list(str1)
	
	#in the list, switch first and last items, second and second last, third and third last...
	for i in range((len(l)/2)):
		temp = l[i]
		l[i] = l[-(i+1)]
		l[-(i+1)] = temp
	
	#convert list to string format
	str1 = ''.join(l)
	return str1
