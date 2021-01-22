# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Initial define of variables that will be pulled from CSV
total_months = 0
net_profit = 0
month = 0
profit_loss = 0

# Define lists that will hold the months and the profit/loss changes
# This is a place to store the values as the for loop goes through the csv
month_count = []
month_profit_change = []

# Define variables needed for future calculations
average_change = 0
pl_change = 0
prev_row = 0
greatest_increase = 0
greatest_decrease = 0

# Open the CSV and make sure that it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print csvreader to make sure everything is set up correctly
    #print(csvreader)

    # Recognize the header row, and know to skip when working with the rest of the rows
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Set for loop to read through each row of the csvreader
    for row in csvreader:
        
        # Define what information is held in each column of each row
        month = (row[0])
        profit_loss = int(row[1])
        

        # Add month value to the month_count list
        # Get total months by getting the length of the month_count list
        month_count.append(month)
        total_months = len(month_count)
        
        # Find the net profit by adding the profit_loss value of column 1 to the net profit running total
        net_profit = net_profit + profit_loss
        #print(net_profit)


        # Calculate the monthly change in profit_loss using if statement
        # This if statement fixes the issue of not getting a zero for the first value
        if pl_change != 0:
            pl_change = profit_loss - prev_row
            month_profit_change.append(pl_change)
        else:
            month_profit_change.append(pl_change)
            pl_change = profit_loss - prev_row
        #print(month_profit_change) - life saving print statement!
    
        # This will store the value in the profit/loss column so that the next time we cycle through it can be used for the pl_change calculation
        # This happens after the if statement so that it effects the next loop but not the current one
        prev_row = int(row[1])

        
        # Calculate the greatest change in increase to the profit_loss column
        if pl_change > greatest_increase:
            greatest_increase = pl_change
            # Grab the associated month when the greatest increase is found
            greatest_increase_month = row[0]
            
        # Same strategy as above, calculate the greatest change in decrease to the profit_loss column
        if pl_change < greatest_decrease:
            greatest_decrease = pl_change
            greatest_decrease_month = row[0]
        

    # Get the average by dividing the monthly change numbers by the total months count
    # The len(month_profit_change) needs a -1 because there is no value change for the first month, meaning there is one less month in the average calculation
    average_change = sum(month_profit_change) / (len(month_profit_change) - 1)
    # Round to two decimal places to match the assignments output
    average_change = str(round(average_change, 2))
    #print(sum(month_profit_change))
    #print((len(month_profit_change))) - This print statement saved me


#-------------------------------------------------#
# Print Statements
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#-------------------------------------------------#
# Export text file of results to Analysis folder

# Specify the file to write to
txt_output = os.path.join("Analysis", "PyBank_Results.txt")

# Open the file using the "w" to write to a file
with open(txt_output, 'w',) as PyBank_Results:

    # Write the same information to the file that was printed in the terminal
    # Added the '\n' because it is a line break function in python when writing to a fiel, this makes the txt output resemble the terminal print
    PyBank_Results.write(f"Financial Analysis\n")
    PyBank_Results.write(f"----------------------------\n")
    PyBank_Results.write(f"Total Months: {total_months}\n")
    PyBank_Results.write(f"Total: ${net_profit}\n")
    PyBank_Results.write(f"Average Change: ${average_change}\n")
    PyBank_Results.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    PyBank_Results.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

