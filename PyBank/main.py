#Import the dependences
import os
import csv

#Read in a .csv file
csv_file = os.path.join("02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

month = []
revenue =[]
revenue_change = []
monthly_change = []
prev_value=''

with open(csv_file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    header = next(csv_reader)

    #Months
    for row in csv_reader:
        month.append(row[0])
        revenue.append(int(row[1]))


    for i in range(len(revenue)-1):

        monthly_change.append(revenue[i+1]-revenue[i])

    max_increase_value = max(monthly_change)
    max_decrease_value = min(monthly_change)

    max_increase_month = monthly_change.index(max(monthly_change)) + 1
    max_decrease_month = monthly_change.index(min(monthly_change)) + 1
    
print("PythonHomeworkCode")
print("----------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: ${sum(revenue)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {month[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {month[max_decrease_month]} (${(str(max_decrease_value))})")

