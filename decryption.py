
import random
import re
import codecs
#w= int("0x48656c ",16 )
import sys


cipher= [1315173943, 969027936, 1179977769, 303419892, 597369997, 914877143, 1659896485];
d= 560947631

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

N=1702953433
integer=[]
for part in cipher:
    c=int(part)
    dec=(int(now(c, d, N)))
    integer.append(dec)
    
print(integer)

hexa=[]
for j in integer:
    w=hex(j)
    p=(w[2:])
    hexa.append(p)
print(hexa)

msg=""
for k in hexa:
    x=bytes.fromhex((k))
    y=x.decode("ascii")
    msg += y 
print(msg)

