def multi_table():
    print("This is a multiplication table generator.")

    def Multiplication(x, y):
        z = x * y
        return z

    NumberConstant = 0

    MultipliedNumber = int(input("Please give me a number to give you a multiplication table for: "))

    print("Here is your table")

    for x in range(12):
        NumberConstant += 1
        print("------------------------------------")
        print(f"This is your number multiplied by {NumberConstant}")
        print(f"{Multiplication(MultipliedNumber, NumberConstant)}")

    print("------------------------------------")