import csv
from pathlib import Path

# create a file to csv file. 
fp = Path.cwd()/"csv_reports"/"Profits_And_Loss.csv"

# read the csv file to append net profit and day from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store day and net profit afterwars
    ProfitsandLoss=[] 

    # append days and net profit into the ProfitsandLoss list
    for row in reader:
        #get the days and net profit of each day
        #and append the ProfitsandLoss list
        ProfitsandLoss.append([row[0],row[4]])   

# print(ProfitsandLoss)

def aCashsurplus(tako):
    """
    -This function will calculate whether the net profit earned is higher than the previous day or not
    -Parameters required are net profit and days
    """
    for dog in range(1, len(tako)):
        if tako[dog][1] <= tako[dog - 1][1]:  # Check if the net profit on the current day is less than or equal to the previous day
            return False
    return True

if aCashsurplus(ProfitsandLoss):
    result = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"

    def calculate_cash_surplus(data):
        """
        Calculate the cash surplus for each day
        """
        cashSurplus = []   # A list to store daily cash surplus
        highestSurplus = 0
        highestSurplusDay = None
        prevdaydata = None

        for day_data in data:
            day = int(day_data[0])     # Extract the day from the data
            netProfits = int(day_data[1])  # Extract the net profit for the day

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
        sentence = f"[CASH SURPLUS] Day: {day}, AMOUNT: USD{cash}\n"
        result += sentence

    result += f"\n[HIGHEST SURPLUS] Day: {highestSurplusDay}, AMOUNT: USD{highestSurplus}\n"
    # print(result)

# Initialize an empty string to store the final result
else:

    result = ""

# Define a function to calculate the profit deficit 
def calculate_cash_deficit(data):
    """
    -This function will calculate the profit deficit if net profit on
    the current day is lower than the previous day
    -Required parameters are days and net profit
    """
    profitdeficit = []       # A list to store data
    previousdaydeficit = 0   # Set initial previous day's deficit to 0

    for cdeficit in data:
        day = int(cdeficit[0])  # Extract the days from the data
        cash = int(cdeficit[1]) # Extract the net profit for the day

        # Calculate the daily deficit based on the difference with the previous day's deficit
        # daily_deficit = previousdaydeficit - cash

        if previousdaydeficit >= 0:
            pd = previousdaydeficit - cash
            # If there's a profit deficit, add it to the profitdeficit list
            if pd > 0:
                profitdeficit.append((day, cash - previousdaydeficit))

        # Update the previousdaydeficit with the current day's deficit for the next iteration
        previousdaydeficit = cash

    return profitdeficit

# Call the function to calculate profit deficit and get the result
profitdeficitlist = calculate_cash_deficit(ProfitsandLoss)

# Generate a formatted string with the details of each day's profit deficit
for profitd in profitdeficitlist:
    day = profitd[0]
    cash = profitd[1]
    sentence = f"[PROFIT DEFICIT] Day: {day}, AMOUNT: USD{cash}\n"
    result += sentence
 
print(profitdeficitlist)