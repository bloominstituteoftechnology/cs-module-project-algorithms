'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    counts = {}
    for x in arr:
        if x in counts:
            del counts[x]
        else:
            counts[x] = 1

    return list(counts.keys())[0]

    # first pass solution in class
    # keep an array, call it no_dups to hold numbers we see in nums array
    # iterate through nums
        # check to see if the number is already present
        # remove duplicate nums
    # when finished, the number remaining is the odd number out
    # no_dups = []
    # for x in arr:
    #     if x not in no_dups:
    #         no_dups.append(x)
    #     else:
    #         no_dups.remove(x)
    # return no_dups[0]

    # solution for homework
    # for i in range(len(arr)):
    #     twice_flag = False
    #     for j in range(len(arr)):
    #         if i != j and arr[i] == arr[j]:
    #             twice_flag = True
    #     if not twice_flag:
    #         return arr[i]
    # return -1

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")