from pathlib import Path
import overheads
import cash_on_hand
import profit_loss

def main():
    overheads_result = overheads.overheads_function()
    cash_on_hand_result = cash_on_hand.cash_on_hand()
    profit_and_loss_result = profit_loss.profit_and_loss_function()

    # Write the results to the summary_report.txt file 
    with open('summary_report.txt', 'w') as file:

        file.write(overheads_result + '\n')
        file.write(cash_on_hand_result + '\n')
        file.write(profit_and_loss_result + '\n')

if __name__ == "__main__":
    main()