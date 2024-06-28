

import cars


available_problems = {
    'Engine': 2000,
    'Breaks': 1000,
    '5000 km treatment': 500,
    '10000 km treatment': 1000,
    'Filters + Oil': 250,
    'Gear': 1000
}

def calculate_price(problems):
    return sum(available_problems[problem] for problem in problems)

def calculate_total_profit():
    return sum(car['price'] for car in cars)

def get_total_cars():
    return len(cars)
