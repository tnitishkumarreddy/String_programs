s=input()
l=s.split()
mrw=''
c=0
for i in l:
    if l.count(i)>c:
        mrw=i
        c=l.count(i)
print(mrw)


''' input= 'python is scripted and python dynamic'

l contains words of s that is l=['python','is','scripted','and',python','dynamic']

iteration 1: it will extract 'python' and check count of 'pyhon' is greater than c=0(2>0) true so iam reassigning mrw='pyhton' and c=2
iteration 2: it will extract 'is' and check count of 'is' is greater than c=2(1>2) false so still mrw='pyhton' and c=2
iteration 3: it will extract 'scripted' and check count of 'scripted' is greater than c=2(1>2) false so still mrw='pyhton' and c=2
iteration 4: it will extract 'and' and check count of 'and' is greater than c=2(1>2) false so still mrw='pyhton' and c=2
iteration 5: it will extract 'python' and check count of 'python' is greater than c=2(2>2) false so still mrw='pyhton' and c=2
iteration 6: it will extract 'dynamic' and check count of 'dynamic' is greater than c=2(1>2) false so still mrw='pyhton' and c=2

at last print most repeated word mrw as 'python'

'''



