'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # This one is a challenge
    # I could do it in O(n^2) time by solving at each index
    # I could also do it in O(n) time by multiplying all the numbers, then dividing by the number at each index
    # But the directions say specifically not to divide

    result = []

    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if j != i:
                product *= arr[j]
        result.append(product)

    return result

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2] * 10000

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
