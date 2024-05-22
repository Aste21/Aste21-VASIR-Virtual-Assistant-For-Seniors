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
                        "description": "Docelowy poziom głośności (od 1 do 10) dla pliku lub rozmowy. Domyśna wartość to 5."
                    }
                },
                "required": ["volume_level"]
            }
        }
    }
]

available_functions = {
    "change_volume": change_volume,
}