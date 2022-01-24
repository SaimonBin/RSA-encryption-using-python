
import random
import re
import codecs
def encryption(N,d):

    msg='Saimon Bin Islam  '
    x= re.findall('...?', msg)

    print(x)
    hex=" "
    for i in x:

        s= (i.encode('utf-8').hex())
        hex += s + " "
    print(hex)
    h=hex.split()
    print(h)

    integer=[]
    for j in h:
        w= int(j, 16)
        integer.append(w)
    print(integer)
    return integer, N, d

def now(base, power, MOD):
     result = 1
     while power > 0:
           # If power is odd
           if power % 2 == 1:
                
                result = (result * base) % MOD

           # Divide the power by 2
           power = power // 2
           # Multiply base to itself
           base = (base * base) % MOD
     return result


integer, N, d=encryption(1702953433, 560947631)

cipher= []
for c in integer:
     cipher.append(int(now(c, d, N)))



print(f"The cipher values are: {cipher}")
