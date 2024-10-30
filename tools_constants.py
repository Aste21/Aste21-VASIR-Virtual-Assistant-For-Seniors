from tools import *

# Tool registration
tools = [
    {
        "type": "function",
        "function": {
            "name": "change_volume",
            "description": "Zmienia głośności mowy",
            "parameters": {
                "type": "object",
                "properties": {
                    "volume_level": {
                        "type": "number",
                        "minimum": 0,
                        "maximum": 10,
                        "default": 5,
                        "description": "Docelowy poziom głośności (od 1 do 10) dla pliku lub rozmowy. Domyśna wartość to 5.",
                    }
                },
                "required": ["volume_level"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_medicine",
            "description": """Dodaje lek do bazy danych.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nazwa lekarstwa",
                    },
                    "pills_count": {
                        "type": "number",
                        "description": "Ilosc tabletek jaka powinna byc wzieta",
                    },
                    "when_to_take_day": {
                        "type": "array",
                        "description": "Dzien tygodnia w ktory powinien byc wziety lek",
                        "items": {"type": "string"},
                    },
                    "when_to_take_hours": {
                        "type": "array",
                        "description": "Godzina o ktorej powinien byc wziety lek",
                        "items": {"type": "integer", "minimum": 0, "maximum": 23},
                    },
                    "when_to_take_minutes": {
                        "type": "array",
                        "description": "Minuta w godzinie o ktorej powinien byc wziety lek",
                        "items": {"type": "number", "minimum": 0, "maximum": 59},
                    },
                },
                "required": [
                    "name",
                    "pills_count",
                    "when_to_take_day",
                    "when_to_take_hours",
                    "when_to_take_minutes",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_event",
            "description": "Dodaje wydarzenie z nazwa i data",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_name": {
                        "type": "string",
                        "description": "Nazwa lub tytul wydarzenia",
                    },
                    "event_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Data wydarzenia w formacie RRRR-MM-DD",
                    },
                },
                "required": ["event_name", "event_date"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "set_monthly_budget",
            "description": "Ustala budzet na specyficzny miesiac i rok",
            "parameters": {
                "type": "object",
                "properties": {
                    "month": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 12,
                        "description": "Miesiąc budzetu reprezentowany jako liczba calkowita od 1 do 12",
                    },
                    "year": {
                        "type": "integer",
                        "description": "Rok",
                    },
                    "amount": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Wysokość budzetu na dany miesiac",
                    },
                },
                "required": ["month", "year", "amount"],
            },
        },
    },
]

available_functions = {
    "change_volume": change_volume,
    "add_medicine": add_medicine,
    "add_event": add_event,
    "set_monthly_budget": set_monthly_budget,
}
