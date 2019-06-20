#PyPoll
#Goal: print voting metrics and export to text file

import os
import csv
from datetime import date

# Variables and arrays
i = 0
Candidates = []
Candidates_List = []
w = 0
z = 0
l = 0
o = 0

#Reading CSV file / Raw Data
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)
    
    #Total Votes calculation & extracting candidate names
    for row in csvreader:
        Candidates.append(row[2])
        Candidates_List.append(row[2])
        i = i + 1
    
    #List of unique candidates 
    Candidates_List =list(dict.fromkeys(Candidates))

    #Khan's total votes & win percentage
    for n in range(int(len(Candidates))):
        if Candidates[n-1] == Candidates_List[0]:
            w = w +1
    Khan_win_perc = round(float((w/len(Candidates)) * 100),3)

    #Correy's total votes & win percentage
    for n in range(int(len(Candidates))):
        if Candidates[n-1] == Candidates_List[1]:
            z = z + 1
    Correy_win_perc = round(float((z/len(Candidates)) * 100),3)

    #Li's total votes & win percentage
    for n in range(int(len(Candidates))):
        if Candidates[n-1] == Candidates_List[2]:
            l = l + 1
    Li_win_perc = round(float((l/len(Candidates)) * 100),3)
    

    #O'Tooley's total votes & win percentage
    for n in range(int(len(Candidates))):
        if Candidates[n-1] == Candidates_List[3]:
            o = o + 1
    OTooley_win_perc = round(float((o/len(Candidates)) * 100),3)

    #Winner 
    Perc_List = [Khan_win_perc,Correy_win_perc,Li_win_perc,OTooley_win_perc]
    Per_Name_Combo = dict (zip(Perc_List,Candidates_List))
    Winner = float (max(Perc_List))

    #Print Report 
    print(f'Electronic Results')
    print(f'---------------------------------------------------')
    print(f'Total Votes: {int(i)}')
    print(f'---------------------------------------------------')
    print(f'{Candidates_List[0]}: {Khan_win_perc}% ({w})')
    print(f'{Candidates_List[1]}: {Correy_win_perc}% ({z})')
    print(f'{Candidates_List[2]}: {Li_win_perc}% ({l})')
    print(f'{Candidates_List[3]}: {OTooley_win_perc}% ({o})')
    print(f'...................................................')
    print(f'Winner: {Per_Name_Combo[Winner]}')
    print(f'---------------------------------------------------')

    #Export Metrics to Text File
    Report_Date = date.today()
    Metrics_Date = Report_Date.strftime("%m_%d_%Y")
    
    with open ("Metrics_" + Metrics_Date + ".txt", "w") as Metrics_File:
        Metrics_File.write("Electronic Results\n")
        Metrics_File.write("-----------------------------------\n")
        Metrics_File.write(f'Total Votes: {int(i)}\n')
        Metrics_File.write(f'------------------------------------\n')
        Metrics_File.write(f'{Candidates_List[0]}: {Khan_win_perc}% ({w})\n')
        Metrics_File.write(f'{Candidates_List[1]}: {Correy_win_perc}% ({z})\n')
        Metrics_File.write(f'{Candidates_List[2]}: {Li_win_perc}% ({l})\n')
        Metrics_File.write(f'{Candidates_List[3]}: {OTooley_win_perc}% ({o})\n')
        Metrics_File.write(f'...................................................\n')
        Metrics_File.write(f'Winner: {Per_Name_Combo[Winner]}\n')
        Metrics_File.write(f'---------------------------------------------------\n')
            
        
        
        

        


   
        



   

