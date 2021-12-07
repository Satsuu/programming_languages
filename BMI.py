class BMI:
    def calcBMI (*args):
        return args[0]/((args[1])/100)**2

    def printBMI(calculate): 
        if calculate <= 18.5:
            print ("Underweight")
        elif calculate <= 24.9:
            print ("Normal Weight")
        elif calculate <= 29.9:
            print ("Overweight")
        elif calculate <= 34.9:
            print ("Obesity class I")
        elif calculate <= 39.9:
            print ("Obesity class II")
        else:
            print ("Obesity class III")

if __name__ == "__main__":
    height = float(input("Enter height in cm: "))
    weight = float(input("Enter weight in kg: "))
    
    calculate = BMI.calcBMI(weight, height)
    print (f"Your BMI is {calculate: .3f}")
    BMI.printBMI(calculate)

    