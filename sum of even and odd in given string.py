s=input()
es,os=0,0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            es+=int(i)
        else:
            os+=int(i)
print(e,o)

''' input='n123i'
iteration 1: it will fetch 'n' check 'n' is digit or not false so still es=0 and os=0
iteration 2: it will fetch '1' check '1' is digit or not true and check int('1') is even or odd it is odd so add it to os so os=1
iteration 3: it will fetch '2' check '2' is digit or not true and check int('2') is even or odd it is even so add oit to es so es=2
iteration 4: it will fetch '3' check '3' is digit or not true and check int('3') is even or odd it is a odd so add it to os so os=1+3=4
iteration 5: it will fetch 'i' check 'i' is digit or not false so os=4 and es=2
'''
