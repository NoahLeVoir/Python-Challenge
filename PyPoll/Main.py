# Import modules
import os
import csv

# Set path for the csv file in the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Dim the variables for total votes and for each candidate
total_votes = 0

# Define place to store votes for each candidate
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

    # First get the total number of votes cast by counting each unique voter ID
    # This is the value stored in the first row, add each entry to the voter count list
    for row in csvreader:
        vote = int(row[0])
        vote_counter.append(vote)
        # The length of the list we just created will give us the number for the total votes cast
        total_votes = len(vote_counter)

        # Now we can use if statements to count votes for each candidate
        # First however we need to identify the candidate column
        candidate = row[2]
        if candidate == "Khan":
            khan_votes.append(candidate)
        elif candidate == "Correy":
            correy_votes.append(candidate)
        elif candidate == "Li":
            li_votes.append(candidate)
        else:
            otooley_votes.append(candidate)

    # Same as with total_votes, the length function of each list will reveal the number of votes each candidate recieved
    khan_total = len(khan_votes)
    correy_total = len(correy_votes)
    li_total = len(li_votes)
    otooley_total = len(otooley_votes)

    # To get the percent value we will divide the candidate total from the total votes
    khan_pct = khan_total / total_votes
    # This format function displays the result as a percentage with 3 decimal points, like it shows in the homework example
    khan_pct = "{:.3%}".format(khan_pct)
    #print(khan_pct)
    # Run the same calculation as above for the rest of the candidates
    # And format each to a percentage with 3 decimal points
    correy_pct = correy_total / total_votes
    correy_pct ="{:.3%}".format(correy_pct)
    li_pct = li_total / total_votes
    li_pct ="{:.3%}".format(li_pct)
    otooley_pct = otooley_total / total_votes
    otooley_pct ="{:.3%}".format(otooley_pct)

    # Use the max function to the greatest number of votes a candidate recieved
    # The answer is the winner of the election
    winner = max(khan_total, correy_total, li_total, otooley_total)
    #print(winner) - This displays the max vote total as a number

    # To get the associated winners name, I can use if logic to match the winner value with a name
    # Will use a new variable called 'winners_name' to store this
    if winner == khan_total:
        winner_name = "Khan"
    elif winner == correy_total:
        winner_name = "Correy"
    elif winner == li_total:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"
    #print(winner_name)

#-------------------------------------------------#
# Print Statements
# The text print statements and formatting are taken directly from the homework instructions, the values are dependant upon the code running successfully
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_pct} ({khan_total})")
print(f"Correy: {correy_pct} ({correy_total})")
print(f"Li: {li_pct} ({li_total})")
print(f"O'Tooley: {otooley_pct} ({otooley_total})")
print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

#-------------------------------------------------#
# Export text file of results to Analysis folder