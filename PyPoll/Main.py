# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Dim the variables for total votes and for each candidate
total_votes = 0

# Store votes for each candidate
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

# List to store the total vote counts
vote_counter = []

# Open the CSV and make sure that it is being read
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print csvreader to make sure everything is set up correctly
    #print(csvreader)

    # Recognize the header row, and know to skip when working with the rest of the rows
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # First we will get the total number of votes cast by counting all of the ID row and putting them into a list
    for row in csvreader:
        vote = int(row[0])
        vote_counter.append(vote)
        # The length of the list we just created will give us the number for the total votes cast
        total_votes = len(vote_counter)






#-------------------------------------------------#
# Print Statements (Test)
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

