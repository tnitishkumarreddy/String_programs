s=input()
v='aeiouAEIOU'
for i in range(len(s)):
    if s[i] in v:
        print(i)


''' input s='hai python'

iteration 1: it will extract 'h' and check it is in vowels or not false so dont print anything
iteration 2: it will extract 'a' and check it is in vowels or not true so print its index position which is 1
iteration 3: it will extract 'i' and check it is in vowels or not true so print its index position which is 2
iteration 4: it will extract ' ' and check it is in vowels or not false so dont print anything
iteration 5: it will extract 'p' and check it is in vowels or not false so dont print anything
iteration 6: it will extract 'y' and check it is in vowels or not false so dont print anything
iteration 7: it will extract 't' and check it is in vowels or not false so dont print anything
iteration 8: it will extract 'h' and check it is in vowels or not false so dont print anything
iteration 9: it will extract 'o' and check it is in vowels or not true so print its index position which is 8
iteration 10: it will extract 'n' and check it is in vowels or not false so dont print anything

