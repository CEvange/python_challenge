import os
import csv


pybank_csv = os.path.join('Resources','budget_data.csv')

with open (pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
   
    header = next(csvfile)

    total_months = []
    total_prof_loss = []
    average_change = []

    for row in csvreader:
        timeline = str(row[0])
        prof_loss = int(row[1])
    
    # total number of months in dataset
    # net total amount of Profit/Losses over the entire period
        if timeline != " ":
            months = (timeline)
            total_months.append(months)
  
        if prof_loss != " ":
            proloss = (prof_loss)
            total_prof_loss.append(proloss)

    monthly_total = len(total_months)
        
    proloss_total = sum(total_prof_loss)

     # average of the changes in Profit/Losses
    for item in range(len(total_prof_loss) - 1):
        average_change.append(total_prof_loss[item + 1]- total_prof_loss[item])
       
    average_change_total= (sum(average_change))/len(average_change)

# greatest increase in profits (date and amount)       
great_inc = max(average_change)
m_inc = average_change.index(max(average_change)) + 1

# greatest decrease in losses (date and amount)
great_dec = min(average_change)
m_dec = average_change.index(min(average_change)) + 1   
        
       
print ('Financial Analysis')
print ('-----------------------------------')
print(f'Total Months: {monthly_total}')
print(f'Total: $ {proloss_total}')
print(f'Average Change: $ {round(average_change_total,2)}')
print (f'Greatest Increase in Profits: {total_months[m_inc]} (${great_inc})')
print (f'Greatest Decrease in Profits: {total_months[m_dec]} (${great_dec})')


filepath = os.path.join('Analytics','pybank_output.txt')
with open(filepath,'w') as file:
    file.write ('Financial Analysis')
    file.write ("\n")
    file.write ('-----------------------------------')
    file.write ("\n")
    file.write (f'Total Months: {monthly_total}')
    file.write ("\n")
    file.write (f'Total: $ {proloss_total}')
    file.write ("\n")
    file.write (f'Average Change: $ {round(average_change_total,2)}')
    file.write ("\n")
    file.write (f'Greatest Increase in Profits: {total_months[m_inc]} (${great_inc})')
    file.write ("\n")
    file.write (f'Greatest Decrease in Profits: {total_months[m_dec]} (${great_dec})')