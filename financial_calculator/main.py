#Max Holdaway Financial Calculator

#Function for the saving money part of the financial calculator
def SaveDeposits(AmountToSave, WeeklyOrMonthly, TotalSavingsGoal):
    #Seeing if the user chose Weekly or Monthly saving
    if WeeklyOrMonthly.lower() == "weekly":
        #How many weeks they need to save for to get their goal
        WeeksToSave = 1
        #A number used to determine how many weeks are needed to save
        WeeklySavings = AmountToSave
        #The loop used to find out how many weeks they need to save for
        while WeeklySavings != TotalSavingsGoal and WeeklySavings < TotalSavingsGoal:
            #Adding one to WeeksToSave
            WeeksToSave += 1
            #Adding more savings to the WeeklySavings variable to check if goal is met
            WeeklySavings += AmountToSave
        #Using the WeeksToSave variable
        return WeeksToSave
    #Seeing if the user chose Weekly or Monthly saving
    elif WeeklyOrMonthly.lower() == "monthly":
        #How many months they need to save for to get their goal
        MonthsToSave = 0
        #A number used to determine how many months are needed to save
        MonthlySavings = AmountToSave
        #The loop used to find out how many months they need to save for
        while MonthlySavings != TotalSavingsGoal and MonthlySavings < TotalSavingsGoal:
            #Adding one to MonthsToSave
            MonthsToSave += 1
            #Adding more savings to the MonthlySavings variable to check if goal is met
            MonthlySavings += AmountToSave
        #Using the MonthsToSave variable
        return MonthsToSave
    else:
        #If the user didn't choose anything correctly this is to compensate for that
        print("You did not choose Weekly or Monthly ")

#Function for calculating interest
def CompoundInterest(MoneyAmount, Interest, InterestTime):
    #Turning the interest into a percentage
    Interest = (Interest / 100)
    #Using a for loop to calculate interest
    for x in range(InterestTime):
        #Calculating the interest the user would gain based on the numbers
        MoneyAmount += (MoneyAmount * Interest)
    #Using the MoneyAmount variable
    return MoneyAmount

#Function for doing budgeting
def BudgetAllocator(MoneyAmount2):
    #Deciding what the percentage is for savings
    SavingsPercentage = 0.3
    #Deciding what the percentage is for food
    FoodPercentage = 0.6
    #Deciding what the percentage is for entertainment
    EntertainmentPercentage = 0.1
    #Calculating savings budget
    SavingsBudget = (MoneyAmount2 * SavingsPercentage)
    #Calculating food budget
    FoodBudget = (MoneyAmount2 * FoodPercentage)
    #Calculating entertainment budget
    EntertainmentBudget = (MoneyAmount2 * EntertainmentPercentage)
    #Putting the budgets into a list to be shown to the user
    BudgetList = [SavingsBudget, FoodBudget, EntertainmentBudget]
    #Using the BudgetList
    return BudgetList

#Function for calculating discounts
def SalesPriceCalculator(CostOfItem, Discount):
    #Turning the dicount into a percentage
    Discount = (Discount / 100)
    #Calculating the discount
    DiscountOfItem = CostOfItem * Discount
    #Applying the discount
    CostOfItem -= DiscountOfItem
    #Using the CostOfItem to show the user the discount
    return CostOfItem

#Function for calculating tip price
def TipCalculator(PriceOfItems):
    #Checking if the price is less than or equal to 50
    if PriceOfItems <= 50:
        #Having them do a 5 dollar tip
        Tip = 5
    #Checking if the price is greater than or equal to 51 and is less than or equal to 100
    elif PriceOfItems >= 51 and PriceOfItems <= 100:
        #Having them do a 10 dollar tip
        Tip = 10
    #Checking if the price is greater than or equal to 101
    elif PriceOfItems >= 101:
        #Having them do a 15 dollar tip
        Tip = 15
    #Using the tip
    return Tip

#The main function or user interface
def main():
    while True:
        #Getting the users decision on what they want to do
        UserDecision = int(input("""Which tool do you want to use? Type the numbers that they start with to choose said tool or option.
                                 1. Saving Deposits Calculator
                                 2. Interest Calculator
                                 3. Budgeting system
                                 4. Dicount Calculator
                                 5. Tip Calculator
                                 6. Exit\n"""))
        #Checking if the user chooses 1
        if UserDecision == 1:
            #Getting the amount the user wants to save
            UserAmountToSave = float(input("How much are you saving per month or week?: "))
            #Asking if the user is saving weekly or monthly
            UserWeeklyOrMonthly = str(input("Are you saving weekly or monthly?: "))
            #Getting the total savings goal from the user
            UserTotalSavingsGoal = float(input("How much money are you trying to save?: "))
            #Clarifying what this will do
            print("This will show you how many weeks or months you need to save for to get that amount of money.")
            #Making a space between these lines
            print("")
            #Showing the user how many weeks or months they need to save for to get their goal.
            print(f"You will need to save for this many weeks or months to get that amount of money: {SaveDeposits(UserAmountToSave, UserWeeklyOrMonthly, UserTotalSavingsGoal)}")
        #Checking if the user chooses 2
        elif UserDecision == 2:
            #Getting the users starting amount of money
            UserMoneyAmount = float(input("How much money are you starting with?: "))
            #Getting the interest rates
            UserInterest = float(input("Please type your interest in the way of like 20 percent (Not using the percent symbol or word): "))
            #Asking if its days, weeks, or months.
            UserTypeOfInterestTime = str(input("Is your interest being compounded for days, weeks, months, or years?: "))
            #How many days, weeks, or months it goes on for.
            UserInterestTime = int(input(f"How many {UserTypeOfInterestTime} is the interest going to last for?: "))
            #Showing the user the interest
            print(f"You will have this much money after this many {UserTypeOfInterestTime}: {CompoundInterest(UserMoneyAmount, UserInterest, UserInterestTime)}")
        #Checking if user chooses 3
        elif UserDecision == 3:
            #Getting the amount of money used for the budgeting
            UserBudgetAmount = float(input("Please give the total amount of money used for budgeting: "))
            #Getting the list used for budgeting
            BudgetAllocatedList = BudgetAllocator(UserBudgetAmount)
            #Giving the user the budget amounts
            print(f"""Here is your budgeting plan Food: {BudgetAllocatedList[0]}
                                                  Entertainment: {BudgetAllocatedList[1]}
                                                  Savings: {BudgetAllocatedList[2]}""")
        #Checking if user chooses 4
        elif UserDecision == 4:
            #Getting the price of the item
            UserCostOfItem = float(input("Please give the original price of the item: "))
            #Getting the discount
            UserDiscount = int(input("Please give me the discount in similar fashion to the interest (Say like 20 percent without the word percent): "))
            #Showing the user the discount they will get
            print(f"This is the item after the discount: {SalesPriceCalculator(UserCostOfItem, UserDiscount)}")
        #Checking if user chooses 5
        elif UserDecision == 5:
            #Getting the total price of the users items
            UserTotalPrice = float(input("Please give me the total price of your items: "))
            #Showing them the tip they will pay
            print(f"This is the tip you will need to pay: {TipCalculator(UserTotalPrice)}")
        #Checking if user chooses 6
        elif UserDecision == 6:
            #Sending a goodbye/exit message
            print("Hope this financial calculator was useful!")
            #Ending the calculator
            break
        #Checking if the user didn't choose numbers 1-6
        elif UserDecision > 6:
            #Making sure the user knows they didn't select an option
            print("You have not selected one of the options please try again.")
            #Bypassing this iteration of the calculator
            continue
