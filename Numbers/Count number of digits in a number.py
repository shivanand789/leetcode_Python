def noofdigits(n):
    num=n
    cnt=0
    while num>0:
        cnt +=1
        num=num//10

    return cnt
123//10
import math
def numberofdigits(n):
    cnt=math.floor((math.log(n,10)))+1
    return cnt



n=input("Ënter the number ")
print(int(n),type(n))

# print(noofdigits(12345))
# print(numberofdigits(45641))

