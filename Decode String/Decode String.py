def decodeString(s):
    stack=[]
    word=''
    
    def peek(stack):
        if stack:
            return stack[-1]
        else:
            return None
        
    def digit(n):
        try:
            int(n)
            return True
        except:
            return False
    
    def alpha(a):
        if digit(i) is False and digit(peek(stack))is False and peek(stack)!='[':
            return True
        else: 
            return False
    for i in s:
        if i==']':
            word=stack.pop()
            stack.pop()
            word = int(stack.pop())*word
            if peek(stack) and peek(stack)!='[':
                stack.append(stack.pop()+word)
            else: 
                stack.append(word)
            continue

        elif alpha(i):
            if peek(stack):
                stack.append(stack.pop()+i)
            else: 
                stack.append(i)
            continue
            
        elif digit(i) and digit(peek(stack)):
            stack.append(stack.pop()+i)
            continue
        stack.append(i)

    return (''.join(stack))

#Test in Case 
#decompress('5[2[a3[bc]3[a]b]]')
#decompress('tryitout')
#decompress('10[a3[bc]3[a]b]')