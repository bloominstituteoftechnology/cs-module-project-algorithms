'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # first pass solution

    # let's create a new list
    # and re order them as we loop arr
    new_list = []
    zero_cnt = 0 # zero counter
    for item in arr:
        if item != 0:
            new_list.append(item)
            continue
        zero_cnt += 1
    new_zeros = [0]*zero_cnt
    return new_list + new_zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")