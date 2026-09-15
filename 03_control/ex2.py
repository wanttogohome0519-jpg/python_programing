#while 문
# 1~10까지의 반복 출력
i=1
while i<11:
    print(i)
    i+=1
    if i==5:
        break
else:
    print("End")

nums =[1,2,3,4,5]
target=2
i=0
while i <len(nums):
    print(nums[i])
    if nums[i] == target:
        print("Found")
        break
    i+=1
else:
    print("Not Found")
i=1
total=0
while i<=10:
    if i%2==0:
        total+=i
    i+=1
print(total)
#집에가고싶다.py