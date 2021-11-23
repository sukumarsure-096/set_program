'''
s = set()
for i in range(1,21):
    #if i%2==0:
        s.add(i)
print(s)
for j in range(1,21):
    if j%2==0:
        s.discard(j)
print(s)
'''
d = set()
n = int(input('enter n :'))
for i in range(1,n):
    d.add(int(input('values :')))
print(d)
