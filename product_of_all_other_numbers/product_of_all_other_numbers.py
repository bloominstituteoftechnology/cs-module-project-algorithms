# '''
# Input: a List of integers
# Returns: a List of integers
# '''


def product_of_all_other_numbers(array):
    # create a holder array to hold the result
    result = []

    # outer loop
    for firstIndex in range(len(array)):
        product = 1
        # inner loop
        for secondIndex in range(len(array)):

            if firstIndex != secondIndex:
                # calculate the product of the rest elements in the array
                product *= array[secondIndex]
        result.append(product)

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
