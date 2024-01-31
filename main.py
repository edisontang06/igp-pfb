from pathlib import Path
import cash_on_hand, overheads, profit_and_loss

def get_second_element(item):
    return item[1]

# create a text file named as "Summary_Report"
text_file = Path.cwd()/"Summary_Report.txt"
# Checks if file exists
if text_file.exists() == False:
    text_file.touch()
with text_file.open(mode="w") as file:

    # writes largest overhead and thee percentage
    file.write(f"[LARGEST OVERHEAD] {overheads.largest_overheads()[0]}: {overheads.largest_overheads()[1]}%")

    # Checks if cash on hand is in surplus
    if cash_on_hand.cash_change_calculator()[0][1] > 0:
        # writes day with highest cash surplus
        file.write("\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST CASH SURPLUSH] DAY: {cash_on_hand.cash_change_calculator()[0]}, AMOUNT: SGD{cash_on_hand.cash_change_calculator()[1]}")
    else:
        # writes the days with cash deficit and the amount
        for day in cash_on_hand.cash_change_calculator():
            file.write(f"\n[CASH DEFICIT] DAY: {day[0]}, AMOUNT: SGD{day[1] * -1}")

        # writes top 3 days with largest cash deficit
        cash_deficit = cash_on_hand.cash_change_calculator()
        cash_deficit.sort(key=get_second_element)
        file.write(f"\n[LARGEST CASH DEFICIT] DAY{cash_deficit[0][0]}, AMOUNT: SGD{cash_deficit[0][1] * -1}")
        if len(cash_deficit) > 1:
            file.write(f"\n[2ND LARGEST CASH DEFICIT]: DAY{cash_deficit[1][0]}, AMOUNT: SGD{cash_deficit[1][1] * -1}")
        if len(cash_deficit) > 2:
            file.write(f"\n[3RD LARGEST CASH DEFICIT]: DAY{cash_deficit[2][0]}, AMOUNT: SGD{cash_deficit[2][1] * -1}")

    # checks if net profit is in surplus
    if profit_and_loss.profit_change_calculator()[0][1] > 0:
        # writes day with largest profit surplus
        file.write("\n[NET PROFIT SURPLUS] PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        file.write(f"\n[HIGHEST NET PROFIT SURPLUS] DAY: {profit_and_loss.profit_change_calculator()[0]}, AMOUNT: SGD{profit_and_loss.profit_change_calculator()[1]}")
    else:
        # writes the days with cash deficit
        for day in profit_and_loss.profit_change_calculator():
            file.write(f"\n[NET PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: SGD{day[1] * -1}")

        # writes top 3 days with largest net profit deficit
        profit_deficit = profit_and_loss.profit_change_calculator()
        profit_deficit.sort(key=get_second_element)
        file.write(f"\n[LARGEST NET PROFIT DEFICIT] DAY{profit_deficit[0][0]}, AMOUNT: SGD{profit_deficit[0][1] * -1}")
        if len(profit_deficit) > 1:
            file.write(f"\n[2ND LARGEST NET PROFIT DEFICIT]: DAY{profit_deficit[1][0]}, AMOUNT: SGD{profit_deficit[1][1] * -1}")
        if len(profit_deficit) > 2:
            file.write(f"\n[3RD LARGEST NET PROFIT DEFICIT]: DAY{profit_deficit[2][0]}, AMOUNT: SGD{profit_deficit[2][1] * -1}")