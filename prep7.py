# Python Program to Create Dictionary from an Object
class Dict():
    def __init__ (self,A,B):
        self.key1=A
        self.key2=B
        
    def DictPrint(self):
        print(self.__dict__)
        
ob=Dict(12,13)
ob.DictPrint()

# Python Program to Check if a Key Exists in a Dictionary or Not
d=eval(input('enter a dictionary: '))
key=input('enter key: ')
if d.setdefault(key)==None:
    print('no such key found')
else:
    print(f'the value for that key is {d[key]}')
    
# Python Program to Add a Key-Value Pair to the Dictionary
d=eval(input('enter a dictionary: '))
d1=eval(input('new key value pair as dictionary: '))
d.update(d1)
print(d)

# Python Program to Find the Sum of All the Items in a Dictionary
print(sum(eval(input('enter a dictionary: ')).values()))

# Python Program to Multiply All the Items in a Dictionary
d=eval(input('enter a dictionary: '))
mul=1
for key,value in d.items():
    mul*=value
print(mul)

# Python Program to Remove a Key from a Dictionary
d=eval(input('enter a dictionary: '))
key=input('enter a key: ')
if d.get(key)==None:
    print('there is no such key is present: ')
else:
    print(d.pop(key))
print(d)
    
# Python Program to Concatenate Two Dictionaries
d1=eval(input('enter the 1st dict: '))
d2=eval(input('ente rthe second dictionary: '))
d1.update(d2)
print(d1)

# Python Program to Map Two Lists into a Dictionary
k=eval(input('enter the keys: '))
v=eval(input('enter the values: '))
print({key:value for key,value in zip(k,v)})

print(dict(zip(k,v)))

# Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character
lst_str=eval(input('enter 1st character of list: '))
print({i[0]:i for i in lst_str})

# Python Program to Create Dictionary that Contains Number
ul=int(input())
print({i:i*i for i in range(1,ul)})

# Python Program to Count the Frequency of Each Word in a String using Dictionary
def freqWd(s):
    wl=s.split()
    wd={}
    for word in wl:
        if word not in wd:
            wd[word]=1
        elif word in wd:
            wd[word]+=1
    for key,value in wd.items():
        print(f'word is {key} and frequency is {value}')
freqWd(input('enter a sentence: '))


