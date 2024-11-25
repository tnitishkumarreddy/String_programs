s=input()
su=0
for i in s:
    if i.isdigit() and int(i)%2==0:
        su+=int(i)
print(su)

''' input='n123i'
iteration 1: it will fetch 'n' check 'n' is digit or not false so still su=0
iteration 2: it will fetch '1' check '1' is digit or not true and check int('1') is even or not false so still su=0
iteration 3: it will fetch '2' check '2' is digit or not true and check int('2') is even or not true so add 2 to su su=2
iteration 4: it will fetch '3' check '3' is digit or not true and check int('3') is odd or not false so still su=2
iteration 5: it will fetch 'i' check 'i' is digit or not false so still su=2



'''
