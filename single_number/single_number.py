'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# this is the first pass solution
# this will loop through the array and will keep the number that doesn't have any 
# number equal to it
# def single_number(arr):
#     # will loop through the array and will put the 
#     # numbers in array 
#     # will check if the number is in a second array.
#     # If the number is not in the array then will add the number to the array.
#     # If the number is in the array already then the number will be removed from the array.
#     single = []
#     for i in range(len(arr)):
#         if arr[i] not in single:
#             single.append(arr[i])
#         else:
#             single.remove(arr[i])
#     return single[0]




# This is the second pass solution that has the space complexity  of o(1)
def single_number(arr):
    # has to flags
    
    val = None
    # looping through the arr
    # will be popping off the value at the index asked for 
    # then will ask if the value is in the rest of the
    # array. If it is not then will return the value 
    # If it is in the array will remove pop this value again from the
    # array to make the array smaller
    # Doing a while loop
    # will continue to loop until there is just one element
    while len(arr) > 1:
        val = arr.pop() # removing the last element in the list
        if val in arr:
            arr.remove(val)
        else:
            break
    return val

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")