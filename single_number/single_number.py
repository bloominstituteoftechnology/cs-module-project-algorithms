'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
from collections import Counter
def single_number(arr):
    a = Counter(arr)
    s = Counter(set(arr))
    r = a - s
    for i in set(arr):
      if i not in r:
        return i




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")