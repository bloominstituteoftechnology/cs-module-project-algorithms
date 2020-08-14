import math as math
'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    final_arr = [0] * len(arr)
    for i in range(len(arr)):

        j = i + 1

        new_arr = arr[:i] + arr[j:] if i != 0 else arr[j:]

        elem = math.prod(new_arr)

        final_arr[i] = elem

    return final_arr   
    # remember the indexes using i and j comprehensions! use them to create 3 arrays... left_of, [elem], right_of
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
