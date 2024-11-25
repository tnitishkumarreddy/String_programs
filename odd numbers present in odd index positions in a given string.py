
'''a=input()
for i in range(len(a)):
    if a[i].isdigit():
        if i%2==0:
            if int(a[i]%2==1):
                 print(a[i])'''




'''a=input()
for i in range(len(a)):
    if a[i].isdigit():
        if int(a[i])%2!=0 and i%2!=0:
            print(a[i])'''


s=input()
for i in range(1,len(s),2):
    if s[i].isdigit() and int(s[i])%2!=0:
        print(s[i])

''' s='hai1243655'

iteration 1: it will extract 1 and check s[1]='a' is digit or not false
iteration 2: it will extract 3 and check s[3]='1' is digit or not true and check int('1') is odd or not true so print s[3]='1'
iteration 3: it will extract 5 and check s[5]='4' is digit or not true and check int('4') is odd or not false so dont print it.
iteration 4: it will extract 7 and check s[7]='6' is digit or not true and check int('6') is odd or not false so dont print it.
iteration 5: it will extract 9 and check s[9]='5' is digit or not true and check int('5') is odd or not true so print s[9]='5'
'''
