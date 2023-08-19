import sys
def power_calcualtor(n,base_value):

    if n==1:
        return base_value
    else:
        return base_value*power_calcualtor(n-1,base_value)
    
def main():
    base_number = int(sys.argv[1])
    n = int(sys.argv[2])
    # base_number = int(input("enter the base vslaue"))
    # n = int(input("enter the n value"))
    print(f"the power of the value {base_number} with power {n} is",power_calcualtor(n,base_number))
if __name__=="__main__":
    main()
