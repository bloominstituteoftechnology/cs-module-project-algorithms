'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # $%$Start
    '''
    Solution that utilizes bitwise-NOT in order to cancel out numbers we've seen before
    O(n) time and O(1) space
    '''
    answer = 0
    for x in arr:
        answer ^= x
    return answer


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


def single_number(nums):  # O(n)
    counts = {}
    # iterate through nums
    for num in nums:  # O(n)
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    for k, v in counts.items():  # O(n)
        if v == 1:
            return k
