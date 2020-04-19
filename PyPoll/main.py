
import csv 
import os 

polls_csv = os.path.join("election_data.csv")

total_votes = 0 
num_votes = {}

with open (polls_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader: 
        total_votes += 1
        
        if row["Candidate"] not in num_votes: 
            num_votes[row["Candidate"]] = [1]
            
        else: 
            key = row["Candidate"]
            num_value = num_votes[key] 
            num_votes[key][0] += 1

winner = max(num_votes, key=num_votes.get)

for candidate in num_votes:
    total_cand = num_votes[candidate][0]
    percent = str(round(total_cand/total_votes*100,3)) + "%"
    num_votes[candidate].append(percent)

winner = max(num_votes, key=num_votes.get)

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for key in num_votes:
    print(f"{key}: {num_votes[key][1]} ({num_votes[key][0]})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#Exporting ot .txt file 
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for key in num_votes:
    line = (f"{key}: {num_votes[key][1]} ({num_votes[key][0]})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
