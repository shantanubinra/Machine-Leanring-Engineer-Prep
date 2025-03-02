import sys

def fib(n):
    """
    0,1,1,2,3,5
    """

    if n==1:
        # print(n)
        return 0
    elif n==2:
        # print(n)
        return 1
    
    else:value = fib(n-1)+fib(n-2)
    # print(value)
    return value

def fib_loop(n):
    a1=0
    a2=1
    recent_value=1
    
    for i  in range(n):
        if i>1:
            recent_value=a1+a2
            a1=a2
            a2=recent_value
            
        else:
            print(i)
    print("I am function 2 with loop",recent_value)




def main():
    n=int(sys.argv[1])
    print("the final last element of the series is",fib(n))
    print(fib_loop(n))
if __name__=="__main__":
    main()
    print(1/2)
    print(8%2)