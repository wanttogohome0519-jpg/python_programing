a=5   # 0000 0101
b=3   # 0000 0011
print(a&b)   # 0000 0001 -> 1
print(a|b)   # 0000 0111 -> 7
print(a^b)   # 0000 0110 -> 6
print(a<<b)  # 0010 1000 -> 40
print(a>>b)  # 0000 0001 -> 1
print( 40>>b) # 0000 0101 -> 5
print(~a)

print("a" in "apple")
print( 3 in [1,2,3,4,5])
max_num= a if a>b else b
print(max_num)
c= "짝수" if a%2==0 else "홀수"
print(c)

score=85
print("A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D" if score>=60 else "F")
