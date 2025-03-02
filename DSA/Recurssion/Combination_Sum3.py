


def combination_sum_24_12_23(array,target,index_to_be_picked,final_list,temp_list,array_length):
    print(array,target,index_to_be_picked,temp_list)
    if index_to_be_picked==array_length:
        if (target==0):
            print(temp_list,"**********************")
        return

    if array[index_to_be_picked]<=target:
        # target-=array[index_to_be_picked]
        temp_list.append(array[index_to_be_picked])
        combination_sum_24_12_23(array,target-array[index_to_be_picked],index_to_be_picked,final_list,temp_list,array_length)
        # target+=array[index_to_be_picked]
        temp_list.pop()
    combination_sum_24_12_23(array,target,index_to_be_picked+1,final_list,temp_list,array_length)

        



def main():
    array =[2,3,5,7]
    target = 8
    index_to_be_picked= 0
    print("start")
    print("The sorted array is",combination_sum_24_12_23(array,target,index_to_be_picked,[],[],len(array)))


if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py
