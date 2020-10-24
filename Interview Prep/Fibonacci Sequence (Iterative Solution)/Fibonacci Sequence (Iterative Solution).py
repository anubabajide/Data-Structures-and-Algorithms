def Fibonacci(val1,val2,stop):
    result=[]
    while stop>-1:
        result.append(val1)
        val2=val1+val2
        val1=val2-val1
        stop-=1
    return result

#Sample Test
#Fibonacci(0,1,10,[])   