# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies

import csv
import os

# Assign a variable for the file to load and the path

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

#Candidate options
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning ocunt tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:


    # To do: Read and analysze the data here.
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

        #Print the candidates name from each row
        candidate_name = row[2]

        # If the candidate name doesn't match existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidates votes
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
    #Iterate through the candidtae list
    for candidate_name in candidate_votes:
        #Retrieve the bote count of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do : print out each candidates name, vote count, and percentage of votes to the terminal

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
    winning_candidate_summary = (
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:/.1f}%\n"
        )

    print(winning_candidate_summary)

    

