def countOfAtoms(self, formula: str) -> str:
    # atoms(stores all elements and their occurences) stack(breaks string down into element and occurences)
    atoms = {'#':0}
    stack=[]
    result=''
    n=len(formula)
    
    # helper function to get last item in the stack
    def peek(stack):
        if stack:
            return stack[-1]
        else:
            return None
    
    #helper function to check if a string is a lowercase alphabet
    def lower(alpha):
        if alpha.lower()==alpha and alpha.isalpha():
            return True
        return False
        
    #First for loop writes all data to a list as individual strings 
    for i in range(n):
        #Condition 1: Alphabet
        if formula[i].isalpha():
            #check if there is a next item
            if i+1<n:
                #To handle two-lettered elements 
                if lower(formula[i+1]):
                    stack.append(formula[i]+formula[i+1])
                    #To append 1 to elements that have no number succeeding them
                    if i+2<=n-1:
                        if not formula[i+2].isnumeric():
                            stack.append('1')
                    else:
                        stack.append('1')
                    #write to dictionary
                    if (formula[i]+formula[i+1]) not in atoms:
                        atoms[formula[i]+formula[i+1]]=0
                #To handle single lettered elements
                elif not lower(formula[i]):
                    stack.append(formula[i])
                    #To append 1 to elements that have no number succeeding them
                    if i+1<=n-1:
                        if not formula[i+1].isnumeric():
                            stack.append('1')
                    else:
                        stack.append('1')
                    #write to dictionary
                    if formula[i] not in atoms:
                        atoms[formula[i]]=0
            else:
                #To handle single lettered elements
                if not lower(formula[i]):
                    stack.append(formula[i])
                    stack.append('1')
                    if formula[i] not in atoms:
                        atoms[formula[i]]=0
        
        #Condition 2: Number
        elif formula[i].isnumeric():
            #check for multi-valued numbers
            if peek(stack).isnumeric():
                stack.append(stack.pop() + formula[i])
            else:
                stack.append(formula[i])
        
        #Condition 3: Brackets
        else:
            stack.append(formula[i])
    
    #Second for loop breaks down all brackets by multiplying all numbers to individuals
    for i in range(len(stack)):
        #Check for number with bracket preceding
        if stack[i].isnumeric() and stack[i-1]==')':
            #store number, erase number and closing bracket
            num=int(stack[i])
            j=i-1
            stack[i]='#'
            stack[j]='#'
            #multiply every number inside bracket
            while stack[j]!='(':
                if stack[j].isnumeric():
                    stack[j]=str(num*int(stack[j]))
                j-=1
            #erase opening bracket
            stack[j]='#'
    
    #Third for loop adds all numbers for an element to value in dictionary 
    for i in range(len(stack)):
        #check for number
        if stack[i].isnumeric():
            num=int(stack[i])
            #add number
            if stack[i-1].isalpha():
                atoms[stack[i-1]]+=num
    
    #delete item for all erased brackets and numbers
    del atoms['#']
    
    #List comprehension to sort dictionary and store in correct format and sorted order
    result = ''.join([x[0]+str(x[1]) if x[1]>1 else x[0] for x in sorted(atoms.items())])
    return (result)