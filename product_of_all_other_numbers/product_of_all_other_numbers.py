'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    result = []
    for firstIndex in range(len(arr)):
        product = 1
        for secondIndex in range(len(arr)):
            if firstIndex != secondIndex:
                product *= arr[secondIndex]
        result.append(product)

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]

print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
