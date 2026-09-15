for i in range(0,4):
    print(i)
print()

a = range(5)
for i in a:
    print(i)
print(a.start, a.stop, a.step)

for i in range(0,11,2):
    print(i, end=" ")
print()

for i in range(5,0,-1):
    print(i, end=" ")
print()
total=0
for i in range(1,11):
    total+=i
print(total)
print(sum(range(1,11)))
s="hi123123123"

for c in s:
    print(c, end=" ")
print(len(s))



for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end="\t")
    print()
