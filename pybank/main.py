# First we'll import the os module
# This will allow us to create file paths across operating systems

from operator import indexOf
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#set variables
sales = []
Date = []
months = []
pnl_delta = 0
monthly_pnl_delta = []


with open(csvpath) as file:  

    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    #print(header)

    for row in csvreader:
        Date.append(row[0])
        sales.append(int(row[1]))


#get # of months
Total_months = len(Date)

#get total profit
Total_PNL = sum(sales)

#create list w/ monthly changes
for i in range(len(sales)-1):
    pnl_delta = sales[i + 1] - sales[i]
    monthly_pnl_delta.append(pnl_delta)

#get avg, inc & dec from monthly delta
Average_Change = round(sum(monthly_pnl_delta)/(Total_months-1), 2)
greatest_increase_in_profits = max(monthly_pnl_delta)
greatest_decrease_in_profits = min(monthly_pnl_delta)

#get months for greatest inc & dec
test = monthly_pnl_delta.index(max(monthly_pnl_delta))
increase_date = Date[test + 1]

test1 = monthly_pnl_delta.index(min(monthly_pnl_delta))
decrease_date = Date[test1 + 1]

#print final results
print('Financial Analysis')
print('----------------------------')
print(f"Total Months: {Total_months}")
print(f"Total PnL: {Total_PNL}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_in_profits})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_in_profits})")

#export to text file
outpath = os.path.join('analysis', 'pybank_output.txt')
with open(outpath, "w") as text:
        text.write('Financial Analysis\n')
        text.write('----------------------------\n')
        text.write(f"Total Months: {Total_months}\n")
        text.write(f"Total PnL: {Total_PNL}\n")
        text.write(f"Average Change: ${Average_Change}\n")
        text.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase_in_profits})\n")
        text.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_in_profits})\n")


