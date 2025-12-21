import os
from reports.report_manager import add_report, list_reports, show_report, _load_reports, _save_reports
from finance.analysis import FinanceAnalysis
from system.logger import setup_logger

#Importera funktioner för att spara och visa rapporter
from reports.report_manager import add_report, list_reports, show_report

#funktion för att rensa skärmen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def center_print(text):
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    print(text.center(terminal_width))

def welcome_user():
    clear_screen()
    print("\n\n")
    print(" " * 15 + "Welcome to your personal MoneyBot! 💰💕")
    print(" " * 10 + "I'm here to help you get full control of your finances")
    print(" " * 15 + "in a simple and fun way! 🌸")
    print("\n\n")

    while True:
        first_name = input("   What's your first name? ").strip().capitalize()
        if first_name.isalpha() and len(first_name) > 2:
            break
        print("   Oops! Please enter a real first name (letters only) 💕")
    
    while True:
        last_name = input("   And your last name? ").strip().capitalize()
        if last_name.isalpha() and len(last_name) > 2:
            break
        print("   Oops! Please enter a real last name (letters only) 💕")
    
    full_name = f"{first_name} {last_name}"
    
    clear_screen()
    print("\n\n\n")
    print(" " * 20 + f"Hi {full_name}! So happy you're here! 🎀✨")
    print(" " * 15 + "Now let's organize your finances together 💕")
    print("\n\n\n")
    input("   Press Enter to go to the menu...")
    return full_name

#Funktion som säkerhetställer att användaren matar in heltal
def safe_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Oops! Please enter a valid number 💕!")

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
    full_name = welcome_user()
    clear_screen()

    while True:
        print("\n" * 3)

        print(" " * 18 + "=== MoneyBot ===")
        print(" " * 18 + "1. Create new report")
        print(" " * 18 + "2. View previous reports")
        print(" " * 18 + "3. Exit")
        print(" " * 18 + "==================")
        print("\n" * 2)

        choice = input(" " * 18 + "Choose an option (1-3): ").strip()

        if choice == "1":
            clear_screen()
            summary = run_moneybot_analysis()
            add_report(summary, full_name)           
            print("\n" + summary)
            input("\n" + " " * 18 + "Press Enter to continue...")

        elif choice == "2":
            clear_screen()
            while True:
                if not list_reports(full_name):
                    print(" " * 18 + "You haven't created any reports yet! 🌸")
                    print(" " * 18 + "Let's create your first one! 🎀")
                    input("\n" + " " * 18 + "Press Enter to go back to main menu...")
                    break

                print(" " * 18 + "1. View a report")
                print(" " * 18 + "2. Delete a report")
                print(" " * 18 + "3. Back to main menu")
                print(" " * 18 + "==================")

                sub_choice = input(" " * 18 + "Choose an option (1-3): ").strip()

                if sub_choice == "1":
                    clear_screen()
                    list_reports(full_name)  # Visar listan igen
                    try:
                        num = int(input(" " * 18 + "Select report number to view: ")) - 1
                        clear_screen()
                        show_report(num, full_name)
                        input("\n" + " " * 18 + "Press Enter to continue...")
                    except ValueError:
                        print(" " * 18 + "Invalid number! 😅")
                        input("\n" + " " * 18 + "Press Enter to continue...")
                    except IndexError:
                        print(" " * 18 + "Report number does not exist! 😅")
                        input("\n" + " " * 18 + "Press Enter to continue...")

                elif sub_choice == "2":
                    clear_screen()
                    list_reports(full_name)
                    try:
                        num = int(input(" " * 18 + "Select report number to delete: ")) - 1
                        # Här hämtar vi alla rapporter och raderar den valda
                        all_reports = _load_reports()
                        user_reports = [r for r in all_reports if r.get("name", "Unknown").title() == full_name.title()]
                        if 0 <= num < len(user_reports):
                            # Hitta index i hela listan och ta bort
                            deleted_report = user_reports[num]
                            all_reports.remove(deleted_report)
                            _save_reports(all_reports)
                            clear_screen()
                            print(" " * 18 + "Report deleted successfully! 🗑️✨")
                        else:
                            print(" " * 18 + "Invalid number!")
                    except ValueError:
                        print(" " * 18 + "Invalid input!")
                    input("\n" + " " * 18 + "Press Enter to continue...")

                elif sub_choice == "3":
                    break  # Går tillbaka till huvudmenyn

                else:
                    print(" " * 18 + "Invalid choice, try again! 😊")
                    input("\n" + " " * 18 + "Press Enter to continue...")

        elif choice == "3":
            clear_screen()
            print("\n" * 4)
            print(" " * 20 + "Thank you for using MoneyBot!")
            print(" " * 20 + "Have a great day! 💕")
            print("\n" * 3)
            break

        else:
            print(" " * 18 + "Invalid choice, please try again.")
            input("\n" + " " * 18 + "Press Enter to continue...")
        

        #Rensa inför nästa varv i loopen
        clear_screen()


# Starta programmet
if __name__ == "__main__":
    main_menu()


