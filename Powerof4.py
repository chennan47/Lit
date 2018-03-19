# 1. A simple method is to take log of the given number on base 4, and if we get an integer then number is power of 4.
#
# 2. Another solution is to keep dividing the number by 4, i.e, do n = n/4 iteratively.
# In any iteration, if n%4 becomes non-zero and n is not 1 then n is not a power of 4, otherwise n is a power of 4.
# Python3 program to check if given
# number is power of 4 or not

# Function to check if x is power of 4


def isPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 4 != 0):
            return False
        n = n // 4

    return True


# Driver code
test_no = 64
if (isPowerOfFour(64)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')

    # This code is contributed by Danish Raza