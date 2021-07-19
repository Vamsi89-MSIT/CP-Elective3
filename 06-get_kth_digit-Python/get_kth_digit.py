# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 


import math
def fun_get_kth_digit(digit, k):
    if digit < 0:
        digit = digit * -1
        return (digit // (10 ** k)%10)
    elif digit > 0:
        return (digit // (10 ** k)%10)
    else:
        return 0

	
		
