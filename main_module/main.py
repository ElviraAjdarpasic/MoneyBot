from finance.analysis import FinanceAnalysis
from system.loggin_util import setup_logger

#Funktion som säkerhetställer att användaren matar in heltal
def safe_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a valid number!")

#Start funktionen för själva MoneyBot
def start_moneybot():
    logger = setup_logger("MoneyBot")
    logger.info("MoneyBot started")
    
    #Frågar användaren om värden
    income = safe_int_input("Monthly income: ")
    rent = safe_int_input("Rent: ")
    food = safe_int_input("Food costs: ")

    transactions = [income, -rent, -food]
    analysis = FinanceAnalysis(transactions)

    print("\n====ECONOMIC REPORT====")
    print("Income:", analysis.total_income())
    print("Expenses:", analysis.total_expenses())
    print("Balance:", analysis.total_balance())
    print("Predicted next month:", analysis.predicted_next_month())

if __name__ == "__main__":
    start_moneybot()



