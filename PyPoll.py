
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
# &&& winning variables - candidate, votes, vote_pct
total_votes=0
cand_list=[]
cand_votes={}
win_cand=''
win_votes=0
win_pct=0
print('-------------------')
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
    # 6z. print to check 
    
    print(f'{cand_name}: received {vote_pct:.2f}% of the vote.')
    ###
    #6a. still in the for-loop, check each variable votes vs the winning vote count variable
    # & replace/update all the winning variables if the amount is greater than
    if votes>win_votes:
        win_cand=cand_name
        win_votes=votes
        win_pct=vote_pct
#7z.  print check
# print(win_cand)
# print(win_votes)
# print(f'{win_pct:.2f}%')
#7.  print winning candidate with f string & all winning variables
win_summary=(
    f'-------------------\n'
    f'Winner: {win_cand}\n'
    f'Winning Vote Count: {win_votes:,}\n'
    f'Winning Percentage: {win_pct:.2f}%\n'
    f'-------------------'
)
print(win_summary)












































































