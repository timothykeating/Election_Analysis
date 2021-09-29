# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
######################################################

# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
######################################################
#Add our dependencies (Modules that we're using)
import csv
import os

# Open the data file that we'll be reading from
elec_data='Resources_Election_Analysis/election_results.csv'
# create a new file to write to
elec_outcome='Resources_Election_Analysis\election_outcome.txt'

# initialize the total_voter_counter variable BEFORE opening the file - of type=integer
# & initialize the candidates list variable - list
# && initialize the candidates votes variable - dictionary
total_votes=0
cand_list=[]
cand_votes={}

#open the file that we're READING first
with open(elec_data) as election_data:
    
    ###read and analyze the data here

    #1. read the file with the reader function in the csv module
    file_reader=csv.reader(election_data)
    #1z. print the entire file as a test that its reading it correctly
    # for row in file_reader:
    #     print(row)
    
    #2. read the header row
    headers=next(file_reader)
    
    #3. loop through the csv file to find the total_votes
    for row in file_reader:
        total_votes+=1
#3z. print the vote total to check
# print(f'the total number of votes is: {total_votes}')

        #4. (continue to) loop through the csv file to find all candidate names
        cand_name=row[2]
        #4aa. use an if statement to determine uniqueness
        if cand_name not in cand_list:
            #4a. add the candidate name to the list
            cand_list.append(cand_name)
#4z. print the candidate list to check
# print(cand_list)

            #5. (continue to) loop through the csv file & stay in the IF statement...
            #  begin to tally vote count
            cand_votes[cand_name]=0
        #5a. add votes to the vote count for each candidate BUT move out of the if statement...
        # because the if statement was setting the list of all candidates, and setting each one of their counters to zero
        # now we want to have it do a plus+1 every time we see the candidate name, which is not logically part of the if statement
        cand_votes[cand_name]+=1
#5z. print the candidate vote dictionary to check
# print(cand_votes)

#6. determine percentage of total votes each candidate got
# we're over here, flush with the left margin, because we're done with the for-loop
# AND we're done reading the csv file, completely
###
# loop through the dictionary, and declare votes and vote_pct with formulae
for cand_name in cand_votes:
    votes=cand_votes[cand_name]
    vote_pct=float(votes)/float(total_votes)*100
    print(f'{cand_name}: received {vote_pct:.2f}% of the vote.')














































































