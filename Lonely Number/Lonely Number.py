def lonely_number(numbers):
	#change list to set
	seen=set()
	seen_twice=set()
	# loop through all items in list
	for i in numbers: 
		#if item is seen before
		if i in seen:
			no.add(i)
		#if item is seen again
		else: 
			yes.add(i)
	#items seen - items seen twice
	return list(yes-no)
