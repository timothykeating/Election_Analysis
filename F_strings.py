my_votes = int(input('How many votes did you get?'))
total_votes=int(input('How many total votes were there?'))

# percentage_votes=(my_votes/total_votes)*100
# print('I received '+str(percentage_votes)+'% of the total votes')

# print(f'I received {my_votes/total_votes*100:.2f}%of the total votes')

# message_to_candidate=(
#     f'You received {my_votes} votes.\n'
#     f'The total number of votes was {total_votes:,}\n'
#     f'You received {my_votes/total_votes*100:.2f}% of the total votes.\n')
# print(message_to_candidate)

print(f'{my_votes/total_votes*100:.2f}')