def array_swaping(top,down,array):
    
    if top>=down:
        print(array)
        exit()
    array[top],array[down] = array[down],array[top]
    array_swaping(top+1,down-1,array)

def array_swapping_single_pointer(single_pointer,array):
    print(single_pointer,"single_pointer")
    if single_pointer>=len(array)//2:
        print(array,"single pointer")
        exit()
    array[len(array)-single_pointer-1],array[single_pointer] = array[single_pointer],array[len(array)-single_pointer-1]
    array_swapping_single_pointer(single_pointer+1,array)



def main():
    
    array=[1,2,3,4,5]
    array_swaping(0,len(array)-1,array)
    array_swapping_single_pointer(0,array)
if __name__=="__main__":
    main()