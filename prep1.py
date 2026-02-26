# # Python Program to Check Whether a Given Number is Even or Odd using Recursion
# def evenOdd(n):
#     if n%2==0:
#         print('even')
#     else:
#         print('odd')
# evenOdd(int(input('enter number: ')))

# # Python Program to Check Whether a Number is Positive or Negative
# def posNeg(n):
#     if n>0:
#         print('positive')
#     else:
#         print('negative')
# posNeg(int(input('enter a number: ')))
# Python Program to Print All Odd Numbers in a Range


# # Python Program to Check if a Number is a Palindrome
# n=int(input('enter a number: '))
# temp=n
# rev=0
# while temp>0:
#     rem=temp%10
#     rev=(rev*10)+rem
#     temp//=10
# if rev==n:
#     print('palindrome')
# else:
#     print('not a palindrome')

# # Python Program to Reverse a Number
# def revnum(n):
#     rev=0
#     while n>0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# reverse=revnum(int(input('enter a number')))
# print(reverse)
        
# # Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3
# def num(n):
#     if n%2==1 and n%3==1:
#         print(n)
#     else:
#         print('not a number')
# num(int(input('enter a number: ')))

# # Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range

# print(list(filter(lambda x:x%5==0 and x%7==0,[i for i in range(int(input('lower limit')),(int(input('upper limit'))),1)] )))

# # Python Program to Print All Numbers in a Range Divisible by a Given Number

# y=int(input('give the number'))
# print(list(filter(lambda x:x%y==0,[i for i in range (int(input('lower limit:')),int(input('upperlimit:')),1)])))

# # Python Program to Find Sum of Digits of a Number

# n=int(input('enter a number'))
# summ=0
# while n>0:
#     summ+=n%10
#     n//=10
# print(summ)
    
# # Python Program to Find Sum of Digit of a Number using Recursion
# def recursive_summ(n):
#     if n==0:
#         return 0
#     else:
#         return (n%10)+recursive_summ(n//10)
# res=recursive_summ(123456)
# print(res)

# # Python Program to Find Sum of Digit of a Number Without Recursion
# def summ(n):
#     add=0
#     while n>0:
#         add+=n%10
#         n//=10
#         if n<=0:
#             return add
# res=summ(123456)
# print(res)

# # Python Program to Count the Number of Digits in a Number
# n=int(input('enter a number:'))
# l=[]
# while n>0:
#     l.append(n%10)
#     n//=10
# print(len(l))

# # Python Program to Find All the Divisors of an Integer

# n=int(input('enter the number'))
# l=[]
# for div in range(2,n//2+1):
#     if n%div==0:
#         l.append(div)
# print(l)

# # Python Program to Find the Smallest Divisor of an Integer

# n=int(input('enter the number'))
# l=[]
# for div in range(2,n//2+1):
#     if n%div==0:
#         l.append(div)
# print(min(l))

