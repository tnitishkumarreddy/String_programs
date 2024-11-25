s=input()
c=0
v='aeiouAEIOU'
for i in s:
    if i.isalpha() and i not in v:
        c+=1
print(c)


'''  input='nitish@1'
iteration 1: it will fetch 'n' check it is digit or not true and check it is consonant or not true  so increment c by 1 c=1
iteration 2: it will fetch 'i' check it is digit or not true and check it is consonant or not false so still c=1
iteration 3: it will fetch 't' check it is digit or not true and check it is consonant or not true  so increment c by 1 c=2
iteration 4: it will fetch 'i' check it is digit or not true and check it is consonant or not false so still c=2 
iteration 5: it will fetch 's' check it is digit or not true and check it is consonant or not true  so increment c by 1 c=3
iteration 6: it will fetch 'h' check it is digit or not true and check it is consonant or not true  so increment c by 1 c=4
iteration 7: it will fetch '@' check it is digit or not false so still c=4
iteration 8: it will fetch '1' check it is digit or not false so still c=4
'''
