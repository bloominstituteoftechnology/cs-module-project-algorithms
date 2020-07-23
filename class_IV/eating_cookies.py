# def eating_cookies(n):
#     # no negative values for n
#     if n < 0:
#         return 0
#     # if "tree" gets down to 0, count that as a way to eat
#     if n == 0:
#         return 1
#     # otherwise, get closer to base case by calling `eating_cookies`
#     # on each of the "alternate futures" for how the monster ate
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    # Implementation has O(3^n) runtime complexity due to the fact that there
    # are three possible decisions each time

    # How do we reduce the amount of redundant work?
        # Use a data structure to "cache" (or "save") answers that some other
        #   branch has already done
        # Someone still has to figure out the answer in the first place
        #   but once that answer is computed, can share that with the other branch
        #   that needs to calculate the same thing
        # Branches that need an answer that's already been computed can check
        #   the cache and see if the answer is already there, and access it
        #   if so

    # What data structure should we use for the cache?
        # Save the n value for the branch along with its associated answer
        # Save the n value as a key and associated answer as its value in 
        #   a dictionary
        # Need to pass the dictionary to each recursive call

def eating_cookies(n, cache):
    # no negative values for n
    if n < 0:
        return 0
    # if "tree" gets down to 0, count that as a way to eat
    if n == 0:
        return 1

    # check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]

    # otherwise, n is not in cache, so compute answer the "normal" way
    else:
        # once the answer is computed, save it in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

    # This implementation cuts out the redundant work by using a cache, in this
    # case a dictionary, so every n value is only computed once rather than
    # redundantly

    # This reduced runtime from O(3^n) to O(n) but did increase space complexity

if __name__ == "__main__":
    n = 50
    print(eating_cookies(n, {}))