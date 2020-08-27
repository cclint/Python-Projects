"""

Binary Search (iterative)

"""
array = [1,2,3,4,5,6,7,8,9,10,11,12] # sorted array in ascending order
target_num = 9 # target integer

def binarySearch(array, target_num):
    lower_bound = 0 # lower bound is the lowest index 
    upper_bound = len(array) - 1 # upper bound is the highest index
    
    while lower_bound <= upper_bound:
        middle_bound = (upper_bound + lower_bound) // 2 # this is the average of left and right 
        
        if array[middle_bound] == target_num:
            return middle_bound
        else:
            if array[middle_bound] < target_num:
                lower_bound = middle_bound + 1
            else:
                upper_bound = middle_bound - 1
            
            
print(binarySearch(array, target_num))       

# this algorithm has the time complexity O(logn), where n is the number of elements in the array
 
