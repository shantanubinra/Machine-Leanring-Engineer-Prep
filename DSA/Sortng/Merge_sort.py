class Merge_Sort:


    def merge_array(self,low,high,mid,array):
        



    def divide_array(self,low,high,array):
        if low==high:
            return
        mid=(low+high)//2
        self.divide_array(low,mid,array)
        self.divide_array(mid+1,high,array)

        self.merge_array(low,high,mid,array)

