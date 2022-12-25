import os
import csv

election_data = os.path.join("..", "Pypoll", "Resources", "election_data.csv")

with open(election_data, encoding = "utf-8-sig") as csv_file:
    election_datareader = csv.reader(csv_file, delimiter = ",")

    header = next(csv_file)

    total_votes = 0
    candidates_dict = {}

    pypoll_analysis = os.path.join("..", "PyPoll", "PyPoll Analysis", "PyPoll_Analysis.txt")
    with open(pypoll_analysis, mode = "w") as txt_file:

        #Calculating Total Votes and Creating Dictionary(Politician Name : Number of Votes Received)
        for row in election_datareader:
            if row[2] not in candidates_dict.keys():
                candidates_dict.update({row[2] : 1})
            else:
                candidates_dict[row[2]] += 1

            total_votes += 1

        #Printing Total Election Votes
        print(f"Election Results \n"
            "------------------------- \n"
            f"Total Votes: {total_votes}\n"
            "-------------------------")
        txt_file.write((f"Election Results \n"
            "------------------------- \n"
            f"Total Votes: {total_votes}\n"
            "------------------------- \n"))
        
        #Printing All Candidates, Percentage of Votes, and Number of Votes as well as Finding Election Winner
        highest_vote = max(candidates_dict.values())
        winner_name = str()
        for politician_name in candidates_dict:
            percentage_votes = round((candidates_dict[politician_name]/total_votes*100), 3)
            print(f"{politician_name}: {percentage_votes}% ({candidates_dict[politician_name]})")
            txt_file.write(f"{politician_name}: {percentage_votes}% ({candidates_dict[politician_name]}) \n")
            if highest_vote == candidates_dict[politician_name]:
                winner_name = politician_name
        
        #Printing Election Winner
        print("------------------------- \n"
        f"Winner {winner_name} \n"
        "-------------------------")

        txt_file.write("------------------------- \n"
        f"Winner {winner_name} \n"
        "-------------------------")
        

