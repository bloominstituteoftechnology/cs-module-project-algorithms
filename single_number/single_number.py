'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    if len(arr) == 0:
        return
    i = 0
    j = i+1
    l = len(arr)
    k = 0
    while i <= l and j <= l:
        target = arr[i]
        k = 0
        if arr[i] != arr[j]:
            j += 1
        else:
            while k <= l - 1:
                if arr[k] == target:
                    arr.remove(arr[k])
                    k = 0
                    l -= 1
                else: 
                    k += 1
        if j == l - 1:
            i += 1
 

    return arr



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")