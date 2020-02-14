def Fibonacci(val1, val2, stop, result):
    result.append(val1)
    if stop>0:
        Fibonacci(val2,val1+val2,stop-1,result)
    return result

#Sample Test
#Fibonacci(0,1,10,[])