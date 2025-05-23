"""
Lab 3
1. Write a Python function to compute the Greatest Common Divisor
(GCD) of two numbers using the Euclidean algorithm. Then, use this
function to find the GCD of three numbers by calling the two-number
GCD function recursively.
2. Write a Python function to find the Least Common Multiple (LCM) of
two numbers by starting from the maximum of the two and checking
each multiple until one is divisible by both numbers. The function
should return the smallest common multiple found through this
process.
3. Write a Python function to check whether a given number n is prime or
not using an efficient approach
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))   # True
print(is_prime(4))   # False


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)

def lcm(a, b):
    multiple = max(a, b)
    while True:
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        multiple += 1

# Testanrop som rekommenderas i feedbacken
print("GCD of 12 and 18 is:", gcd(12, 18))               # 6
print("GCD of 15, 25, and 35 is:", gcd_three(15, 25, 35))  # 5
print("LCM of 4 and 6 is:", lcm(4, 6))                   # 12