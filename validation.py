from exceptions import invalidExpense

CATEGORIES = [
    "Food"
    "Shopping"
    "Education"
    "Health"
    "Entertainmet",
    "Other"


]

def validateTitle(title):
    title = title.strip()
    if not title:
        invalidExpense("Title cannot be empty!")

    return title

def validateAmount(amount):
    try:
        amount = float(amount)

    except ValueError:
        invalidExpense("Amount must be a number!")
    if amount <= 0:
        invalidExpense("Amount must be greather than 0!")
    return amount
        
