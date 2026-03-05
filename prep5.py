# # 1.Write a program to remove duplicates in list? 
# L=eval(input('enter the list elements'))
# DL=[]
# for ele in L:
#     if ele in DL:
#         continue
#     else:
#         DL.append(ele)
# print(DL)

# # oneline solution

# print(sorted(list(set(eval(input('enter a list'))))))
# # 2.Write a program to remove duplicates in string? 
# S=eval(input('enter the string: '))
# SL=''
# for i in S:
#     if i in SL:
#         continue
#     else:
#         SL+=i 
# print(SL)
# # 3.Write a program to print most repeated character in string? 
# S=eval(input('enter the string: '))
# RS={}
# for i in S:
#     if i not in RS:
#         RS[i]=1
#     elif i in RS:
#         RS[i]+=1

# maxi=max(RS.values())
# for s in RS:
#     if RS[s]==maxi:
#         print(s)
# # 4.Write a program to print most repeated word in sentence?
# senetence=input('enter a sentence:')
# WD={}
# SL=senetence.split()
# for word in SL:
#     if word not in WD:
#         WD[word]=1
#     elif word in WD:
#         WD[word]+=1
# maxi=max(WD.values())
# for word in WD:
#     if WD[word]==maxi:
#         print(word)

# # 5.Write a program to print most repeated element in list?
# LI=eval(input('enter a list'))
# LD={}
# for ele in LI:
#     if ele not in LD:
#         LD[ele]=1
#     elif ele in LD:
#         LD[ele]+=1
# maxi=max(LD.values())
# for k in LD:
#     if LD[k]==maxi:
#         print(k)
 
# # 6.Write a program to print lengthiest word in sentence? 
# sentence=input('enter a beautiful sentence: ')
# WD={}
# SL=sentence.split()
# for word in SL:
#     if word not in WD:
#         WD[word]=len(word)
    
# maxi=max(WD.values())
# for W in WD:
#     if WD[W]==maxi:
#         print(W)
# # 7.Prime number program 
# print(list(filter(lambda x: x>1 and all(x%i!=0 for i in range (2,x//2+1)),[i for i in range(2,int(input('enter a upperlimit:')),1)])))

# # 8.Program to swap two values 
# a=input('enter a value:')
# b=input('enter a value:')
# a,b=b,a

# #9.Factorial and Fibonacci with recursion and without recursion 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(int(input('enter a number:'))))

# #normal approach

# n=int(input('enter a number: '))
# fact=1
# for i in range(2,n+1):
#     if n==0 or n==1:
#         print(fact)
#         break
#     else:
#         fact*=i
# print(fact) 
    
# # 10.Input:- we are the programmers Output:-programmers the are we
# S='we are the programmers'
# print(' '.join(S.split()[::-1]))

# # 11.Input:- we are the programmers Output:-ew era eht sremmargorp 

# print(' '.join([i[::-1] for i in (input().split())]))

# # 12.Write a program to check weather the given number is palindrome or not? 
# def palindrome(n):
#     temp=n
#     new=0
#     while temp>0:
#         new=new*10+(temp%10)
#         temp//=10
#     if new==n:
#         return 'palindrome'
#     else:
#         return 'not a palindrome'
# print(palindrome(int(input('enter number: '))))

# # 13.Write a program to check weather the given string is palindrome or not?

# def palindrome(p):
#         if p==p[::-1]:
#             return 'palindrome'
#         else:
#             return 'not a palindrome'
# print(palindrome(input('enter a number: ')))

# # 14.Write a program to print highest value in list? 

# print(max(eval(input('enter a list: '))))

# print(sorted(eval(input('enter a list')),reverse=True)[0])

# import functools
# print(functools.reduce(lambda x,y: x if x>y else y,eval(input('enter a list:'))))

# # 15.Write a program to print second highest value in list? 

# print(sorted(eval(input('enter a list: ')))[-2])

# # 16.Write a program to print least value in list? 

# print(min(eval(input('enter a list: '))))

# # 17.Sort the given array without using built-in methods? 

# L=eval(input('enter a list: '))
# for n in range(len(L)):
#     for ip in range(1,len(L)):
#         if L[ip]<L[ip-1]:
#             L[ip],L[ip-1]=L[ip-1],L[ip]
# print(L)

# # 18.Write a program to swap first and last element in given list? 

# L=eval(input('enter a list'))
# for ip in range(len(L)):
#     if ip==0:
#         L[ip],L[-1]=L[-1],L[ip]
#         break
# print(L)

# # 19.Input:- aaabbcccdaabbb Output:-3a2b3c1d2a3b 

# S=input('enter string: ')
# S1=''
# C=1
# for ip in range(1,len(S),1):
#     if S[ip]==S[ip-1]:
#         C+=1
#     else:
#         S1=S1+str(C)+S[ip-1]
#         C=1
#     if ip==len(S)-1:
#         S1=S1+str(C)+S[ip]
# print(S1)


# # 20.Input:- ['kumar', 'somu', 'sonu', 'ram', 'raju'], Output:- {'k': 1, 's': 2, 'r': 2} 

# d={}
# for ele in eval(input('enter list: ')):
#     if ele[0] not in d:
#         d[ele[0]]=1
#     elif ele[0] in d:
#         d[ele[0]]+=1
# print(d)

# # 21.Write a program to sort numbers in list without using built-in methods?

# L=eval(input('enter a list: '))
# for n in range(len(L)):
#     for ip in range(1,len(L)):
#         if L[ip]<L[ip-1]:
#             L[ip],L[ip-1]=L[ip-1],L[ip]
# print(L)
