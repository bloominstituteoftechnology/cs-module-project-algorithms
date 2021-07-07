# O(n^2) runtime on brute force approach, can we improve?

# Is there a data structure that would help?
# A dict help by allowing to check for duplicate values
# Sets are also an option
# As we loop, save the fact that we saw this value
# If we see it again, then remove them


def single_number(arr):
    '''
    Input: a List of integers where every int except one shows up twice
    Returns: an integer
    '''

    # As far as space complexity is concerned, worse case would be
    #   if we only have half of the elems in the set before we start
    #   removing any of them: O((1/2) * n) space complexity
    s = set() #> O(1)

    # loop through array #> O(n)
    for i in arr:

        if i in s:
            s.remove(x) #> O(1)
        else:
            s.add(x) #> O(1)

    # at this point, should only have 1 elem in set
    return list(s)[0] #> O(1)


# Space complexity: measures how memory-usage scales

    # ANy data structures that are passed into a function don't count
    #   towards space complexity

    # Space complexity only cares about any additional data structures
    #   that are initialized during function execution