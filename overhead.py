from pathlib import Path
import csv
def overheads_path_reader():
    '''
    Function to read overheads.csv file and appends data
    No parameters required
    '''
# create a file to csv file.
    fp = Path.cwd()/"csv_files"/"Overheads.csv"

    # read the csv file to append overheads
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store days and overhead
        global overhead_list
        overhead_list=[]

        # append store days and overhead into the overhead list
        for row in reader:
            overhead_list.append([row[0],row[1],row[3]])
        return overhead_list

def largest_overheads():
    '''
    Function to find the biggest overhead and the percentage
    '''
    # Create a dictionary to store the overheads
    overheads_path_reader()
    overheads = {}

    # Calculate total overhead for every category
    for expense in overhead_list:
        category = expense[1]
        amount = float(expense[2])
        if category in overheads:
            overheads[category] += amount
        else:
            overheads[category] = amount

    # Find the category with the highest overhead
    highest_overhead = max(overheads, key=overheads.get)
    highest_percentage = overheads[highest_overhead] / sum(overheads.values()) * 100
    return highest_overhead, round(highest_percentage,2)
