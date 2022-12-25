import os
import csv

budget_data = os.path.join("..", "Pybank", "Resources", "budget_data.csv")

with open(budget_data, encoding = "utf-8-sig") as csv_file:
    budgetdata_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_file)
  
    num_months = 0
    net_profit = 0
    date_list = []
    profitloss_list = []
    monthly_change_list = []

    #Calculating Total Months and Net Profit as well as creating separate lists for dates and profits/losses
    for row in budgetdata_reader:
        num_months += 1
        net_profit = net_profit + int(row[1])
        date_list.append(row[0])
        profitloss_list.append(int(row[1]))

    #Calculating Average Change    
    length_profitloss_list = len(profitloss_list)
    index_num = int(1)
    for num in profitloss_list:
        if length_profitloss_list > index_num:
            monthly_change_list.append(profitloss_list[index_num] - num)
            index_num += 1
    avg_change = round(sum(monthly_change_list)/len(monthly_change_list), 2)
        
    #Greatest Increase/Decrease in Profits with Date and Amount
    greatest_increase = max(monthly_change_list)
    greatest_decrease = min(monthly_change_list)
    greatestincrease_dateindex = monthly_change_list.index(greatest_increase) + 1
    greatestdecrease_dateindex = monthly_change_list.index(greatest_decrease) + 1
    date_highestincrease = date_list[greatestincrease_dateindex]
    date_highestdecrease = date_list[greatestdecrease_dateindex]

    #Printing Financial Analysis
    print("Financial Analysis \n"
        "---------------------------- \n"
        f"Total Months: {num_months} \n"
        f"Total: ${net_profit} \n"
        f"Average Change: ${avg_change} \n"
        f"Greatest Increase in Profits: {date_highestincrease} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {date_highestdecrease} (${greatest_decrease})")
        
    #Creating Financial Analysis Text
    pybank_analysis = os.path.join("..", "Pybank", "PyBank Analysis", "PyBank_Analysis.txt")
    with open(pybank_analysis, mode = "w") as txt_file:
        txt_file.write(("Financial Analysis \n"
            "---------------------------- \n"
            f"Total Months: {num_months} \n"
            f"Total: ${net_profit} \n"
            f"Average Change: ${avg_change} \n"
            f"Greatest Increase in Profits: {date_highestincrease} (${greatest_increase})\n"
            f"Greatest Decrease in Profits: {date_highestdecrease} (${greatest_decrease})"))
