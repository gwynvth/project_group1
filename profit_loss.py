import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Profits_And_Loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store time sheet and sales record
    ProfitsandLoss=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, toal hours, break hours, and sales for each record
        #and append the salesRecords list
        ProfitsandLoss.append([row[0],row[4]])   

# print(ProfitsandLoss)

def aCashsurplus(tako):
    """
    -This function will calculate whether the net profit earned is higher than the previous day or not
    -Parameters required are net profit and days 
    """
    for dog in range(1, len(tako)):
        if tako[dog] <= tako[dog - 1]:
            return False
    return True

if aCashsurplus(ProfitsandLoss):
    result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"

    def calculate_cash_surplus(data):
        """
        """
        highestSurplus = 0
        highestSurplusDay = None 
        prevdaydata = None

        for yay in data:
            day = range(len(yay[0]))
            netProfits = int(yay[1])

            cashSurplus = []
            totalCashsurplus = 0

else:
    result = ""

    def calculate_cash_deficit(data):
        profitdeficit = []
        previousdaydeficit = 0

        for cdeficit in data:
            day = int(cdeficit[0])
            cash = int(cdeficit[1])

            if previousdaydeficit > cash:
                daily_deficit = previousdaydeficit - cash
            elif daily_deficit > 0:
                profitdeficit.append((day, daily_deficit))

            previousdaydeficit = cash

        return profitdeficit
    
    


                
