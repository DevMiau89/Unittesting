
def multiply():
    a = 5
    b = 4
    c = a * b
    print "The result is : %d" % c 
    return c
    
  
def factorial( n ):
    if n < 1:   # base case
        return 1
    else:
       return n * factorial( n - 1 )  # recursive call

def fact(n):
    for i in range(1, n+1 ):
        print "%2d! = %d" % ( i, factorial( i ) )        

def test_factorial():
    assert factorial(3) == 5 

def test_multiply():
    assert multiply() == 21
