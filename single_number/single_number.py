from sorting import merge, merge_sort

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    
    arr = merge_sort(arr)
    
    i = 0
    j = 1
    
    # run this loop until I manually break it
    while True:
        
        # if index j is outside the list range, return the last item in the list
        if j >= len(arr):
            return arr[i]
            break
        
        # if value at index i equals value directly to its right, increment i
        #. and j by 2 and continue the loop
        elif arr[i] == arr[j]:
            i += 2
            j += 2

        # Otherwise, two values next to each other aren't equal, and we should
        #. return the value to the right
        else:
            return arr[i]
            break
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")