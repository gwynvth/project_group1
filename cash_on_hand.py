<<<<<<< HEAD
from pathlib import Path
import csv_reports

# create a file to csv file.
fp = Path.cwd()/"Cash_On_Hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv_reports.reader(file)
    next(reader) # skip header

    # create an empty lists to store day and cash on hand records
    cashonhand=[] 

    # append cash on hand record into the cashonhand list
    for row in reader:
        #get the day and cash on hand for each day
        cashonhand.append([row[0],row[1]])  
print(cashonhand) 
=======


ufdthfyf 

for jf in di:


>>>>>>> 20582b2 (first)











