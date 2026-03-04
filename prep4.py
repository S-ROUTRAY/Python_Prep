# Python Program to Print Table of a Given Number
n=int(input('enter a number: '))
for i in range (1,11):
    print(f'{n}*{i}={n*i}')
    
# Python Program to Calculate Grade of a Student
def grade(percentage):
    if percentage>=90:
        return 'A1'
    elif percentage>=70 and percentage<90:
        return 'A2'
    elif percentage>=60 and percentage<70:
        return 'B1'
    elif percentage>=50 and percentage<60:
        return 'B2'
    elif percentage>=30 and percentage<50:
        return 'C'
    else:
        return 'Fail'
totalmark=int(input('enter total mark'))
mark=int(input('enter secured mark'))
percentage=(mark*100)/totalmark
print(grade((percentage)))

# Python Program to Check Whether a given Year is a Leap Year

def leapYear(Y):
    if Y%100!=0 and Y%4==0:
        return "leapYear non centurian"
    elif Y%400==0:
        return 'leapYear centurian'
    else:
        return 'not a leapYear'
print(leapYear(int(input('enter Year: '))))

# Python Program to Convert Centimeters to Feet and Inches

def cmToinchTofeet(cm):
    inch=cm/2.54
    feet=cm/30
    print(round(inch,2))
    print(round(feet,2))
    
cmToinchTofeet(int(input()))

# Python Program to Read a Number n and Compute n+nn+nnn

n=int(input('enter the number'))
nn=str(n)*2
nnn=str(n)*3
print(n+int(nn)+int(nnn))

# Python Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order

print('-'.join(sorted(input('enter the string: ').split())))

# Python Program to Count the Occurrences of Each Word in a String

d={}
def count(s1):
    for word in s1.split():
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
count(input('s1: '))
for key,value in d.items():
    print(key,value)

# Python Program to Count Number of Vowels in a String using Sets

def count(s1):
    s={'a','e','i','o','u'}
    c=0
    for char in s1:
        if char in s:
            c+=1
    return c
print(count(input('s1: ')))

# Python Program to Check if a Given String is Palindrome

def pali(s1):
    return s1=="".join(reversed(s1))
print(pali(input('s1: ')))
    
# Python Program to Check whether two Strings are Anagrams

def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        return sorted(s1)==sorted(s2)
print(anagram(input('s1:'),input('s2:')))

# Python Program to Check whether a String is Palindrome or not using Recursion

def strRecur(s):
    return s==s[::-1]

string=input('enter a string: ')
print(strRecur(string))

# Python Program to Find All Odd Palindrome Numbers in a Range without using Recursion

lr=int(input('enter the lower range:'))
ur=int(input('enter the upper range:'))

if lr%2==0:
    lr+=1
for num in range(lr,ur+1,2):
    temp=num
    rn=0
    while temp>0:
        rn=rn*10+(temp%10)
        temp//=10
    if rn==num:
        print(f'{num} odd palindrome')
    else:
        print(f'{num} odd but not palindrome')
