# https://discuss.codecademy.com/t/challenge-product-of-everything-else/176317
def product_of_all_other_numbers(arr):
    """
    Write a function that receives an array of integers and returns an array
    consisting of the product of all numbers in the array except the number at that index.
    :param arr: a list of integers
    :return: a list of integers
    """
    # so someway to exclude the index while we are doing multiplying
    # results to keep the result of all the products except index
    result = 1
    # product_list to put each product for each value
    product_list = []
    # loop through the arr
    for i in range(len(arr)):
        # access each number in the arr
        for n in arr:
            if n != arr[i]:
                # if n doesn't equal the current number for i then multiple it
                result *= n
        product_list.append(result)
        # restart
        result = 1
    return product_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
