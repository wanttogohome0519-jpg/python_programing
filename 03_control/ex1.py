score = 85
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("D")

grade = "A"
match grade:
    case "A":
        print("90점 이상")
    case "B":
        print("80점 이상")
    case "C":
        print("70점 이상")
    case _: # default
        
        print("60점 미만")
