#main.py in PyPoll

import os
import csv

# set the path
csvpath = os.path.join( 'election_data.csv')

# initialize the variables
total_votes = 0
candidate_option = []
candidate_vote = {}
winning_count = 0

# open the election_data.csv
with open(csvpath, newline="") as csvfile:
   # read the rows
   csvreader=csv.reader(csvfile,delimiter=",")
  #Skips the header row
   csv_header = next(csvreader)
   # loop through the rows and add them to the dictionary if not already there.
   for row in csvreader:
    total_votes = total_votes + 1 
    candidate_name = row[2]
    if candidate_name not in candidate_option:
        candidate_option.append(candidate_name)
        candidate_vote[candidate_name]=0
    candidate_vote[candidate_name]= candidate_vote[candidate_name]+1
    #winning vote count for candidate
    for candidate in candidate_vote:
       votes = candidate_vote.get(candidate)
       vote_percentage = float(votes) / float (total_votes)  * 100

      # find winning vote count and candidate
       if votes > winning_count: 
            winning_count = votes
            winning_candidate = candidate


print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
print(f"{winning_candidate}")


# Print the results and export the data to our text file
output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, "w") as txt_file:
   # Print the final vote count (to terminal)
   election_results = (
       f"\n\nElection Results\n"
       f"******************\n"
       f"Total Votes: {total_votes}\n"
       f"*************\n")
   print(election_results, end="")
   # Save the final vote count to the text file
   txt_file.write(election_results)
   # Determine the winner by looping through the counts
   for candidate in candidate_vote:
       # Retrieve vote count and percentage
       votes = candidate_vote.get(candidate)
       vote_percentage = float(votes) / float(total_votes) * 100
       # Determine winning vote count and candidate
       if (votes > winning_count):
           winning_count = votes
           winning_candidate = candidate
       # Print each candidate's voter count and percentage (to terminal)
       voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
       print(voter_output, end="")
       # Save each candidate's voter count and percentage to text file
       txt_file.write(voter_output)
   # Print the winning candidate (to terminal)
   winning_candidate_summary = (
       f"********************\n"
       f"Winner: {winning_candidate}\n"
       f"********************\n")
   print(winning_candidate_summary)
   # Save the winning candidate's name to the text file
   txt_file.write(winning_candidate_summary)




      #print(row) using this to make sure code works.
      #If Khan  not in dictionary add them to it, if so add to count.

      #If Correy not in dictionary add them to it, if so add to count.

      #If Li not in dictionary add them to it, if so add to count.

      #If O'Tooley not in dictionary add them to it, if so add to count.

      #Get total votes for votes cast

      #complete list of candidates who received votes

      #The percentage of votes each candidate won

#look up how  see if someone is in a dictionary and then add them if not in the dictionary.