def Multiply():
    assert inc(3) == 5
    a = 5
    b = 0
    c = a / b
    print "The result is : %d" % c 
   

def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       return n * factorial( n - 1 )  # recursive call

def fact(n):
    for i in range(1, n+1 ):
        print "%2d! = %d" % ( i, factorial( i ) )        
