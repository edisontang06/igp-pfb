from pathlib import Path
import csv

def profit_and_loss_reader():
    '''
    Function to read overheads.csv file
    No parameters needed
    '''
    fp = Path.cwd()/"CSV_Files"/"profit_and_loss.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        global profit_and_loss_list
        # create an empty list to store days and net profit
        profit_and_loss_list = [] 

        # append days and net profit into the profit_and_loss list
        for row in reader:
            profit_and_loss_list.append([row[0],float(row[4])])
    return profit_and_loss_list

def profit_change_calculator():
    '''
    Calculates the profit deficit days or highest profit surplus day
    No parameters needed
    '''
    # calls function to read Net-Profit file
    profit_and_loss_reader()

    # value storing
    change_of_net_profit = []
    deficit_days = []
    largest_increment = []

    # Calculates the changes in net profit
    for day,profit in enumerate(profit_and_loss_list[1:],start=11):
        net_profit_change = profit[1] - profit_and_loss_list[day - 11][1]
        change_of_net_profit.append([day, net_profit_change])

    # Finds the days where net profit change is negative
    for day in change_of_net_profit:
        if day[1] < 0:
            deficit_days.append(day)

    # Checks if net profit is always increasing
    if deficit_days == []:
        # returns day with largest increment
        largest_surplus = 0
        largest_surplus_day = 0
        for surplus in change_of_net_profit:
            if surplus[1] > largest_surplus:
                largest_surplus = surplus[1]
                largest_surplus_day = int(surplus[0])
        largest_increment.append(change_of_net_profit[largest_surplus_day - 11])
        return largest_increment

    # Returns days where profit is in a deficit and top 3 days
    return deficit_days
