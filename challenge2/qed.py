import math
import sys

# determines if numbers are prime
def isPrime(p):
    if p <= 1:  # 0 or 1
        return False
    elif p <= 3:    # 2 or 3
        return True

    if p % 2 == 0 or p % 3 == 0:    #eliminates multiples of 2 or 3
        return False

    # ALL NON-PRIME NUMBERS ARE DIVISIBLE BY PRIME NUMBERS
    #starts at 5 (or 6n-1) and increases by 6
    for i in range(5, math.ceil(math.sqrt(p)), 6):
        if p % i == 0 or p % (i + 2) == 0: #checks if p is divisible by 6n-1 or 6n+1
            return False

    return True


print("Odd numbers that cannot be calculated with given formula:")
# only evaluate odd nums
# k = p + 2*n*n
count = 0
with open("output.txt", "w") as f: #refrence output.txt for numbers
    for k in range(5775, sys.maxsize, 2):
        valid = False

        for n in range(0, math.floor(math.sqrt(k)), 1):
            p = k - 2 * n * n
            if isPrime(p) == 1:
                valid = True
                break

        if not valid:
                count += 1
                f.write(str(k)+"\n") #stores in file
                print(str(k))

        if count == 2: #only 2 possible solutions
            break

print("Finished!")