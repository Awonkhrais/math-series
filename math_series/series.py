# lucas fibonacci 

def fibonacci(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# lucas series 

def lucas (n):

    if n == 0 :
        return 2
    if n == 1 :
        return 1

    return lucas(n-1) + lucas(n-2)


# sum series:(this one for Fibonacci )

def sum_series(n,x=0,y=1):
    
    if n == 0 :
        return x
    
    if n == 1 :
        return y 
    
    return sum_series(n-1) + sum_series(n-2)



# ---------------------------------------------
# sum series:(this one for Lucas )

# def sum_series(n,x=2,y=1):
    
#     if n == 0 :
#         return x
    
#     if n == 1 :
#         return y 
    
#     return sum_series(n-1) + sum_series(n-2)

# ---------------------------------------------


