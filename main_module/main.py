import os
from finance.analysis import FinanceAnalysis
from logger import setup_logger

#Importera funktioner för att spara och visa rapporter
from report_manager import add_report, list_reports, show_report

#funktion för att rensa skärmen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#Funktion som säkerhetställer att användaren matar in heltal
def safe_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

#Start funktionen för själva MoneyBot
def run_moneybot_analysis()-> str:
    logger = setup_logger("MoneyBot")
    logger.info("Running new economic analysis")
    
    #Frågar användaren om värden
    income = safe_int_input("Monthly income: ")
    rent = safe_int_input("Rent: ")
    food = safe_int_input("Food costs: ")

    transactions = [income, -rent, -food]
    analysis = FinanceAnalysis(transactions)

    #Skapar en fin raport
    report = (
        "==== ECONOMIC REPORT ====\n" 
        f"Income: {analysis.total_income()}\n" 
        f"Expenses: {analysis.total_expenses()}\n" 
        f"Balance: {analysis.total_balance()}\n" 
        f"Predicted next month: {analysis.predicted_next_month()}\n"
    )
    return report

#Huvudmenyn
def main_menu():
    while True:
        print("\n\n=== MoneyBot ===")
        print("1. Create new report")
        print("2. View previous reports")
        print("3. Exit")
        print("==================")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            clear_screen()
            summary = run_moneybot_analysis()
            add_report(summary)           
            print(summary)
            input("\nPress Enter to continue...")
        elif choice == "2":
            clear_screen()
            if list_reports():       
                try:
                    num = int(input("Select report number: ")) - 1
                    clear_screen()
                    show_report(num)
                except ValueError:
                    print("Invalid number!")
                except IndexError:
                    print("Report number does not exist!")
            input("\nPress Enter to continue...")

        elif choice == "3":
            clear_screen()
            print("Thank you for using MoneyBot!")
            break

        else:
            print("Invalid choice, please try again.")
            input("\nPress Enter to continue...")

        #Rensa inför nästa varv i loopen
        clear_screen()


# Starta programmet
if __name__ == "__main__":
    main_menu()


