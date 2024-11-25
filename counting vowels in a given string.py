s=input()
c=0
v='aeiouAEIOU'
for i in s:
    if i in v:
        c+=1
print(c)


'''  input='nitish@1'
iteration 1: it will fetch 'n' check it is vowel or not false  so still c=0
iteration 2: it will fetch 'i' check it is vowel or not true  so increment c by 1 so c=1
iteration 3: it will fetch 't' check it is vowel or not false  so still c=1
iteration 4: it will fetch 'i' check it is vowel or not true  so increment c so c=2
iteration 5: it will fetch 's' check it is vowel or not false  so still c=2
iteration 6: it will fetch 'h' check it is vowel or not false  so still c=2
iteration 7: it will fetch '@' check it is vowel or not false  so still c=2
iteration 8: it will fetch '1' check it is vowel or not false  so still c=2
'''
