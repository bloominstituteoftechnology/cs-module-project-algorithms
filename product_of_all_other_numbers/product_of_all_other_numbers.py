'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Start with 1. If we start with 0 it will multiply by 0
    result = 1

    # This while loop through our array, and multiply each value with the result
    for x in arr:
        # After the multiplication, we'll have a new result so keep multiplying to, until we run out of elements in our array
        result *= x
        # Our result (total) will then be divided by the number in our list. 
    return [result / x for x in arr]
    
    # Using the first arr = [1, 2, 3, 4, 5] it will return a result of 120.
        # 120 will then be divided by each number in our list, giving us an output of [120, 60, 40, 30, 24]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    #arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")