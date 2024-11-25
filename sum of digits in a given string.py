s=input()
su=0
for i in s:
    if i.isdigit():
        su+=int(i)
print(su)



'''
input='ni123t
iteration 1: it will fetch 'n' so i='n' check 'n' is digit or not false so still su=0
iteration 2: it will fetch 'i' so i='i' check 'i' is digit or not false so still su=0
iteration 3: it will fetch '1' so i='1' check '1' is digit or not true so convert string of 1 to integer and add to su so su=1
iteration 4: it will fetch '2' so i='2' check '2' is digit or not true so convert string of 2 to integer and add to su so su=3
iteration 5: it will fetch '3' so i='3' check '3' is digit or not true so convert string of 3 to integer and add to su so su=6
iteration 6: it will fetch 't' so i='t' check 't' is digit or not false so still su=6

'''
