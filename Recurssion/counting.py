import sys
def count_calcualtor_tail(n):
    """
    In this processing steps comes before the fumcton calls
    """

    if n==0:
        return 
    else:
        #tail recurssion
        print(n)
        count_calcualtor_tail(n-1)

def count_calcualtor_head(n):
    """
    In this processing steps comes after the fumcton calls
    """

    if n==0:
        return 
    else:
        #tail recurssion
        
        count_calcualtor_head(n-1)
        print(n)
def main():
    # base_number = int(sys.argv[1])
    n = int(sys.argv[1])
    
    # base_number = int(input("enter the base vslaue"))
    # n = int(input("enter the n value"))
    # print(f"the power of the value {base_number}",count_calcualtor(n))
    # count_calcualtor_tail(n)
    count_calcualtor_head(n)

if __name__=="__main__":
    main()
