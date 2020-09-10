'''
Input: a List of integers
Returns: a List of integers
'''

from functools import reduce

def product_of_all_other_numbers(arr):
    ''' FIRST PASS SOLUTION '''

    # # Get full product of arr by multiplying each element by current product value
    # product = 1
    # for i in arr:
    #     product *= i

    # # Setup result list with initial state of full array product and a length of len(arr)
    # result = [product] * len(arr)

    # # For each element, return the product divided by that element
    # index = 0
    # for i in arr:
    #     # If product is 0 and i is 0, set product to all other elements combined
    #     if product is 0 and i is 0:
    #         temp_product = 1
    #         for j in arr:
    #             if arr.index(j) != arr.index(i):
    #                 temp_product *= j
    #         result[index] = temp_product
    #         index += 1
    #     # Else, if product is 0, but element is not, increase index by 1
    #     elif product is 0:
    #         index += 1
    #     # Else, set result at index to be product / element
    #     else:
    #         result[index] = product / i
    #         index += 1

    # return result

    ''' WRITING BETTER SOLUTIONS '''
    result = []

    for i in arr:
        # Find if i is a duplicate number
        duplicates = [d for d in arr if d == i]

        # Create a temporary list of all elements minus the current one
        temp_list = [n for n in arr if n != i]
        
        # If len(duplicates) > 1, add duplicates[1:] to temp_list
        if len(duplicates) > 1:
            combined_list = temp_list + duplicates[1:]
            # Get product of all elements in the temp_list
            product = reduce(lambda x, y: x * y, combined_list)
        else:
            product = reduce(lambda x, y: x * y, temp_list)

        # Append product to result list
        result.append(product)
    
    return result

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")