from tools import *

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
                        "description": "Docelowy poziom głośności (od 1 do 10) dla pliku lub rozmowy. Domyślnie ustawione na 5.",
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
            "description": "Dodaje lek do bazy danych.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nazwa lekarstwa",
                    },
                    "pills_count": {
                        "type": "number",
                        "description": "Ilość tabletek, które należy przyjąć",
                    },
                    "when_to_take_day": {
                        "type": "array",
                        "description": "Dni tygodnia, w które należy przyjąć lek",
                        "items": {"type": "string"},
                    },
                    "when_to_take_hours": {
                        "type": "array",
                        "description": "Godziny, w których należy przyjąć lek",
                        "items": {"type": "integer", "minimum": 0, "maximum": 23},
                    },
                    "when_to_take_minutes": {
                        "type": "array",
                        "description": "Minuty, w których należy przyjąć lek",
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
            "description": "Dodaje wydarzenie z nazwą, datą i opcjonalną listą gości",
            "parameters": {
                "type": "object",
                "properties": {
                    "event_name": {
                        "type": "string",
                        "description": "Nazwa lub tytuł wydarzenia",
                    },
                    "event_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Data wydarzenia w formacie RRRR-MM-DD",
                    },
                    "guest_list": {
                        "type": "array",
                        "description": "Opcjonalna lista gości wydarzenia",
                        "items": {"type": "string", "description": "Imię i nazwisko gościa"},
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
            "description": "Ustala budżet na specyficzny miesiąc i rok",
            "parameters": {
                "type": "object",
                "properties": {
                    "month": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 12,
                        "description": "Miesiąc budżetu reprezentowany jako liczba całkowita od 1 do 12",
                    },
                    "year": {
                        "type": "integer",
                        "description": "Rok",
                    },
                    "amount": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Wysokość budżetu na dany miesiąc",
                    },
                },
                "required": ["month", "year", "amount"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_spending",
            "description": "Rejestruje wydatki i odejmuje je od bieżącego budżetu",
            "parameters": {
                "type": "object",
                "properties": {
                    "budget": {
                        "type": "object",
                        "properties": {
                            "month": {"type": "integer"},
                            "year": {"type": "integer"},
                            "amount": {"type": "number"},
                        },
                        "description": "Budżet, z którego odejmowany jest wydatek",
                    },
                    "expense": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Kwota wydatku do odjęcia od budżetu",
                    },
                    "description": {
                        "type": "string",
                        "description": "Opis wydatku, np. jedzenie, paliwo",
                    },
                },
                "required": ["budget", "expense", "description"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_income",
            "description": "Rejestruje przychód i dodaje go do bieżącego budżetu",
            "parameters": {
                "type": "object",
                "properties": {
                    "budget": {
                        "type": "object",
                        "properties": {
                            "month": {"type": "integer"},
                            "year": {"type": "integer"},
                            "amount": {"type": "number"},
                        },
                        "description": "Budżet, do którego dodawany jest przychód",
                    },
                    "income": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Kwota przychodu do dodania do budżetu",
                    },
                    "description": {
                        "type": "string",
                        "description": "Opis przychodu, np. pensja, zwrot podatku",
                    },
                },
                "required": ["budget", "income", "description"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "add_recurring_spending",
            "description": "Dodaje powtarzający się wydatek jako notatkę",
            "parameters": {
                "type": "object",
                "properties": {
                    "expense": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Kwota powtarzającego się wydatku",
                    },
                    "description": {
                        "type": "string",
                        "description": "Opis wydatku, np. czynsz, media",
                    },
                    "recurrence": {
                        "type": "string",
                        "enum": ["monthly"],
                        "description": "Częstotliwość wydatku, obecnie obsługiwany tylko 'miesięczny'",
                    },
                },
                "required": ["expense", "description", "recurrence"],
            },
        },
    },
    # Adding the 'add_memory' function for storing memories:
    {
        "type": "function",
        "function": {
            "name": "add_memory",
            "description": "Dodaje wspomnienie do bazy danych.",
            "parameters": {
                "type": "object",
                "properties": {
                    "memory_name": {
                        "type": "string",
                        "description": "Nazwa wspomnienia",
                    },
                    "memory_description": {
                        "type": "string",
                        "description": "Opis wspomnienia",
                    },
                    "memory_date": {
                        "type": "string",
                        "format": "date",
                        "description": "Data wydarzenia w formacie RRRR-MM-DD",
                    },
                    "memory_details": {
                        "type": "string",
                        "description": "Szczegóły wspomnienia (np. jak się czułeś, co się wydarzyło)",
                    },
                },
                "required": ["memory_name", "memory_description", "memory_date", "memory_details"],
            },
        },
    },
    # Adding the 'memory_lane_quiz' function for the memory quiz
    {
        "type": "function",
        "function": {
            "name": "memory_lane_quiz",
            "description": "Uruchamia quiz Ścieżka Wspomnień, aby sprawdzić, ile pamiętasz.",
            "parameters": {
                "type": "object",
                "properties": {
                    "memories": {
                        "type": "array",
                        "description": "Lista zapisanych wspomnień, które będą używane w quizie",
                        "items": {"type": "object"},
                    }
                },
                "required": [],
            },
        },
    },
]

available_functions = {
    "change_volume": change_volume,
    "add_medicine": add_medicine,
    "add_event": add_event,
    "set_monthly_budget": set_monthly_budget,
    "add_spending": add_spending,
    "add_income": add_income,
    "add_recurring_spending": add_recurring_spending,
    "collect_memory_info": collect_memory_info,
    "memory_lane_quiz": memory_lane_quiz,
}
