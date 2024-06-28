

cars = []

def add_car(car):
    cars.append(car)

def delete_car(car_number):
    global cars
    cars = [car for car in cars if car['Car Number'] != car_number]

def search_car(car_number):
    for car in cars:
        if car['Car Number'] == car_number:
            return car
    return None
