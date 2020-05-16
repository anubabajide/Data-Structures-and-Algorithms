def removeThree(s):
    stack=[]
    last=''
    def peek(stack):
        if len(stack)!=0:
            return stack[-1]
        else: 
            return None
        
    for i in range(len(s)):
        
        stack.append(s[i])
        if peek(stack) == last:
            stack.pop()
        else:
            last=None
        if len(stack)>2:
            if stack[-1]==stack[-2] and stack[-1]==stack[-3]:
                stack.pop()
                stack.pop()
                last=stack.pop()
    return (''.join(stack))

# Test Cases
# print(removeThree("baaabbbc"))
# print(removeThree("aabbbacd"))
# print(removeThree("aaabbbacd"))
# print(removeThree("baaabbbabbccccd"))
# print(removeThree("aabbccddeeedcbattaaatttab"))