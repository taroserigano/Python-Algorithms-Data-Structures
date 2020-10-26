# Python3 code to implement Jump Search 
import math 
  
def jumpSearch( arr , x , n ): 
      
    # Finding BLOCK size to be jumped 
    step = math.sqrt(n) 
      
    # Finding the block where element is 
    # present (if it is present) 
    # min for initial number of the block
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        # go to another block
        step += math.sqrt(n) 
        if prev >= n: 
        # then, the n number was NOT found
            return -1
      
    # Doing a linear search for x in  
    # block beginning with prev. 
    while arr[int(prev)] < x: 
        # move inside the block ONE by ONE 
        prev += 1
          
        # If we reached next block or end  
        # of array, element is not present. 
        if prev == min(step, n): 
            return -1
      
    # If element is found 
    if arr[int(prev)] == x: 
        return prev 
      
    return -1


# Driver code to test function 
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 55
n = len(arr) 
  
# Find the index of 'x' using Jump Search 
index = jumpSearch(arr, x, n) 
  
# Print the index where 'x' is located 
print("Number" , x, "is at index" ,"%.0f"%index) 