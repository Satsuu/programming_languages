try:
    #Allow the user to input many values
    value = list(map(int, input("Enter values that you want to multiply: ").split(',')))
    #Place holder for my list 
    total = 1
    for i in value:
        #Multiplication
        total *= i
    print ("Product:", total)
    
except ValueError:
    print ("Invalid Input!")
    quit()
    





