'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zero_count = arr.count(0)
    curr_count =0
    print( zero_count)
    while curr_count<zero_count:
        arr.pop(arr.index(0))
        arr.append(0)
        
        curr_count+=1
    return arr
 
 
    
 

  

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")