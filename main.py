print("hello world")
print("   /|")
print("  / |")
print(" /  |")
print("/   |")
hii="meghal"
print("my name is "+hii+" guo")
hii="aadil"
print("my name \"is\" "+hii+" guo")
ji="mefghal"
print(hii+ji)
print(ji.upper().isupper())
hii=len("hello")
print(hii)
print(ji[0])
print(ji.index("ghal"))
print(ji.replace("ghal","hii"))
print("2")
print(2.098)
print(-567)
print(8+9.87)
x=9
print(8+(x+2))
print(str(x)+"hii")
print(pow(5,8))
print(round(5.8))
from math import *
print(floor(3.7))
print(sqrt(36))
print(isqrt(36))
#name=input("enter your name")
#print("hello"+name+"!")
#num1=int(input("enter 1no"))
#num2=int(input("enter 2no"))
#num3=num1 + num2
#print(num3)
friends=["hii","hello","meghal","oscar","toby"]
print(friends[-1][3])
print(friends[-2:])
print(friends[1:3])
print(friends[:3])
friends[1]="mike"
print(friends[1])
cor=[(1,2),(6,0),(7,5)]
print(cor[-1][-2])
def hello():
    print("hello")
hello()
def cube(num):
    str(num*num*num)
print(cube(3))
i=1
while i<=20:
    print(i*i)
    i=i*2
def power(num,power):
    result=1
    for i in range(power):
        result=result*num
    return result
print(power(2,3))
numer=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for i in numer:
    for j in i:
        print(j)
 employee=open("hii.txt","r")
