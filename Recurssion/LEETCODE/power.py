"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""
import sys
import math
def isPowerOfTwo(n):
    print(n)
    if n==1:
        
        return True
    else:
        if n%2!=0:
            return False
        return isPowerOfTwo(n//2)

def isPowerOfThree(n):
    print(n)
    if n==1:
        
        return True
    else:
        if n%3!=0:
            return False
        return isPowerOfTwo(n//3)

def normal_solution(n):
    if n>0:
        return n>0 and ((math.log(n)/math.log(4))-int(math.log(n)/math.log(4)))==0
    
def main():
    n=int(sys.argv[1]) 
    print("Number which is input is",n)
    # print("solution from the recursion  ",isPowerOfTwo(n))
    # print("solution from the normal solotion using log",normal_solution(n))
    print("solution from the recursion fro 3",isPowerOfThree(n))

    
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py
