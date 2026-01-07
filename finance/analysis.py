class FinanceAnalysis:
    # Spara alla transaktioner
    def __init__(self, transactions: list[int]):
        self.transactions = transactions
        
    # Summan av alla inkomster
    def total_income(self):
        return sum(x for x in self.transactions if x > 0)

    # Summan av alla utgifter
    def total_expenses(self):
        return sum(x for x in self.transactions if x < 0)

    # Totalt saldo
    def total_balance(self):
        return sum(self.transactions)

    # Förutsäg nästa månads saldo baserat på genomsnitt
    def predicted_next_month(self):
        if not self.transactions:
            return 0
        average = sum(self.transactions) / len(self.transactions)
        return self.total_balance() + average
