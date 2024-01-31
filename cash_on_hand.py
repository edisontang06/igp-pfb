from pathlib import Path
import csv

def cash_on_hand_reader():
    '''
    Function to read cash_on_hand.csv file
    No parameters needed
    '''
    fp = Path.cwd()/"CSV_Files"/"cash_on_hand.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        global cash_on_hand_list
        # create an empty list to store days and cash on hand
        cash_on_hand_list = [] 

        # append days and cash on hand into the list
        for row in reader:
            cash_on_hand_list.append([row[0],float(row[1])])
    return cash_on_hand_list

def cash_change_calculator():
    '''
    Calculates the cash deficit days or highest cash surplus day
    No parameters needed
    '''
    # calls function to read Net-Profit file
    cash_on_hand_reader()

    # value storing
    change_of_cash = []
    deficit_days = []
    largest_increment = []

    # Calculates the changes in cash
    for day,profit in enumerate(cash_on_hand_list[1:],start=11):
        net_profit_change = profit[1] - cash_on_hand_list[day - 11][1]
        change_of_cash.append([day, net_profit_change])

    # Finds the days where cash change is negative
    for day in change_of_cash:
        if day[1] < 0:
            deficit_days.append(day)

    # Checks if net profit is always increasing
    if deficit_days == []:
        # returns day with largest increment
        largest_surplus = 0
        largest_surplus_day = 0
        for surplus in change_of_cash:
            if surplus[1] > largest_surplus:
                largest_surplus = surplus[1]
                largest_surplus_day = int(surplus[0])
        largest_increment.append(change_of_cash[largest_surplus_day - 11])
        return largest_increment

    # Returns days where profit is in a deficit
    return deficit_days