# Python Program to Check if a String is a Pangram or Not

S=input('enter the string: ')
Alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ip=0
count=0
while ip<len(Alpha):
    if Alpha[ip] in set(S.upper()):
        count+=1
    ip+=1
if count==(len(Alpha)):
    print('this is a panagram')
else:
    print('this is not a panagram')


# optimised one

S=set(input('enter the string: ').lower())
if S.isalpha() and len(S)==26:
    print('pangram')
else:
    print('not pangram')
    
    
# Python Program to Remove Odd Indexed Characters in a string
S=input('enter the string')
ip=0
S1=''
while ip<len(S):
    S1+=S[ip]
    ip+=2
print(S1)

# 2nd approach
S=input('enter the string')
ip=1
while ip<len(S):
    S=S.replace(S[ip],'')
    ip+=2
print(S)

    
# Python Program to Remove the nth Index Character from a Non-Empty String
S=input('enter a a string: ')
ip=int(input('enter the index position '))
if len(S)>0 and len(S)>ip:
    S=S.replace(S[ip],'')
print(S)

# Python Program to Replace All Occurrences of ‘a’ with $ in a String
S=input('enter a a string: ')
while 'a' in S:
    S=S.replace('a','$') 
print(S)

# Python Program to Replace Every Blank Space with Hyphen in a String
S=input('enter a a string: ')
while ' ' in S:
    S=S.replace(' ','-') 
print(S)


# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
S=input('enter a a string: ')
char=input('enter a a string: ')
c=S.count(char) 
print(c)

# Python Program to Find the Length of a String without Library Function
S=input('enter a a string: ')
lenth=0
for ele in S:
    lenth+=1
print(lenth)

# Python Program to Count the Number of Words and Characters in a String
S=input('enter a a string: ')
lenth=0
countt=0
for ele in S:
    lenth+=1
    if ele==' ':
        countt+=1
print('number of words are :',countt+1)
print('number of characters are :',lenth)

# Python Program to Count Number of Lowercase Characters in a String
S=input('enter a a string: ')
countt=0
for ele in S:
    if ele.isalpha() and ele.islower():
        countt+=1
print('number of lower characters are :',countt)

# Python Program to Count the Number of Vowels in a String
S=input('enter a a string: ')
V='AEIOUaeiou'
countt=0
for ele in S:
    if ele in V:
        countt+=1
print('number of Vowels are :',countt)

# Python Program to Count Number of Uppercase and Lowercase Letters in a String
S=input('enter a a string: ')
lowc=0
upc=0
for ele in S:
    if ele.isalpha():
        if ele.isupper():
            upc+=1
        else:
            lowc+=1
print('number of upper characters are :',upc)
print('number of lowe characters are :',lowc)

# Python Program to Count the Number of Digits and Letters in a String
S=input('enter a a string: ')
c=0
for ele in S:
    if ele.isalnum():
        c+=1
print('Number of Digits and Letters are :',c)

# Python Program to Check if the Substring is Present in the Given String
S=input('enter the string: ')
SS=input('enter the string: ')
countt=0
for ip in range(len(S)-len(SS)+1):
    if S[ip:len(SS)+ip]==SS:
        countt+=1
if countt>0:
    print(f'the substring is present in sting {countt} times')
else:
    print('the substring is not present in the string')

# Python Program to Find Common Characters in Two Strings
S=set(input('enter the string: '))
S1=set(input('enter the string: '))
S3=S.intersection(S1)
print(S3)

# without typecasting
S=set(input('enter the string: '))
S1=set(input('enter the string: '))
L=[]
for ele in S:
    if ele in S1:
        L.append(ele)
print(L)
    
# Python Program to Print All Letters Present in Both Strings
S=set(input('enter the string: '))
S1=set(input('enter the string: '))
S3=''
for ele in S :
    if ele in S1 and ele.isalpha():
        S3+ele
print(S3)

# Python Program that Displays which Letters are in First String but not in Second
S=set(input('enter the string: '))
S1=set(input('enter the string: '))
S3=''
for ele in S :
    if ele not in S1 and ele.isalpha():
        S3+=ele
print(S3)

# Python Program to Create a New String Made up of First and Last 2 Characters
S=input('enter the string: ')
S1=''
for ip in range(len(S)):
    if ip<2 or ip>(len(S)-3):
        S1+=S[ip]
print(S1)
        
# Python Program to Find the Larger String without using Built-in Functions
S=set(input('enter the string: '))
S1=set(input('enter the string: '))
if S.issuperset(S1):
    print('S is grater than S1')
else:
    print('S1 is grater than S')

# Python Program to Swap the First and the Last Character of a String
S=input('enter the string: ')
ip=1
while ip==0:
    if ip==0:
        ele=S[ip]
        S.replace(S[ip],S[-1])
        S.replace(S[-1],ele)
print(S)
