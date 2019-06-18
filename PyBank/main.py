#PyBank
#Goal: ouput metrics via print screen and export to text file 

#Reading CSV file: raw data
import os
import csv

# Variables for storing data from csv file and running loops  
Dates = []
i = 0
Profit_Losses = []
Profit_Losses_Changes = []
j = 1

csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)

    # month count & net profit/loss calculation
    for row in csvreader:
        Dates.append(row[0])
        i = i + 1
        Profit_Losses.append(int(row[1]))
        total = sum(Profit_Losses,0)
    
    # monthly changes (first element of Monthly Change array is zero since it cannot be calculated for the first month of the list)
    Profit_Losses_Changes.append(int(0))
    for j in range(1,i):
        change = Profit_Losses[j] - Profit_Losses[j-1]
        Profit_Losses_Changes.append(int(change))
        j = j + 1
    
    # Monthly changes average
    Total_Changes = sum(Profit_Losses_Changes,0)
    Changes_Count = len(Profit_Losses_Changes)
    Monthly_Ave =round(Total_Changes / Changes_Count,2) 

    #Largest Increase & Decrease Monthly Changes 
    Max_Monthly_Change = int(max(Profit_Losses_Changes))
    Min_Monthly_Change = int(min(Profit_Losses_Changes))
    Monthly_Changes_Combo = dict (zip(Profit_Losses_Changes,Dates))
    
    #Print Report
    print("Financial Analysis")
    print("----------------------------------------------------")
    print(f'Total Months: {i}')
    print(f'Net Profit/Loss: ${total}')
    print(f'Average Monthly Change: ${Monthly_Ave}')
    print(f'Greatest Increase in Profits: {Monthly_Changes_Combo[int(Max_Monthly_Change)]} (${Max_Monthly_Change})')
    print(f'Greatest Decrease in Profits: {Monthly_Changes_Combo[int(Min_Monthly_Change)]} (${Min_Monthly_Change})')
    print(f'----------------------------------------------------')

    



   





    
    


    



  

        



    















