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

#notowanie waznych dat - urodziny, wizyty itd.
def add_event(event_name: str, event_date: str):
    event = {"name": event_name, "date": event_date}
    print(f"Dodano wydarzenie: {event}") 
    return event

def set_monthly_budget(month: int, year: int, amount: float):
    if 1 <= month <= 12 and year > 0 and amount >= 0:
        budget = {"month": month, "year": year, "amount": amount}
        print(f"Monthly budget set: {budget}")
        return budget
    else:
        raise ValueError("Niepoprawny miesiąc, data albo suma. Miesiąc powinien istnieć, rok i budzet powinny być wartością dodatnią.")