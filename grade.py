count = 4
getTotal = 0
for i in range(count):
    grade = float(input("Enter Grade: "))
    getTotal += grade
avg = getTotal / 4
if avg < 60:
    print (str(avg) + " is Failed")
elif avg >= 60: 
    print (str(avg) + " is Passed")
else: 
    print ("Invalid Input")