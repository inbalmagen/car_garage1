
import cars
from cars.actions import add_car, delete_car, search_car
from cars.problems import calculate_price, calculate_total_profit, get_total_cars, available_problems


def main_menu():
    while True:
        print("\n--- Car Garage Menu ---")
        print("1. List all cars")
        print("2. Add a car")
        print("3. Delete a car")
        print("4. Search for a car")
        print("5. Calculate total cars and profit")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_cars_menu()
        elif choice == '2':
            add_a_car()
        elif choice == '3':
            delete_a_car()
        elif choice == '4':
            search_for_car()
        elif choice == '5':
            calculate_total_cars_and_profit()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def list_all_cars_menu():
    cars = list_all_cars()
    print("\n--- List of Cars ---")
    for car in cars:
        print(f"Car Number: {car['Car Number']}, Problems: {', '.join(car['Problems'])}, Price: {car['price']} NIS")

def add_a_car():
    car_number = input("Enter Car Number: ")
    problems = select_problems()
    price = calculate_price(problems)
    print(f"The price of this fix is: {price} NIS.")
    decision = input("Do you wish to proceed? (yes/no): ")
    if decision.lower() == 'yes':
        add_car({'Car Number': car_number, 'Problems': problems, 'price': price})
        print("Car added successfully.")
    else:
        print("Car not added.")

def delete_a_car():
    car_number = input("Enter Car Number to delete: ")
    delete_car(car_number)
    print("Car deleted successfully.")

def search_for_car():
    car_number = input("Enter Car Number to search: ")
    car = search_car(car_number)
    if car:
        print(f"Car found - Car Number: {car['Car Number']}, Problems: {', '.join(car['Problems'])}, Price: {car['price']} NIS")
    else:
        print("Car not found.")

def calculate_total_cars_and_profit():
    print(f"Currently there are {get_total_cars()} cars.")
    print(f"The current profit is: {calculate_total_profit()} NIS.")

def select_problems():
    selected_problems = []
    while True:
        print("\n--- Select Problems ---")
        for idx, problem in enumerate(available_problems.keys(), 1):
            print(f"{idx}. {problem} ({available_problems[problem]} NIS)")
        print(f"{len(available_problems) + 1}. Done")

        choice = input("Select a problem: ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_problems):
            problem = list(available_problems.keys())[int(choice) - 1]
            selected_problems.append(problem)
        elif choice == str(len(available_problems) + 1):
            break 
        else:
            print("Invalid choice. Please try again.")

    return selected_problems


def main_menu():
    while True:
        print("\n--- Car Garage Menu ---")
        print("1. List all cars")
        print("2. Add a car")
        print("3. Delete a car")
        print("4. Search for a car")
        print("5. Calculate total cars and profit")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_cars()
        elif choice == '2':
            add_a_car()
        elif choice == '3':
            delete_a_car()
        elif choice == '4':
            search_for_car()
        elif choice == '5':
            calculate_total_cars_and_profit()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def list_all_cars():
    print("\n--- List of Cars ---")
    for car in cars:
        print(f"Car Number: {car['Car Number']}, Problems: {', '.join(car['Problems'])}, Price: {car['price']} NIS")

def add_a_car():
    car_number = input("Enter Car Number: ")
    problems = select_problems()
    price = calculate_price(problems)
    print(f"The price of this fix is: {price} NIS.")
    decision = input("Do you wish to proceed? (yes/no): ")
    if decision.lower() == 'yes':
        add_car({'Car Number': car_number, 'Problems': problems, 'price': price})
        print("Car added successfully.")
    else:
        print("Car not added.")

def delete_a_car():
    car_number = input("Enter Car Number to delete: ")
    delete_car(car_number)
    print("Car deleted successfully.")

def search_for_car():
    car_number = input("Enter Car Number to search: ")
    car = search_car(car_number)
    if car:
        print(f"Car found - Car Number: {car['Car Number']}, Problems: {', '.join(car['Problems'])}, Price: {car['price']} NIS")
    else:
        print("Car not found.")

def calculate_total_cars_and_profit():
    print(f"Currently there are {get_total_cars()} cars.")
    print(f"The current profit is: {calculate_total_profit()} NIS.")

def select_problems():
    selected_problems = []
    while True:
        print("\n--- Select Problems ---")
        for idx, problem in enumerate(available_problems.keys(), 1):
            print(f"{idx}. {problem} ({available_problems[problem]} NIS)")
        print(f"{len(available_problems) + 1}. Done")

        choice = input("Select a problem: ")
        if choice.isdigit() and 1 <= int(choice) <= len(available_problems):
            problem = list(available_problems.keys())[int(choice) - 1]
            selected_problems.append(problem)
        elif choice == str(len(available_problems) + 1):
            break
        else:
            print("Invalid choice. Please try again.")

    return selected_problems
