import os
from finance.analysis import FinanceAnalysis
from system.logger import setup_logger
from colorama import init, Fore, Style
init(autoreset=True)

#Importera funktioner för att spara och visa rapporter
from reports.report_manager import add_report, list_reports, show_report, _load_reports, _save_reports

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
    print("\n")
    print(" " * 15 + "✨ Prediction: Keep an eye on your spending!")
    print(" " * 6 + "This shows how much money could stay in your pocket next month")
    print(" " * 15 +"if you keep things similar! 🌸")
    print("\n\n")
    print("Who’s using MoneyBot today?")
    print("\n")

    # Förnamn
    while True:
        first_name = input("What's your first name? ").strip().capitalize()
        if first_name.isalpha() and len(first_name):
            break
        else:
            clear_screen()
            print("\n\n")
            print(" " * 15 + "Welcome to your personal MoneyBot! 💰💕")
            print(" " * 10 + "I'm here to help you get full control of your finances")
            print(" " * 15 + "in a simple and fun way! 🌸")
            print("\n")
            print(" " * 15 + "✨ Prediction: Keep an eye on your spending!")
            print(" " * 6 + "This shows how much money could stay in your pocket next month")
            print(" " * 15 +"if you keep things similar!")
            print("\n\n")
            print("Who’s using MoneyBot today?")
            print("\n")            
            print(Fore.RED +"Oops! Please enter a real last name (letters only) 💕"+ Style.RESET_ALL)
    #Efternamn
    while True:
        last_name = input("And your last name? ").strip().capitalize()
        if last_name.isalpha() and len(last_name):
            break  
        else:  
            clear_screen()
            print("\n\n")
            print(" " * 15 + "Welcome to your personal MoneyBot! 💰💕")
            print(" " * 10 + "I'm here to help you get full control of your finances")
            print(" " * 15 + "in a simple and fun way! 🌸")
            print("\n")
            print(" " * 15 + "✨ Prediction: Keep an eye on your spending!")
            print(" " * 6 + "This shows how much money could stay in your pocket next month")
            print(" " * 15 +"if you keep things similar!")
            print("\n\n")
            print("Who’s using MoneyBot today?")
            print("\n")
            print(f"First name: {first_name} ✓")
            print(Fore.RED +"Oops! Please enter a real last name (letters only) 💕"+ Style.RESET_ALL)
            
    full_name = f"{first_name} {last_name}"
    
    while True:
        clear_screen()
        print("\n\n")
        print(" " * 15 + "Welcome to your personal MoneyBot! 💰💕")
        print(" " * 10 + "I'm here to help you get full control of your finances")
        print(" " * 15 + "in a simple and fun way! 🌸")
        print("\n")
        print(" " * 15 + "✨ Prediction: Keep an eye on your spending!")
        print(" " * 6 + "This shows how much money could stay in your pocket next month")
        print(" " * 15 +"if you keep things similar!")
        print("\n\n")
        print("Who’s using MoneyBot today?")
        print("\n")
        print(f"Your name: {first_name}")
        print(f"Your lastname: {last_name}")
        print("\n")
        print("Is it correct(Answer Yes or No)?")
        answer = input( "> ").strip().lower()

        if answer in ["yes", "y"]:
            break
        elif answer in ["no", "n"]:
            clear_screen()
            print("\n\n")
            print(" " * 15 + "Okey, Lets start over.💕")
            print("\n")

            #Startar från början med att fråga om förnamn
            return welcome_user()
        else:
            clear_screen()
            print(" " * 15 + "Please answer yes or no!")
            print("\n")
            
    clear_screen()
    print("\n\n\n")
    print(" " * 20 + f"Hi {full_name}!") 
    print("\n")
    print(" " * 20 +"So happy you're here! 🎀✨")
    print(" " * 14 + "Now let's organize your finances together 💕")
    print("\n\n\n")
    input(Fore.BLUE + " " * 18 +"Press Enter to go to the menu..."+ Style.RESET_ALL)
    clear_screen()
            
    return full_name
            
#Funktion som säkerhetställer att användaren matar in heltal           
def safe_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + " " * 18 + "Oops! Please enter a valid number (you can use decimals) 💕!" + Style.RESET_ALL)

#Start funktionen för själva MoneyBot
def run_moneybot_analysis():
    logger = setup_logger("MoneyBot")
    logger.info("Running new economic analysis")

    print("\n")
    print(" " * 18 + Fore.MAGENTA + "=== MoneyBot - Monthly Budget ===" + Style.RESET_ALL)
    print(" " * 18 + "Enter your approximate values below:\n")

    income = safe_float_input(" " * 18 + "Monthly income: ")
    rent = safe_float_input(" " * 18 + "Rent: ")
    food = safe_float_input(" " * 18 + "Food costs: ")

    analysis = FinanceAnalysis([income, -rent, -food])

    report = (
         "\n" * 3 +
        Fore.CYAN + "==== ECONOMIC REPORT ====" + Style.RESET_ALL + "\n"
        f"Income: {analysis.total_income():.2f}\n"
        f"Expenses: {analysis.total_expenses():.2f}\n"
        f"Balance: {analysis.total_balance():.2f}\n"
        f"Estimated money left for next month: {analysis.predicted_next_month():.2f}\n"    
        )

    comments = []

    balance = analysis.total_balance()
    predicted = analysis.predicted_next_month()

    if balance > 0:
        comments.append("Nice! You've got money left this month! Great job! 🎉")

        if predicted > balance:
            comments.append("Next month looks even better if you keep this up! 🚀")
        elif predicted < balance:
            comments.append("Next month might be a bit tighter... aim to save more or cut spending! 💪")
        else:
            comments.append("Next month looks about the same as this one! Steady! 🌟")
    else:
        comments.append("Uh oh... this month ended in the red. No panic... it happens! 😅")

        if predicted > balance:
            comments.append("Next month could turn around! Keep an eye on spending! 💕")
        else:
            comments.append(
                "If you keep going like this, next month will be tough too... "
                "try cutting back! You've got this!"
            )

    return report, comments
    
#Huvudmenyn
def main_menu():
    full_name = welcome_user()
    clear_screen()
    
    while True:
        clear_screen()
        print("\n" * 3)
        print(" " * 18 + Fore.MAGENTA + Style.BRIGHT + "=== MoneyBot ===" + Style.RESET_ALL)        
        print(" " * 18 + "1. Create new report")
        print(" " * 18 + "2. View or Delete previous reports")
        print(" " * 18 + "3. Exit")
        print(" " * 18 + "==================")
        print("\n")

        choice = input(" " * 18 + "Choose an option (1-3): ").strip()
        
        if choice == "1":
            clear_screen()
            report, comments = run_moneybot_analysis()
            add_report(report, full_name)

            print("\n")
            print(" " * 18 + Fore.GREEN + "Report saved successfully! 🎀💕" + Style.RESET_ALL)
            print("\n")

            for line in report.split("\n"):
                print(" " * 18 + line)
            
            print()
            for c in comments:
                print(" " * 18 + f"[MoneyBot] INFO: {c}")
            
            print("\n")
            input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
            clear_screen()

        elif choice == "2":
            while True:
                clear_screen()
                print("\n" * 3)
                print(" " * 18 + Fore.CYAN + "==== MENY ====" + Style.RESET_ALL)
                print(" " * 18 + "1. View a report")
                print(" " * 18 + "2. Delete a report")
                print(" " * 18 + "3. Back to main menu")
                print(" " * 18 + "==================")
                
                sub_choice = input(" " * 18 + "Choose an option (1-3): ").strip()
                
                if sub_choice == "1":
                    clear_screen()
                    user_reports_exist = list_reports(full_name)

                    if not user_reports_exist:
                        print(" " * 18 + "You haven't created any reports yet! 🌸")
                        print(" " * 18 + "Let's create your first one! 🎀")
                        print("\n")
                        input(Fore.BLUE + " " * 18 + "Press Enter to go back to main menu..." + Style.RESET_ALL)
                        clear_screen()
                        continue

                    while True:
                        clear_screen()
                        list_reports(full_name)

                        try:
                            choice_num = int(input(" " * 18 + "Select report number to view: "))

                            all_reports = _load_reports()
                            user_reports = [
                                r for r in all_reports
                                if r.get("name", "Unknown").title() == full_name.title()
                        ]
                        
                        
                            if choice_num < 1 or choice_num > len(user_reports):
                               print(Fore.RED + " " * 18 + "Invalid report number! Please try again." + Style.RESET_ALL)
                               input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                               continue

                            report = user_reports[choice_num - 1]
                            clear_screen()

                            print("\n")
                            for line in report["summary"].split("\n"):
                                print(" " * 18 + line)

                            print("\n" + " " * 18 + f"Report by: {report['name']} on {report['date']}")
                            input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                            clear_screen()
                            break

                        except ValueError:
                            print(Fore.RED + " " * 18 + "Please enter a number." + Style.RESET_ALL)
                            input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                            clear_screen()

                elif sub_choice == "2":
                    all_reports = _load_reports()
                    user_reports = [r for r in all_reports if r.get("name", "Unknown").title() == full_name.title()]
                    
                    if not user_reports:
                        clear_screen()
                        print(" " * 18 + "You haven't created any reports yet! 🌸")
                        input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                        clear_screen()
                        continue
                    
                    clear_screen()
                    list_reports(full_name)
                    try:
                        num = int(input(" " * 18 + "Select ONE report number to delete: ")) - 1
                        if 0 <= num < len(user_reports):
                            deleted_report = user_reports[num]
                            for i, r in enumerate(all_reports):
                                if r == deleted_report:
                                    del all_reports[i]
                                    break
                            
                            _save_reports(all_reports)
                            clear_screen()
                            print(" " * 18 + Fore.GREEN + "Report deleted successfully! 🗑️✨" + Style.RESET_ALL)
                            print("\n")
                            input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                            clear_screen()
                        else:
                            print(Fore.RED + " " * 18 + "Invalid number! Please choose an existing report number." + Style.RESET_ALL)
                            input(Fore.BLUE + " " * 18 + "Press Enter to try again..." + Style.RESET_ALL)
                            clear_screen()
                    except ValueError:
                        print(Fore.RED + " " * 18 + "Please enter a number." + Style.RESET_ALL)
                        input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                        clear_screen()

                elif sub_choice == "3":
                    clear_screen()
                    break

                else:
                    print(Fore.RED + " " * 18 + "Invalid choice, please try again." + Style.RESET_ALL)
                    input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
                    clear_screen()

        elif choice == "3":
            clear_screen()
            print("\n" * 4)
            print(" " * 20 + "Thank you for using MoneyBot!")
            print(" " * 20 + "Have a great day! 💕")
            print("\n" * 3)
            break

        else:
            print(Fore.RED + " " * 18 + "Invalid choice, please try again." + Style.RESET_ALL)
            input(Fore.BLUE + " " * 18 + "Press Enter to continue..." + Style.RESET_ALL)
            clear_screen()


# Starta programmet
if __name__ == "__main__":
    main_menu()
