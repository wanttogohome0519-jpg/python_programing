a="python"
print(a,type(a))
print(" I'll be back")
print('I\'ll be back')

a="""
Life is short
You need Python
"""
print(a)

def func():
    """
    func() 함수에 대한 설명을 작성합니다.
    """
    pass
print(func.__doc__)


print("Hello"+"Python")

#문자열 반복
print("Hello"*3)
print("-"*50)
print("Hello"+10)
print("Hello"+str(10))
print("10"+"20")
print(int("10")+int("20"))

name="pororo"
age=23
print(f"이름:{name}, 나이:{age}")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")
pi=3.14159265358979
print(f"파이: {pi:.2f}")
print(f"파이: {pi:.0f}")
num=123456789
print(f"{num:,}")
print(f"{num:15d}")
