import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Profits_And_Loss.csv"

# read the csv file to append net profit and day from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store day and net profit afterwards
    ProfitsandLoss=[] 

    # append days and net profit into the ProfitsandLoss list
    for row in reader:
        # get the days and net profit of each day
        # and append the ProfitsandLoss list
        ProfitsandLoss.append([row[0],row[4]])   

# print(ProfitsandLoss)

def aCashsurplus(tako):
    """
    -This function will calculate whether the net profit earned is higher than the previous day or not

    -Parameters required are net profit and days
    """
    for dog in range(1, len(tako)):
        # Check if the net profit on the current day is less than or equal to the previous day
        if tako[dog][1] <= tako[dog - 1][1]:  
            return False
    return True

if aCashsurplus(ProfitsandLoss):
    result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"

    def calculate_cash_surplus(data):
        """
        Calculate the cash surplus for each day
        """
        # To store daily cash surplus
        cashSurplus = []  
        highestSurplus = 0
        highestSurplusDay = None
        prevdaydata = None

        for day_data in data:
             # Extract the day from the data
            day = int(day_data[0])    
             # Extract the net profit for the day
            netProfits = int(day_data[1])  

            # Calculate the daily cash surplus based on the difference with the previous day's net profit
            if prevdaydata is not None:
                cash_surplus = netProfits - prevdaydata[1]
                cashSurplus.append((day, cash_surplus))
            prevdaydata = (day, netProfits)

            # Update the highestSurplus and highestSurplusDay if applicable
            if cash_surplus > highestSurplus:
                highestSurplus = cash_surplus
                highestSurplusDay = day

        return cashSurplus, highestSurplusDay, highestSurplus

    # Call the function to calculate cash surplus and find the highest surplus day
    cashsurpluslist, highestSurplusDay, highestSurplus = calculate_cash_surplus(ProfitsandLoss)

    # Generate a formatted string with the details of each day's cash surplus
    result += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
    for cashsurplus in cashsurpluslist:
        day = cashsurplus[0]
        cash = cashsurplus[1]
        # sentence = f"[CASH SURPLUS] Day: {day}, AMOUNT: USD{cash}\n"
        # result += sentence

    result += f"\n[HIGHEST SURPLUS] Day: {highestSurplusDay}, AMOUNT: USD{highestSurplus}\n"
    # print(result)

# If there's no cash surplus, data will go to this function
else:
# Create an empty string to store
    result = ""

def profit_and_loss_function():
    """
    -This function will calculate the profit deficit if net profit on
    the current day is lower than the previous day

    -Parameters required: None
    """
    # Create a list to store data
    profitdeficit = []
    # Set initial previous day's deficit to 0   
    previousdaydeficit = 0   
    result = ""

    for cdeficit in ProfitsandLoss:
        # Extract days from the data
        day = int(cdeficit[0])  
        # Extract the net profit for the day
        cash = int(cdeficit[1])

        # Calculate the daily deficit based on the difference with the previous day's deficit
        pd = previousdaydeficit - cash

        # If there's a profit deficit, add it to the profitdeficit list
        if pd > 0:
            # Ensure pd is abs() to get a positive output
            profitdeficit.append((day, abs(pd)))
            sentence = f"[PROFIT DEFICIT] Day: {day}, AMOUNT: USD{abs(pd)}\n"
            result += sentence
        
        # Update the previousdaydeficit with the current day's deficit for the next iteration
        previousdaydeficit = cash

    return result

# Call the function to get the result
profit_and_loss_result = profit_and_loss_function()

# print(profit_and_loss_result)
