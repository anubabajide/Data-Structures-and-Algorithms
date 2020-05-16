def Palindrome(n):
    #copy value of n
    t=n
    r=0
    #store each value of n in r in reverse order
    while n!=0:
        r=r*10
        r=r+(n%10)
        n=n//10
    #check if r is the same
    if r==t:
        return(True)
    return(False)