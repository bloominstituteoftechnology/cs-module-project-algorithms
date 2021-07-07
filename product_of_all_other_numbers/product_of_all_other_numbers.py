import math

def product_of_all_other_numbers(arr):
    '''
    Input: a List of integers
    Returns: a List of integers
    '''
    # Your code here

    # empty list to catch the products
    products = []

    # Create start and end points for loop
    start = 0
    end = len(arr) - 1 #> O(n)

    # Loop through arr by using start as index
    while start <= end: #> O(n)

        # make a copy of arr to leave unmodified by `pop`
        c = arr.copy()
        # breakpoint()
        # print("start:", start)
        # print(c)

        # `pop` current index value
        c.pop(start) #> O(1): always popping a single elem

        # now, get product of remaining copy list
        x = math.prod(c) #> O(nk)

        # add that to products list
        products.append(x) #> O(1)

        # print(c)
        # breakpoint()
        # Update start
        start += 1 #> O(1)

    return products


# Another tricky one to me because I'm using a while loop, which has
# O(n) runtime based on size of input array, but all the commands
# inside the loop are O(1) with 1 exception: getting the product of the 
# list.

# The problem with that though is the length of the array it is multipying
# is always the same: len(arr) - 1. This would not ever increase, so does
# that also make it a constant runtime O(1)?


if __name__ == '__main__':
    # # Use the main function to test your implementation
    # # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    # For example, given
    # ```
    # [1, 7, 3, 4]
    # ```
    # your function should return
    # ```
    # [84, 12, 28, 21]
    # ```
    # by calculating
    # ```
    # [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    # ```

    samp = [1, 7, 3, 4]
    print(product_of_all_other_numbers(samp))
    # breakpoint()
