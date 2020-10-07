'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # there will be 2 matches for all numbers except one
    matches = 2 
    # we will start at the beginning of the array
    current_number = 0

    # Keep looping until there aren't 2 matches
    while matches == 2:
        # make sure to reset the matches count
        matches = 0
        # loop through each item 1 by one
        for item in arr:
            # if it matches then increment by one
            if arr[current_number] == item:
                matches += 1
        # go to the next item in the array and do again
        current_number += 1
    
    # if there wasn't 2 matches then the one before the increment was our number
    return arr[current_number-1]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")