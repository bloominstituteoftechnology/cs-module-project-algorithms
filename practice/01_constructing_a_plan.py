'''
We'll say that a positive int divides itself
if every digit in the number divides into the
number evenly.

Example One:
So for example 128 divides itself
since 1, 2, and 8 all divide into 128 evenly.

Example Two:
64
This does not divide itself because 64 is not evenly divisible by 6.

And we'll say that 0 does not divide into anything
evenly, so no number with a 0 digit divides itself. 

Write a function to determine if a number divides itself.

[source - https://codingbat.com/prob/p165941]
'''

def divides_self(num):
    '''Takes in a positive integer and determines if the number "divides itself"

    input: integer
    output: Boolean

    >>> divides_self(128)
    True
    >>> divides_self(12)
    True
    >>> divides_self(120)
    False
    '''
    # Plan
    # if num less than or equal to 0
        # return False
    # if num less than 10
        # return True

    # split num into individual digits and
    # loop through each digit in num
        # if digit does not evenly divide into num or if digit equals 0
            # return False

    # if we get through all of the digits
    # return True

    # Going to need modulo (even division)
    # May need split
    # Need method for isolating each digit in the num