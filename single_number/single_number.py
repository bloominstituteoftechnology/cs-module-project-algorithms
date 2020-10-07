'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # loop through entire array and find the same number if not there
    #then that's the one
    matches = 2 
    current_number = 0

    while matches == 2:
        matches = 0
        for item in arr:
            if arr[current_number] == item:
                matches += 1
        current_number += 1
    

    return arr[current_number-1]




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")