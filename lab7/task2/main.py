from models import GasCar, ElectricCar

def main():
    mustang = GasCar("Ford", "Mustang", 1969, 60)
    tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
    
    fleet = [mustang, tesla]
    
    print("--- Vehicle Fleet Management ---\n")
    
    for vehicle in fleet:
        print(f"Vehicle: {vehicle}")
        print(f"Action: {vehicle.start_engine()}")
        
        if isinstance(vehicle, GasCar):
            print(f"Fuel Info: {vehicle.refuel()}")
        elif isinstance(vehicle, ElectricCar):
            print(f"Battery Info: {vehicle.check_range()}")
        
        print("-" * 30)

if __name__ == "__main__":
    main()