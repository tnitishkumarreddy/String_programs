s=input()
e,o=0,0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            e+=1
        else:
            o+=1
print(e,o)

''' input='n123i'
iteration 1: it will fetch 'n' check 'n' is digit or not false so still e=0 and o=0
iteration 2: it will fetch '1' check '1' is digit or not true and check int('1') is even or odd it is odd so still e=0 and o=1
iteration 3: it will fetch '2' check '2' is digit or not true and check int('2') is even or odd it is even so e=1 and  c=1
iteration 4: it will fetch '3' check '3' is digit or not true and check int('3') is even or odd it is a odd so increment c from 1 to 2 so c=2 and e=1
iteration 5: it will fetch 'i' check 'i' is digit or not false so o=2 and e=1
'''
