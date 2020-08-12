'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    curr_count = 1
    arr.sort()
    
    least_frequent =-1
    min_count = len(arr) + 1

    for i in range( 1, len(arr)):
        
         if arr[i] == arr[i-1]:
             curr_count +=1
         else:
             if(curr_count <min_count):
                 min_count = curr_count
                 least_frequent = arr[i-1]
             curr_count =1   
    if (curr_count<min_count):
        min_count = curr_count
        least_frequent =arr[len(arr)-1] 
        
    return least_frequent
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")