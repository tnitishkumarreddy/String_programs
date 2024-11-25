s=input()
n=''
for i in range(len(s)-1,-1,-1):
    n+=s[i]
print(n)

'''
s=input()
rev=''
for i in s:
    rev=i+rev
print(rev)'''

'''s='hello'
len(s)=5
iteration 1: it will extract 5-1=4 index element s[4]='o' and add it n='' so n='o'
iteration 2: it will extract 4-1=3 index element s[3]='l' and add it n='o' so n='ol'
iteration 1: it will extract 3-1=2 index element s[2]='l' and add it n='ol' so n='oll'
iteration 1: it will extract 2-1=1 index element s[1]='e' and add it n='oll' so n='olle'
iteration 1: it will extract 1-1=0 index element s[0]='h' and add it n='olle' so n='olleh'

'''
