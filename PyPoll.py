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

#open the file that we're READING first
with open(elec_data) as election_results:
    
    #read and analyze the data here
    #1. read the file with the reader function in the csv module
    file_reader=csv.reader(election_results)
    #1a. print the entire file as a test that its reading it correctly
    # for row in file_reader:
    #     print(row)
    
    #2. print the header row only
    headers=next(file_reader)
    print(headers)





































































