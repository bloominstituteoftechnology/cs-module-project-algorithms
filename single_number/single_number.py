'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
Need O(1) space complexity, which means doing the traversal in place, rather than creating new arrays, and without
changing the shape of the given array. O(1) space complexity allows for creation of pointers (even multiple pointers)
as long as the number of pointers is static, not related to n of list
Attempt to find doubled int on one traversal through array
'''
def single_number(arr):
    # need matching pointer to check against l[0].
    # if no match is found, step pointer forward until a match is found. discard values. now l[0] is a new value.
    # if second reaches end of list with no pair found, l[0] is result
    pointer = 1
    while len(arr) > 1 and pointer < len(arr):
        if arr[0] == arr[pointer]:
            arr.pop(pointer)
            arr.pop(0)
            pointer = 1
        else:
            pointer += 1
    return arr[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")