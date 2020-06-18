'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# My first pass solution
# def single_number(arr): 
#     # initialize a null list for single numbers
#     single_list = []
#     duplicate_list = []

#     # go through all elements
#     for element in arr:
#         if element not in single_list:
#             single_list.append(element)
#         else:
#             duplicate_list.append(element)
#             single_list.remove(element)
#     return single_list[0]

# # Instructor's first-pass solution
# def single_number(num): 
    # # we'll keep an array, call it `no_dups` to hold numbers we see in the nums array
    # no_dups = [] # O(n)
    # # iterate through nums
    # for num in nums: # O(n)
    #     # check to see if the number is already in the `no_dups` array
    #     if num not in no_dups: # 0(n)
    #         no_dups.append(num)
    #     # if it is, remove it from the `no_dups` array
    #     else:
    #         no_dups.remove(num) # O(n)
    # # when we're done iterating, the only number in our `no_dups` array is the odd number out
    # # return the odd number out
    # return no_dups[0]

# Optimized solution
def single_number(arr): # O(n)
    # keep track of number of times an item occurs in input
    counts = {}

    # loop through input list - O(n)
    for num in arr:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            # add item
            counts[num] = 1
    
    # return counts[counts.keys()[0]]
    for key, value in counts.items(): # O(1), because it will always be only 1 item
        if value == 1:
            return key

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")