'''
Input: a List of integers
Returns: a List of integers
https://stackoverflow.com/questions/36288124/multiply-list-by-all-elements-of-the-list-except-at-its-own-index
reduce https://www.geeksforgeeks.org/reduce-in-python/
enumerate https://www.bitdegree.org/learn/python-enumerate
'''

from functools import reduce

def product_of_all_other_numbers(arr):
    # Your code here
    res = []
    for i, el in enumerate(arr):
        res.append(reduce(lambda x, y: x*y, arr[:i] + arr[i+1:]))
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
