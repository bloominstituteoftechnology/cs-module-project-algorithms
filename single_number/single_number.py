'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    my_set = set()

    for num in arr:
      if num not in my_set:
        my_set.add(num)
      else:
        my_set.remove(num)
    
    return my_set


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
