class Computation:

    def seriesOfNumber():
        value = input("Enter series of number using seperate using 'comma': ").split(',')
        emptyList = []
        for item in value:
            try:
                value = float(item)
                emptyList.append(value)
            except:
                print(f"Could not convert string to float {item}")
                continue
        return emptyList

    def addition (value):
        total = 0
        for i in value:
            total += i
        print (total)

    def subtraction (value):
        sub = value[0]
        for item in value[1:]:
            sub -= item
        print (sub)

if __name__ == '__main__':
    value = Computation.seriesOfNumber()

    choice = input('Select operator \n [1] Add [2] Subtract: ')
    if choice == '1':
        Computation.addition(value)
    elif choice == '2':
        Computation.subtraction(value)

   



        

