'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    i = 0
    neighbor_index = 1

    while len(arr) > 1:
        if neighbor_index == len(arr):
            return arr[i]
        if arr[i] == arr[neighbor_index]:
            arr.pop(neighbor_index)
            arr.pop(i)
            neighbor_index = 1
        else:
            neighbor_index += 1


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


    array = [1,3,6,7,67,9]

# // I have an array, I'm to find numbers evenly divisible by three

for n in array:
    # if this num when divided by 3 has no remainder
    if n % 3 == 0:
        print(n)
    