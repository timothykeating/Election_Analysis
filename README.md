# Election_Analysis
Python Module 3

# PyPoll.py File
The PyPoll.py file was created as I progressed through Module 3.  In order to analyze the data and write the results of the election analysis to a text file, I took many steps, and here they are laid out in order:  
- Add dependent modules csv and os;
- Name the files that we'll be reading from and writing to;
- Initialize all variables to be used later;
- Open the file that we're reading from;
- Read the file with csv.reader;
- Skip the header row data;
- Loop through the file to:
	- Find the total number of votes,
	- Find a list of all candidates,
	- Find the number of votes for each candidate
- Open the file that we're writing to;
- Write on the file:
	- Header,
	- Total votes,
	- Votes per candidate,
	- Percentage votes per candidate
- Establish and declare a winner;
- Create a summary of the winner & write that information to the file.
