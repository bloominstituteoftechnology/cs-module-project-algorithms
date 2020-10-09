'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zereos = []
    others = []
    for x in range(len(arr)):
        if arr[x] == 0:
            zereos.append(arr[x])
        else:
            others.append(arr[x])
            
    arr = others + zereos
    
    return arr

# arr = [0, 3, 1, 0, -2]
# moving_zeroes(arr)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")