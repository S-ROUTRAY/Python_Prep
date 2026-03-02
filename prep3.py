# Python Program to Check Whether a Number is Positive or Negative
N=int(input('enter the number: '))
if N==0:
    print(f'{N} is zero')
    
elif N<0:
    print(f'{N} is negative number')

else:
    print(f'{N} is positive number')

# Python Program to Print All Odd Numbers in a Range
SL=int(input('enter the starting limit:'))
EL=int(input('enter the ending limit:'))
if SL%2==0:
    SL+=1

# using for loop
for num in range(SL,EL+1,2):
    print(num)

# using while loop
while SL<=EL:
    print(SL)
    SL+=2

# Python Program to Check if a Number is a Palindrome
N=int(input('enter the number: '))
RN=0
temp=N
while temp>0:
    r=temp%10
    temp=temp//10
    RN=RN*10+r
if RN==N:
    print('number is palindrome')
else:
    print('not palindrome')

# Python Program to Reverse a Number
N=int(input('enter the number: '))
RN=0
temp=N
while temp>0:
    r=temp%10
    temp=temp//10
    RN=RN*10+r
print(f'the reverse of number{N} is {RN}')

# Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3

N=int(input('enter the digit: '))
for num in range(N+1):
    if num%2!=0 and num%3!=0:
        print(num)
        
# Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range
SLI=int(input('enter the digit for starting limit: '))
ELI=int(input('enter the digit for ending limit: '))

# with for loop
for num in range(SLI,ELI+1):
    if num%7 ==0 and num%5==0:
        print(num)
    else:
        print(f'{num} is not divisible by 7 and 5 both')
        
# with while loop
while SLI<ELI:
    if SLI%7==0 and ELI%5==0:
        print(SLI,'divisible by 7 and 5')
    else:
        print(f'{SLI} is not divisible by 7 and 5 both')
    SLI+=1


# Python Program to Print All Numbers in a Range Divisible by a Given Number
N=int(input('enter the number: '))
SV=int(input('enter the start: '))
EV=int(input('enter the end: '))
# using for loop
for num in range(SV,EV+1):
    if num%N==0:
        print(num)
#using while loop:
while SV<=EV:
    if SV%N==0:
        print(SV)
    SV+=1
    
# Python Program to Find Sum of Digits of a Number
N=int(input('enter the number: '))
summ=0
temp=N
while temp>0:
    r=temp%10
    temp=temp//10
    summ+=r
print(summ)

# Python Program to Count the Number of Digits in a Number
N=int(input('enter the number: '))
count=0
temp=N
while temp>0:
    r=temp%10
    temp=temp//10
    count+=1
print(count)

# Python Program to Find All the Divisors of an Integer
N=int(input('enter the number: '))
for num in range(2,(N//2)+1):
    if N%num==0:
        print(num)

# Python Program to Find the Smallest Divisor of an Integer
N=int(input('enter the number: '))
D=[]
for num in range(2,(N//2)+1):
    if N%num==0:
        D.append(num)
print(D[0])

# Python Program to Print Table of a Given Number
N=int(input('enter the number: '))
for num in range(1,11):
    print(f'{N}*{num}={N*num}')

# Python Program to Calculate Grade of a Student
grade=int(input('enter grade: '))
if grade<30:
    print('fail')
elif grade<=50 and grade>=30:
    print('third class')
elif grade>50 and grade<60:
    print('2nd class')
else:
    print('first class')
    
# Python Program to Check Whether a given Year is a Leap Year
Year=int(input('enter the year'))
if Year%100!=0 and Year%4==0:
    print(f'{Year}is the leap year')
elif Year%400==0:
    print(f'{Year} is the leap year')
else:
    print('the year is not a leap year')

# Python Program to Convert Centimeters to Feet and Inches
cm=int(input('enter the centemeter: '))
inch=(12/30)*cm
feet=(1/30)*cm
print(feet)
print(inch)

# Python Program to Read a Number n and Compute n+nn+nnn
n=input('enter the ')
summ=0
i=1
# for i in range(1,4):
while i<=3:
    summ+=int(n*i)
    i+=1
print(summ)