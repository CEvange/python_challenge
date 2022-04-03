import os
import csv

pypoll_csv = os.path.join('Resources','election_data.csv')

with open (pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvfile)

    total_votes = 0
    candidate_total = {}
    
 # The total number of votes cast

    for row in csvreader:
        cdd = str(row[2])

        total_votes = total_votes + 1

# To get the candidates and total votes per candidate
        if cdd in candidate_total.keys():
            candidate_total[cdd] = candidate_total [cdd] + 1
        else: 
            candidate_total[cdd] = 1

# Creates lists of candidates, total votes for each candidate and percentage of votes 

cdd_list = []
cdd_vote = []

for name,vote_count in candidate_total.items():
    cdd_list.append (name)
    cdd_vote.append (vote_count)

percentage = []
for number in cdd_vote:
    percentage.append(round(number/total_votes*100,3))


summary_table = list(zip(cdd_list, percentage, cdd_vote))


# The winner of the election based on popular vote.
winner = max(cdd_vote)
win_cdd = cdd_vote.index(max(cdd_vote))
winning_candidate = (cdd_list[win_cdd])
        

print ('Election Results')
print('------------------------------------------')
print (f'Total Votes: {total_votes}')
print('------------------------------------------')
for cddname in summary_table:
    print (cddname)
print('------------------------------------------')
print(f'Winner: {winning_candidate}')
print('------------------------------------------')

filepath = os.path.join('Analytics','pypoll_output.txt')
with open(filepath,'w') as file:
    file.write ('Election Results')
    file.write ("\n")
    file.write ('------------------------------------------')
    file.write ("\n")
    file.write (f'Total Votes: {total_votes}')
    file.write ("\n")
    file.write ('------------------------------------------')
    file.write ("\n")
    file.write (f'{summary_table}')
    file.write ("\n")
    file.write ('------------------------------------------')
    file.write ("\n")
    file.write (f'Winner: {winning_candidate}')
    file.write ("\n")
    file.write ('------------------------------------------')