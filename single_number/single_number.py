from sorting import merge, merge_sort


def single_number(arr):
    '''
    Returns the only integer in the list that only shows up once
    
        Parameters:
                arr (list/array): a list/array of integers, where every integer
                shows up once except for one integer
            
        Returns:
                single number (int): the one integer that shows up once
    '''
    # arr = merge_sort(arr) # O(n log n)
    
    # i = 0
    # j = 1
    
    # # run this loop until I manually break it
    # while True:
    #     # if index j is outside the list range, return the last item in the list
    #     if j >= len(arr):
    #         return arr[i]
    #         break
    #     # if value at index i equals value directly to its right, increment i
    #     #. and j by 2 and continue the loop
    #     elif arr[i] == arr[j]:
    #         i += 2
    #         j += 2
    #     # Otherwise, two values next to each other aren't equal, and we should
    #     #. return the value to the right
    #     else:
    #         return arr[i]
    #         break
        
    
    odd_one_out = (2 * sum(set(arr))) - sum(arr) # O(1)
    
    return odd_one_out
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")