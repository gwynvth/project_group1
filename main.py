from pathlib import Path
# Import all the functions over to main.py
import overheads
import cash_on_hand
import profit_loss

def main():
    """
    -This function will will import all the
    functions from modular program to coordinate and 
    execute them into a text file.

    -Parameters required: None
    """
    
    # Calculate overheads result
    overheads_result = overheads.overheads_function()
    # Calculate cash on hand result
    cash_on_hand_result = cash_on_hand.cash_on_hand()
    # Calculate profit and loss result
    profit_and_loss_result = profit_loss.profit_and_loss_function()

    # Write the results to the summary_report.txt file 
    with open('summary_report.txt', 'w') as file:

        file.write(overheads_result + '\n')
        file.write(cash_on_hand_result + '\n')
        file.write(profit_and_loss_result + '\n')


# Check if this script is being run directly as the main program
if __name__ == "__main__":
    main()