import csv 
import os 
import statistics

polls_csv = os.path.join("budget_data.csv")

num_months = 0 
net_total = 0 
max_profit = 0 
min_profit = 0 
max_profit_month = ""
min_profit_month = ""
profit = []
netchange = 0
netchange_log = []

with open (polls_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for row in csvreader: 
        num_months += 1
        net_total = net_total + int(row[1])
        profit.append(int(row[1]))
        
        if num_months > 1:
            netchange = profit[-1]-profit[-2]
            netchange_log.append(netchange)

            if netchange > max_profit: 
                max_profit = netchange
                max_profit_month = row[0]
            
            elif netchange < min_profit:
                min_profit = netchange
                min_profit_month = row[0]
        


avg_change = "$" + str(round(statistics.mean(netchange_log),2))


# Displaying results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {str(num_months)}")
print(f"Total: ${net_total}")
print((f"Average Change: {avg_change}"))
print(f"Greater Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

#Exporting ot .txt file 
output = open("output_financial.txt", "w")
line1 = "Financial Analysis"
line2 = "--------------------------"
line3 = f"Total Months: {str(num_months)}"
line4 = f"Total: ${net_total}"
line5 = f"Average Change: {avg_change}"
line6 = f"Greater Increase in Profits: {max_profit_month} (${max_profit})"
line7 = f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})"
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))