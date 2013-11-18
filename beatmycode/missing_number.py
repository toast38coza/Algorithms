"""
# Missing number:
Source: http://www.beatmycode.com/challenge/6/show

----

One number is deleted from the sequence 1,2,3, ... N. 
You get the numbers in a random order, and have to find the deleted one. 
Preferably in O(N).

The "BMC_TEST_INPUT_MAGIC" (with quotes) in the code will be replaced with the actual value of the input. 
The input is in the format: "N:1,2,3,...,N" where N is the end of the sequence. 
Any item can be missing from 1 to N, so you get N-1 numbers!

N is at least 1.

Example:
"8:1,2,3,4,5,6,8" -> 7 is the deleted item


"""

def missing_number(l, n):
    """
    method: 
    1. Calculate the sum of the numbers without the missing number (using Gauss'es trick: http://mathforum.org/library/drmath/view/57919.html)
       * Order doesnt matter here. We know that numbers are consecutive and we have the total number
    2. Iterate though the list once and sum the total
    3. Missing number is the difference of the two
    """


    expected_total = n * (n+1)/2
    actual_total = reduce(lambda x, y: x+y,l)

    return expected_total-actual_total

if __name__ == "__main__":
    print missing_number([1,2,3,4,5,6,8],8)