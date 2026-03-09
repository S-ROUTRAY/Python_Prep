# Python Program to Check if a String is a Pangram or Not
s=input('enter a string')
alphabets='abcdefghijklmnopqrstuvwxyz'
def check(s):
    return set(alphabets)-set(s.lower())==set()

if (check(s)==True):
    print('this is a pangram ')
else:
    print('this is not a pangram')
    
# Python Program to Remove Odd Indexed Characters in a string
def odc(s):
    new=''
    for i in range(1,len(s),2):
        new+=s[i]
    print(new)
odc(input('enter string: '))

# Python Program to Remove the nth Index Character from a Non-Empty String
n=int(input('enter index position: '))
s=input('enter string')
print(s.replace(str(s[n]),input('specified char: '),1))

# Python Program to Replace All Occurrences of ‘a’ with $ in a String
# type-1
s=input('enter a string: ')
print(s.replace('a','$'))
# type-2
def rep(s):
    new=''
    for ele in s:
        if ele =='a':
            new+='$'
        else:
            new+=ele
    print(new)
rep(input('enter a string: '))

# Python Program to Replace Every Blank Space with Hyphen in a String
# type:1
print("-".join((input().strip()).split()))
# type:2
s=input('enter a string: ')
print(s.replace(' ','-'))

# Python Program to Reverse a String using Recursion
def rev(s):
    return s[::-1]
print(rev(input('enter s string: ')))

# Python Program to Reverse a String Without using Recursion
s=input()
print(s[::-1])

# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
def occour(s):
    l=input('enter char: ')
    return s.count(l)
print(occour(input('enter sentence: ')))

# Python Program to Find the Length of a String without Library Function
def findLen(s):
    len=0
    for i in s:
        len+=1
    return len
print(findLen(input()))

# Python Program to Count the Number of Words and Characters in a String
def countWordChar(s):
    no_of_word=len(s.split())
    no_of_char=len(s)
    print(f'word={no_of_word},char={no_of_char}')
countWordChar(input('enter sentence: '))

# Python Program to Count Number of Lowercase Characters in a String
def countLower(s):
    count=0
    for i in s:
        if i.islower():
            count+=1
    return count
print(countLower(input('enter the string: ')))

# Python Program to Count the Number of Vowels in a String
def countVowel(s):
    vl=[]
    for ele in s :
        if ele in 'AEIOUaeiou'and ele not in vl:
            vl.append(ele)
    return len(vl)
print(countVowel(input('enter the string: ')))
        
# Python Program to Count Number of Uppercase and Lowercase Letters in a String
def coUpLow(s):
    ucount=0
    lcount=0
    for ele in s:
        if ele.isalpha():
            if ele.isupper():
                ucount+=1
            else:
                lcount+=1
    print(f'uppercases:{ucount} and lowercases{lcount}')
coUpLow(input('enter a string'))

# Python Program to Count the Number of Digits and Letters in a String
def coDigLet(s):
    dcount=0
    lcount=0
    for ele in s:
        if ele.isdigit():
            dcount+=1
        elif ele.isalpha():
            lcount+=1
    return 'digits={},letters={}'.format(dcount,lcount)
print(coDigLet(input('enter string: ')))

# Python Program to Check if the Substring is Present in the Given String
def match(s):
    substr=input('substr: ')
    count=0
    ip=0
    while ip<len(s):
        if substr==s[ip:ip+len(substr):1]:
            count+=1
            ip+=1
        else:
            ip+=1
    return count
print(match(input('str: ')))

# Python Program to Find Common Characters in Two Strings
# type1:
def common(s1,s2):
    cele=set()
    for ele1 in s1:
        if ele1 in s2:
            cele.add(ele1)
    return cele
print(common(input('str1: '),input('str2: ')))
# type:2
set1=set(input('enter str1: '))
set2=set(input('enter str2: '))
res=set1.intersection(set2)
print(res)

# Python Program to Print All Letters Present in Both Strings
def common(s1,s2):
    cele=set()
    for ele1 in s1:
        if ele1.isalpha() and ele1 in s2:
            cele.add(ele1)
    return cele
print(common(input('str1: '),input('str2: ')))

# Python Program that Displays which Letters are in First String but not in Second
def common(s1,s2):
    uncele=set()
    for ele1 in s1:
        if ele1.isalpha() and ele1 not in s2:
            uncele.add(ele1)
    return uncele
print(common(input('str1: '),input('str2: ')))

# Python Program that Displays Letters that are not Common in Two Strings
def uncommon(s1,s2):
    return set(s1).symmetric_difference(set(s2))
unc=(uncommon(input('str1:'),input('str2:')))
l=[]
for letter in unc:
    if letter!=' ':
        l.append(letter)
print(l)

# Python Program to Create a New String Made up of First and Last 2 Characters
def newStr(s):
    new=''
    for ip in range(len(s)):
        if ip==0 or ip==1 or ip==len(s)-2 or ip==len(s)-1:
            new+=s[ip]
    return new
print(newStr(input('str: ')))

# Python Program to Find the Larger String without using Built-in Functions
def large(s1,s2):
    s1len=0
    s2len=0
    for i in s1:
        s1len+=1
    for j in s2:
        s2len+=1
    if s1len==s2len:
        return 'same length'
    elif s1len>s2len:
        return 's1 is big'
    else:
        return 's2 is big'
print(large(input('s1: '),input('s2: ')))

# Python Program to Swap the First and the Last Character of a String
def swap(s):
    l=[i for i in s]
    ip=0
    while ip==0:
        l[ip],l[len(s)-1]=l[len(s)-1],l[ip]
        ip+=1
    print(''.join(l))
swap(input('str: '))
    
# Python Program to Sort Hyphen Separated Sequence of Words in Alphabetical Order
print(sorted(input('enter hypen separated words: ').split('-')))

# Python Program to Count the Occurrences of Each Word in a String
def occourance(s):
    wd={}
    for word in s.split():
        if word not in wd:
            wd[word]=1
        elif word in wd:
            wd[word]+=1
    for key in wd:
        if wd[key]==max(wd.values()):
            return key
print(occourance(input('str1: ')))

# Python Program to Count Number of Vowels in a String using Sets
def countVowel(s):
    vowel={'a','e','i','o','u'}
    count=0
    for ele in s:
        if ele in vowel:
            count+=1
    return count
print(countVowel(input('str1: ')))

# Python Program to Check if a Given String is Palindrome
def palindrome(s):
    return s[::-1]
string=input('str:')
rev=(palindrome(string))
if string==rev:
    print('palindrome')
else:
    print('not palindrome')
    
# Python Program to Check whether two Strings are Anagrams
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'anagram'
    else:
        return 'not anagram'
print(anagram(input('str1: '),input('str2: ')))

# Python Program to Find All Odd Palindrome Numbers in a Range without using Recursion
def palindrome(s):
    for num in range(s):
        if num%2!=0 and num==int(str(num)[::-1]):
            print(num)
palindrome(int(input('enter a range: ')))