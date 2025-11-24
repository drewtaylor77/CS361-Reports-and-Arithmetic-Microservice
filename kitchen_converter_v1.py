# -*- coding: utf-8 -*-

class CookingConverter:
    def __init__(self):
        self.conversions = {
            "volume": {
                "teaspoon": 5,           # mL
                "tablespoon": 15,        # mL
                "fluid_ounce": 30,       # mL
                "cup": 250,              # mL
                "pint": 500,             # mL
                "quart": 950,            # mL
                "gallon": 3800           # mL
            },
            "weight": {
                "ounce": 28,             # grams
                "pound": 454             # grams
            },
            "temperature": {
                "F_to_C": lambda f: round((f - 32) * 5 / 9, 1),
                "C_to_F": lambda c: round((c * 9 / 5) + 32, 1)
            }
        }

    def convert_volume(self, amount, unit=None, to_metric=True):
        conv = self.conversions["volume"]
        if to_metric:
            unit = unit.lower()
            if unit in conv:
                return amount * conv[unit]
            raise ValueError(f"Unknown imperial volume unit: {unit}")
        else:
            # Round to nearest common kitchen volume unit
            sorted_units = sorted(conv.items(), key=lambda x: x[1])
            best_match = min(sorted_units, key=lambda x: abs(amount - x[1]))
            rounded_amount = round(amount / best_match[1], 2)
            return rounded_amount, best_match[0]
    
    def convert_weight(self, amount, unit=None, to_metric=True):
        conv = self.conversions["weight"]
        if to_metric:
            unit = unit.lower()
            if unit in conv:
                return amount * conv[unit]
            raise ValueError(f"Unknown imperial weight unit: {unit}")
        else:
            # Round to nearest common kitchen weight unit
            sorted_units = sorted(conv.items(), key=lambda x: x[1])
            best_match = min(sorted_units, key=lambda x: abs(amount - x[1]))
            rounded_amount = round(amount / best_match[1], 2)
            return rounded_amount, best_match[0]

    def convert_temperature(self, value, direction="F_to_C"):
        if direction not in self.conversions["temperature"]:
            raise ValueError("Direction must be 'F_to_C' or 'C_to_F'")
        return self.conversions["temperature"][direction](value)
