class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        return f"The {self.brand} {self.model}'s engine is now humming."

    def stop_engine(self):
        self.is_running = False
        return f"The {self.brand} {self.model} has been turned off."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class GasCar(Vehicle):
    def __init__(self, brand, model, year, fuel_capacity):
        super().__init__(brand, model, year)
        self.fuel_capacity = fuel_capacity

    def start_engine(self):
        self.is_running = True
        return f"The {self.brand} roars to life with a combustion rumble!"

    def refuel(self):
        return f"Filling the {self.fuel_capacity}L tank with gasoline."


class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_kwh):
        super().__init__(brand, model, year)
        self.battery_kwh = battery_kwh

    def start_engine(self):
        self.is_running = True
        return f"The {self.brand} {self.model} powers up silently with a digital chime."

    def check_range(self):
        dist = self.battery_kwh * 6
        return f"Estimated range: {dist} km."