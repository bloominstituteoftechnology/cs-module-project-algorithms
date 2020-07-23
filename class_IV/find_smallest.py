# What is the runtime of this?
# Is that the best we can do?
    # Is there anything about the problem we aren't taking
    #   advantage of?
    # Is there a more appropriate data struc ture that would help?

# If given some sorted data, always consider binary serch
# Does binary search possibly help us here? (O(log n))

# Can we find the first elem whose value doesn't match its index
# The samllest missing elem is the 1st elem that doesn't match
# its array index
def find_smallest_missing(arr):
    """
    Given a sorted arr of distinct non-negative integers, find the
    smallest missing element in it
    """
    if arr[0] != 0:
        return 0

    for i in range(len(arr) - 1):
        print(arr)
        print(i)

        if arr[i+1] != arr[i] + 1:
            # breakpoint()
            return arr[i] + 1
        else:
            print(arr[i+1])
            return arr[-1] + 1

if __name__ == "__main__":
    
    A1 = [0,1,2,6,7] #> 3
    A2 = [1,2,3,4,6,7] #> 0
    A3 = [0,1,2,3,4,5,6] #> 7

    # print(f"A1: {find_smallest_missing(A1)}")
    # print(f"A2: {find_smallest_missing(A2)}")
    print(f"A3: {find_smallest_missing(A3)}")