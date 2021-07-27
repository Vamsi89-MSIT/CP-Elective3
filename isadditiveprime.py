def isprimes(n):
    if(n < 2):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
        return False

def isAdditivePrime(n):
    if(isprimes(n)):
        s = 0
        while(n):
            remainder = n % 10
            s = s + remainder
            n = n // 10
            if(n == 0) and (isprimes(s)):
                return True
    return False

assert(isAdditivePrime(121) == False)
assert(isAdditivePrime(32) == True)

        