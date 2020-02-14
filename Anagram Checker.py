def anagram(s,t):
    one={}
    two={}
    for i in range(len(s)):
    	if s[i] in one:
    		one[s[i]]+=1
    	else:
    		one[s[i]]=1

    	if t[i] in two:
    		two[t[i]]+=1
    	else:
    		two[t[i]]=1
    
    if sum(two.values())!=len(t):
    	return False
    
    for i in one:
    	if one[i] != two[i]:
    		return False    
    
    return True

#Test Cases
#print(anagram("aanu","uans"))
#print(anagram("aanu","uana")) 