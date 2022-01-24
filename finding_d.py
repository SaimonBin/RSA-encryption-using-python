
import random



phiN= 1702870528
e=48975
d=0
y1=1
temp_phiN = phiN

while e> 0:
    temp1 = temp_phiN//e
    temp2 = temp_phiN - temp1*e
    temp_phiN = e
    e = temp2

    y = d - temp1 * y1

    d = y1
    y1 = y

    if e == 1:
        break;

print(f"value of d is {y1}")

