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
]

available_functions = {"change_volume": change_volume, "add_medicine": add_medicine}
