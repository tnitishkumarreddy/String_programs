from itertools import permutations

s=input()
for length in range(1,len(s)+1):
    pe=permutations(s,length)
    for p in pe:
        print("".join(p))


