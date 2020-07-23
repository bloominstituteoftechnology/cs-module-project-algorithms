'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    max_num = max(arr)
    #print(max_num)
    #create an array of zero for each possible number + 1 for 0
    full_array = [0 for _ in range(max_num + 1)]
    #print('full_array 1', full_array)

    for x in range(len(arr)):
        #add 1 to the index everytime the number occurs
        full_array[arr[x]] += 1


    #find the item with only one occurance
    for x in range(len(full_array)):
        if full_array[x] == 1:
            return x


arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
print('single 1:', single_number(arr))

def single_number2(nums):
    #keep track of counts of times seen a particular number
    #dictonaries are better at being searched
    counts = {}

    #loop through nums to tally up how many times we've seen each number
    for x in nums:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    #loop through all key-value pairs in counts to find the one pir
    #whose value is 1
    for num in counts:
        if counts[num] == 1:
            return num

arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
single_number2(arr)

if __name__ == '__main__':
    #Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number2(arr)}")

def solution(A):
    # write your code in Python 3.6
    maxValue = max(A)
    #maxValue + 1, because starts with 0
    elements = [0 for _ in range(0, maxValue + 1)]
    
    print(elements)
    for i in A:
        elements[i] += 1
    print(elements)
    for i in range(len(elements)):
        if elements[i] == 1:
            odd = i
    return odd
print(solution(arr))

def return_odd(A):
    # write your code in Python 3.6
    counts = {}

    #loop through nums to tally up how many times we've seen each number
    for x in A:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    #loop through all key-value pairs in counts to find the one pir
    #whose value is 1
    for num in counts:
        if counts[num]%2 != 0:
            return num

A = [1,3,1,3,0, 0 ,0]
print(return_odd(A))

