def rev(s):
    r=''
    for i in s:
        r=i+r
    rr=''
    for i in range(len(r)):
        if i%2==0:
            rr+=str(i)
        else:
            rr+=r[i]
    print(rr)
rev('harshad')

def reverse(st):
    l=[]
    for i in st:
        l.insert(0,i)
    for i in range(0,len(l),2):
        l[i]=i
    for i in l:
        print(i,end='')
reverse('harshad')


