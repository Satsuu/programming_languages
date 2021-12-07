def addition(input1, input2):
    return (input1 + input2)
def subtraction(input1, input2):
    return (input1 - input2)
def multiplication(input1, input2):
    return (input1 * input2)
def division(input1, input2):
    return (input1 / input2)

while True:
    input1 = int(input("Enter Number: "))
    input2 = int(input("Enter Number: "))

    print ("Choose operation: \n 1 - addition\n 2 - subtraction\n 3 - multiplication\n 4 - division\n")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print (input1, "+", input2, "=", addition(input1,input2))
    elif choice == 2:
        print (input1, "-", input2, "=", subtraction(input1,input2))
    elif choice == 3:
        print (input1, "*", input2, "=", multiplication(input1,input2))
    elif choice == 4:
        print (input1, "/", input2, "=", division(input1,input2))
    else:
        print ("Invalid Input") 

    retry = int(input("Do you want to try again? [1] - Yes\n \t[2] - No: "))
    if retry == 2:
        break