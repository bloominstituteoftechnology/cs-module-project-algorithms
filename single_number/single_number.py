'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    a = set(arr)

    for item in a:
        count = arr.count(item)

        if count == 1:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


def single_number(nums):
    no_dups = []

    for num in nums:
        if num not in no_dups:
            no_dups.append(num)

        else:
            no_dups.remove(num)

    return no_dups[0]


def single_number_dict(nums):

    counts = {}

    for num in nums:
        if num not in counts:
            counts[num] = 1

        else:
            counts[num] += 1

    for k, v in counts.items():
        if v == 1:
            return k
