s=input()
l=s.split()
lw=l[0]
for i in l:
    if len(i)>len(lw):
        lw=i
print(lw)


''' input ='python is a scripted lang'

l=['python','is','a','scripted','lang']
l[0]='python'

iteration 1: it will extract 'python' and check length of 'python'(6) is greater than length of 'python'(6) false so still lw='pyhton'
iteration 2: it will extract 'is' and check length of 'is'(2) is greater than length of 'python'(6) false so still lw='pyhton'
iteration 3: it will extract 'a' and check length of 'a'(1) is greater than length of 'python'(6) false so still lw='pyhton'
iteration 4: it will extract 'scripted' and check length 'scripted'(8) is greater than length of 'python'(6) true so  lw='scripted'
iteration 5: it will extract 'lang' and check length of 'lang'(4) is greater than length of 'scripted'(8) false so still lw='scripted'

at last print most repeated word mrw as 'scripted'

'''
