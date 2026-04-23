## Take the average of a student grades in a subject
## Show the lows marks and highest marks

marks = [50,60,65,55,70]
average = sum(marks)/len(marks)
print(f"{average:.0f}")
print(min(marks))
print(max(marks))