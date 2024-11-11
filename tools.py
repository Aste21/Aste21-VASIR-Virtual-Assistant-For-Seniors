from data_classes import *

# Function to change volume
def change_volume(volume_level: int):
    global volume
    if 0 <= volume_level <= 10:
        volume = volume_level
        print("Volume changed to: " + str(volume))
    else:
        raise ValueError("Volume level must be between 0 and 10")

def add_medicine(
    name: str,
    pills_count: float,
    when_to_take_day,
    when_to_take_hours,
    when_to_take_minutes,
):
    when_to_take = []
    for i in range(len(when_to_take_hours)):
        when_to_take.append(
            Date(when_to_take_day[i], when_to_take_hours[i], when_to_take_minutes[i])
        )
    medicine = Medicine(name, pills_count, when_to_take)
    print(medicine)

def add_event(day: int, month: str, year: int, hour: int, minute: int, content: str, reminders: list = None):
    # Default reminders if none are provided
    if reminders is None:
        reminders = [
            {'days_before': 1, 'hours_before': 0, 'minutes_before': 0},
            {'days_before': 0, 'hours_before': 2, 'minutes_before': 0}
        ]
    
    # Create the event with the appropriate reminders
    event = Event(day, month, year, hour, minute, content, reminders)
    
    return event

def create_shopping_list():
    shopping_list = []
    print(f"Stworzono listę zakupów")
    return shopping_list

def add_to_shopping_list(products, shopping_list):
    for product in products:
        shopping_list.append(product)
        print(f"Dodano produkt do listy zakupów: {product}")
    return shopping_list

def delete_from_shopping_list(products, shopping_list):
    for product in products:
        if product in shopping_list:
            shopping_list.remove(product)
            print(f"Usunięto produkt z listy zakupów: {product}")
        else:
            print(f"Produkt {product} nie znajduje się na liście zakupów.")
    return shopping_list

#notowanie budzetu na dany rok i miesiac 
def set_monthly_budget(month: int, year: int, amount: float):
    if 1 <= month <= 12 and year > 0 and amount >= 0:
        budget = {"month": month, "year": year, "amount": amount}
        print(f"Monthly budget set: {budget}")
        return budget
    else:
        raise ValueError("Niepoprawny miesiąc, data albo suma. Miesiąc powinien istnieć, rok i budzet powinny być wartością dodatnią.")
  
#add_income and add_spending need to lather fetch the budget from the database.
#Currently there is a problem with adding a spending or an income when the budget has not yet been set.
  
def add_spending(budget: dict, expense: float, description: str):
    if 'amount' in budget and budget['amount'] >= expense >= 0:
        budget['amount'] -= expense
        print(f"Added spending: {description}, amount: {expense}. Remaining budget: {budget['amount']}")
        return budget
    else:
        raise ValueError("Invalid expense amount or budget exceeded.")
    
def add_income(budget: dict, income: float, description: str): 
    if 'amount' in budget and income >= 0:
        budget['amount'] += income
        print(f"Added income: {description}, amount: {income}. New budget total: {budget['amount']}")
        return budget
    else:
        raise ValueError("Invalid income amount.")
    

def add_recurring_spending(budget: dict, expense: float, description: str, recurrence: str):
    if recurrence != "monthly":
        raise ValueError("Currently, only monthly recurrence is supported.")

    if 'amount' in budget and budget['amount'] >= expense >= 0:
        budget['amount'] -= expense
        print(f"Added recurring spending: {description}, amount: {expense}. Remaining budget: {budget['amount']}")
        return budget
    else:
        raise ValueError("Invalid recurring expense amount or budget exceeded.")
  
#potem tez by sie przydalo dodac te przypomnienia jak juz asystent bedzie mial dostep do zegara
def add_recurring_spending(expense: float, description: str, recurrence: str):
    if recurrence != "monthly":
        raise ValueError("Currently, only monthly recurrence is supported.")

    recurring_expense = {"expense": expense, "description": description, "recurrence": recurrence}
    print(f"Recurring spending noted: {recurring_expense}")
    return recurring_expense

#pierwsza gra ktora imo bylaby spoko to memory lane quiz:
#jak dziala: Asystent zadaje osobie pytania o jej przeszłość (dzieciństwo, ulubione #wspomnienia, miejsca, które odwiedziła, dawne hobby, itp.). Liczy punkty za kazda dobra odp.

def collect_memory_info():
    memories = []
    print("Zbierzmy kilka wspomnień do Twojego quizu! Zadamy kilka pytań.")

    while True:
        question = input("Jakie pytanie chciałbyś dodać do quizu? (np. 'Jak miał na imię Twój pierwszy zwierzak?')\n")
        answer = input(f"Jaka jest odpowiedź na to pytanie?\n")

        memories.append({"question": question, "answer": answer})
        print("Wspomnienie zapisane!\n")

        more = input("Czy chcesz dodać kolejne wspomnienie? (tak/nie)\n").strip().lower()
        if more != 'tak':
            break

    print("Wszystkie wspomnienia zostały zapisane! Możemy rozpocząć quiz w dowolnym momencie.")
    return memories

def memory_lane_quiz(memories=None):
    if not memories:
        print("Nie masz jeszcze zapisanych wspomnień do quizu. Zbierzmy je teraz!")
        memories = collect_memory_info()

    print("Witaj w quizie Ścieżka Wspomnień! Zobaczymy, jak wiele pięknych chwil uda Ci się przypomnieć.")
    score = 0

    for memory in memories:
        user_answer = input(f"{memory['question']}\n")
        if user_answer.strip().lower() == memory['answer'].strip().lower():
            print("Świetnie! To naprawdę wspaniale, że pamiętasz!")
            score += 1
        else:
            print(f"To nic, pamięć bywa kapryśna! Poprawna odpowiedź to: {memory['answer']}.")

    print(f"Quiz zakończony! Twój wynik końcowy: {score} z {len(memories)}. Pamięć to piękna podróż, gratuluję udziału!")
