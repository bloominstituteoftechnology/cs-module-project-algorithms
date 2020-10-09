'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    new = []
    for i in arr:
      if i != 0:
        new.insert(0, i)
      else:
        new.append(0)
    return new


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")