#Max Holdaway Financial Calculator

#Function for the saving money part of the financial calculator
def SaveDeposits(AmountToSave, WeeklyOrMonthly, TotalSavingsGoal):
    #Seeing if the user chose Weekly or Monthly saving
    if WeeklyOrMonthly == "Weekly":
        #How many weeks they need to save for to get their goal
        WeeksToSave = 0
        #A number used to determine how many weeks are needed to save
        WeeklySavings = AmountToSave
        #The loop used to find out how many weeks they need to save for
        while WeeklySavings != TotalSavingsGoal:
            #Adding one to WeeksToSave
            WeeksToSave += 1
            WeeklySavings += AmountToSave
        return WeeksToSave
    elif WeeklyOrMonthly == "Monthly":
        MonthsToSave = 0
        MonthlySavings = AmountToSave
        while MonthlySavings != TotalSavingsGoal:
            MonthsToSave += 1
            MonthlySavings += AmountToSave
        return MonthsToSave
    else:
        print("You did not choose Weekly or Monthly ")

def CompoundInterest(MoneyAmount, Interest, InterestTime):
    for x in InterestTime:
        MoneyAmount += (MoneyAmount * Interest)

