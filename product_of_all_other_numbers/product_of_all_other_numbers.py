'''
Input: a List of integers
Returns: a List of integers
'''
# This is the first pass of the solution
# Will loop through the list using the index
# will have a second loop within the  first loop 
# that will then multiply everthing found in the array
# except at the index of the first array
# def product_of_all_other_numbers(arr):
#     new_array = []
    
#     for i in range(len(arr)):
#         value = 1
#         # second loop
#         for k in range(len(arr)):
#             if i != k:
#                 # do the multiplication here
#                 value *= arr[k]
#         # appending to the array
#         new_array.append(value)
#     return new_array

# # This is the second pass through of this method
# def product_of_all_other_numbers(arr):
#     # will find the product of all the numbers in the array and then
#     # will just divide this number by the number in the current index
#     totalVal = 1
#     prod = []
#     # doing the looping to find the total value
#     for i in range(len(arr)):
#         totalVal *= arr[i]
#     # now will to the loop
#     for i in range(len(arr)):
#         prod.append(totalVal/arr[i])
#     return prod



def product_of_all_other_numbers(arr):
    # Will try to increment from one end to the other on both sides of the 
    # list will get the suffix products and the prefix products
    # will then use the suffix and the prefix to find the current product at 
    prod = [0] * len(arr)
    # the specified index
    suffix = [1] * (len(arr))
    prefix = [1] * (len(arr))
    # putting in the first value of the prefix and the suffix
    #prefix[1] = arr[0]
    #suffix[-2] = arr[-1]
    # will loop through the array twice filling up the suffix products and 
    # prefix products
    
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] * arr[i-1]
    # second loop
    for i in range(len(arr)-2, -1, -1):
        suffix[i] = suffix[i+1] * arr[i+1]
    # filling the product array
    for i in range(len(arr)):
        prod[i] = prefix[i] * suffix[i]
    return prod


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
