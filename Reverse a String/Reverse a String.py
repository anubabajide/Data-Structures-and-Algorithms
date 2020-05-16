def reverse_string(str1):
    #define list of equal length
    n=len(str1)
    l = [0]*n
    
    #in the list, switch first and last items, second and second last, third and third last...
    for i in range(n//2):
        l[i] = str1[-(i+1)]
        l[-(i+1)] = str1[i]

    #replace middle item if string length is odd 
    if n%2==1:
        l[(n//2)]=str1[(n//2)]

    #convert list to string format
    return ''.join(l)
