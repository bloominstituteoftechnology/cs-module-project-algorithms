'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    ans = 0
    for i in arr:
        ans = ans^i
    return ans


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
""""
PLAN
  Create a variable ans  
  Loop through arr list
    - Use ^ to perform an XOR operation to remove the odd number
  Return ans 
"""

"""
Pseudocode
    Init ans var with 0
    Loop through given array
        - XOR ans with the item in list
    Return ans 
"""
