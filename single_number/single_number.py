'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# def single_number(arr):
#     # get length of arr
#     n = len(arr)
#     # iterate of range of n
#     for i in range(0, n):
#         # create an index variable to compare with i
#         j = 0
#         # while j < length of arr
#         while j<n:
#             # if i and j are not equal, but the values at the respective indexes are then break (i.e. run our loop again).  We have a match.
#             if i != j and arr[i] == arr[j]:
#                 break
#             # increment j
#             j += 1
#             # if we're at the end of the loop we have not found a match for the value of element at i index.
#             if j == n:
#                 return arr[i]
#     return -1

def single_number(arr):
    # dictionary that keeps track of number of times an item occurs in arr
    cache = {}

    # loop through each item in arr
    for x in arr:
        # if item exists in cache, we found a duplicate.  Delete it.
        if x in cache:
            del cache[x]
        # if it doesn't exist create it.
        else:
            cache[x] = 1
    # there should be only 1 item left in the dictionary.  Return it.
    for k,v in cache.items():
       return k


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")