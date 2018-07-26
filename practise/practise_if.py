length = float(input("input length:"))
weight = float(input("input weight:"))
bmi = weight/length**2
print(bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
elif bmi >= 32:
    print("严重肥胖")
