'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

def single_number(arr):
    ''' FIRST PASS SOLUTION '''

    # # Find the count of each number
    # for i in arr:
    #     # If a number returns a count of one, return that number
    #     if arr.count(arr[i]) == 1:
    #         return arr[i]

    ''' WRITING BETTER SOLUTIONS '''

    # Sort all elements in arr
    arr.sort()

    # If first element is not equal to the value on its right, it's a single element
    if arr[0] != arr[1]:
        return arr[0]

    # If last element is not equal to the value on its left, it's a single element
    if arr[len(arr) - 1] != arr[len(arr) -2]:
        return arr[len(arr) - 1]

    # All other elements look to left and right
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
            return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")