
import random

def generatePrime(bits):
     while True:
         num =random.randrange(2 ** (bits - 1), 2 ** bits - 1)
         if (isPrime(num)):
             return num

def isPrime(n):
     if n ==2 or n==3:
          return True
     if n%2==0 or n<2:
          return False
     for i in range(2, int(n)):
        if (n % i) == 0:
             return False
     return True

def gcd (a , b):
    while b:
        a, b= b, a % b
        return a

def generateKeys(bits):
    e = d = N = 0
    p = generatePrime(bits)
    q = generatePrime(bits)

    #print(f"p: {p}")
    #print(f"q: {q}")

    N= p*q
    phiN= (p-1) * (q-1)
    #print(f"N: {N}")
    #print(f"phiN: {phiN}")

    e=random.randrange(1, phiN)
    g=gcd(e, phiN)
    while g!=1:
         e= random.randrange(2 ** (bits - 1), 2 ** bits - 1)
         g=gcd(e, phiN)
         break;
    #print((f"e: {e}"))
    return p, q, N, phiN, e

def main():
     print("The numbers are: ")
     bits=16
     p, q, N, phiN, e= generateKeys(bits)
     print(f"p: {p}")
     print(f"q: {q}")
     print(f"N: {N}")
     print(f"phiN: {phiN}")
     print(f"e: {e}")


main()
