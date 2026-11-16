def expensesNotFound():
    raise LookupError("Expense Not Found")

def invalidExpense(message):
    raise ValueError(message)