score = int(input("Enter your score: "))
if score > 100:
    grade = "Please enter correct digit"
elif score >= 85:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 65:
    grade = "C"
elif score >= 55:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("your grade is: ", grade)
