'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    boii = []

    if arr == 0:
        return 0

    else: 
        for num in range(len(arr)):
            for other in range(num + 1, len(arr)):
                if boii.__contains__(arr[num]):
                    break
                
                if arr[other] == arr[num]:
                    boii.append(arr[other])
                    break
                else: 
                    if other + 1 == len(arr):
                        print(arr[num])
                        return arr[num]
                        
                    else: 
                        continue
                    
                    
# arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
# arr2 = [2,8,2,9,5,9,5]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")