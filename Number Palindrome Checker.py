def threatDetector(textMessages):
    #helper function to generate count and score of palindromes
    def palindrome(j,n,string):
        #check for even palindromes
        start=j-2
        stop=j+1
        count=0
        score=0
        #condition for palindrome 'yxxy' is [0]=[3] and [1]=[2] and string is character(alphanumeric)
        while start>=0 and stop<n and string[start]==string[stop] and string[start].isalnum() and string[stop].isalnum():
            if stop-start+1>2:
                score+=stop-start+1
                count+=1
            start-=1
            stop+=1
        

        #check for odd palindromes
        start=j-1
        stop=j+1
        #condition for palindrome 'xyxyx' is [0]=[4] and [1]=[3] and string is character(alphanumeric)
        while start>=0 and stop<n and string[start]==string[stop] and string[start].isalnum() and string[stop].isalnum():
            if stop-start+1>2:
                score+=stop-start+1
                count+=1
            start-=1
            stop+=1
        return((count,score))
    
    #helper function to print output
    def give_output(count,score,l):
        if count>1:
            if 0<score<11:
                print(''.join(l), 'Possible')
            elif 10<score<41:
                print(''.join(l), 'Probable')
            elif 40<score<151:
                print(''.join(l), 'Escalate')
            else:
                print(''.join(l), 'Ignore')
        else:
            print(''.join(l), 'Ignore')




    #split string into appropriate parts
    message=[]
    symbol=[]
    for i in textMessages:
        message.append(''.join(i[:-2]))
        symbol.append(''.join(i[-3:]))

    #iterate through multiple messages
    for i in range(len(message)):
        #iterate through particular messsage
        n=len(message[i])
        count=0
        score=0
        for j in range(1,n-1):
            temp,temp2= palindrome(j,n,message[i])
            count+=temp
            score+=temp2
        give_output(count,score,symbol[i])
