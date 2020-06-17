
def multiplyList(myList) : 
    if len(myList) == 0:
      return 0
    # Multiply elements one by one
    else:
      result = 1
      for x in myList: 
          result = result * x
      return result  
  
  
def product_of_all_other_numbers(arr):
    """
    Returns a list of integers consisting of the product of all numbers in the
    array _except_ the number at that index.
    
        Parameters:
                arr (list): a list of integers
                
        Returns:
                arr (list): a list of integers
    """
    
    # Loop through each item in the list
    # using index as the split, separate into left and right arrays at index
    # create helper function to multiply all items in a list with each other

    multi = []

    for i in range(1, len(arr) + 1):
        if i == 1 or i == (len(arr)):
            left = arr[:(i - 1)]
            right = arr[i:]

            left = multiplyList(left)
            right = multiplyList(right)

            both = left + right

            multi.append(both)

        else:
            left = arr[:(i - 1)]
            right = arr[i:]

            left = multiplyList(left)
            right = multiplyList(right)

            both = left * right

            multi.append(both)        

    return multi


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
