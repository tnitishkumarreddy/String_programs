s=input()                   #  taking string as a input
c=0                         # Assuming that the given string doesnt contain any digits so iam assigning c=0
for i in s:                 # iterating the given string by using for loop
    if i.isdigit():         # checking whether the fetched element is digit or not
        c+=1                # incrementing c value by 1 if the fetched element is only digit
print(c)                    # printing c value after completion of all iterations


''' input s='ni4ti23sh'
iteration 1: it will fetch 'n' so i='n' check 'n' is digit or not false so still c=0
iteration 2: it will fetch 'i' so i='i' check 'i' is digit or not false so still c=0
iteration 3: it will fetch '4' so i='4' check '4' is digit or not True so increment c by 1 so c becomes 1 (c=1)
iteration 4: it will fetch 't' so i='t' check 't' is digit or not false so still c=1
iteration 5: it will fetch 'i' so i='i' check 'i' is digit or not false so still c=1
iteration 6: it will fetch '2' so i='2' check '2' is digit or not True so increment c by 1 so c becomes 2 (c=2)
iteration 7: it will fetch '3' so i='3' check '3' is digit or not True so increment c by 1 so c becomes 3 (c=3)
iteration 8: it will fetch 's' so i='s' check 's' is digit or not false so still c=3
iteration 9: it will fetch 'h' so i='h' check 'h' is digit or not false so still c=3


after completion of all iterations print the value of c(3)'''

