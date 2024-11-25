s=input()
m=''
c=0
for i in s:
    if s.count(i)>c:
        m=i
        c=s.count(i)
print(m)


''' input='harshad'

iteration 1: it will fetch 'h' and check count of 'h' (which is 2) is greater than c=0 true so reassign m with 'h' and update c with count of 'h' so c=2
iteration 2: it will fetch 'a' and check count of 'a' (which is 2) is greater than c=2 false so stll m='h' and c=2
iteration 3: it will fetch 'r' and check count of 'r' (which is 1) is greater than c=2 false so stll m='h' and c=2
iteration 4: it will fetch 's' and check count of 's' (which is 1) is greater than c=2 false so stll m='h' and c=2
iteration 5: it will fetch 'h' and check count of 'h' (which is 2) is greater than c=2 false so stll m='h' and c=2
iteration 6: it will fetch 'a' and check count of 'a' (which is 2) is greater than c=2 false so stll m='h' and c=2
iteration 7: it will fetch 'd' and check count of 'd' (which is 1) is greater than c=2 false so stll m='h' and c=2

at last print maximum repeated element m as 'h' so m='h'

'''

        
