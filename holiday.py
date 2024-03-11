'''
1. Create a function (using keyword def) named hotel_cost and store num_nights in the parameters as the argument
    - Create a variable named price_per_night and store the price charged by the hotel
    - Return total cost by multiplying num_nights by price_per_night

2. Create another funtion named plane_cost with city_flight being the argument
    - Use if/elif/statements where if the user input matchets one of the cities listed a price will be returned
    - use else statement to return 0 if what user has entered does not match list

3. Create another function named car_rental with rental_days being the argument
    - Create a variable named daily_rental_cost and store price per day
    - return total cost by multiplying rental_days and daily_rental_cost

4. Create another function named holiday_cost with the arguments being hotel_cost, plane_cost, and car_rental
    - Create a total cost by adding the three previous functions together
    - Return total cost
5. Get user inputs under the following variables: city_flight, num_nights, rental_days
    - Use upper() function on city_flight input 
    - Turn num_nights and rental_days input into integers

'''
# Dictionary used instead for a more concise code
def plane_cost(city_flight):
    city_prices = {
        "PORT OF SPAIN": 1000,
        "VENICE": 400,
        "TOKYO": 800,
        "MELBOURNE": 550
    }
    return city_prices.get(city_flight, 0) # If the city name is not found in the dictionary, 'get' returns a default value 0 as a precaution

def hotel_cost(num_nights, city_flight):
    city_prices = {
        "PORT OF SPAIN": 85,
        "VENICE": 100,
        "TOKYO": 120,
        "MELBOURNE": 90
    }
    price_per_night = city_prices.get(city_flight.upper(), 0)
    return num_nights * price_per_night

def car_rental(rental_days, city_flight):
    city_prices = {
        "PORT OF SPAIN": 40,
        "VENICE": 50,
        "TOKYO": 60,
        "MELBOURNE": 45
    }
    daily_rental_cost = city_prices.get(city_flight.upper(), 0)
    return rental_days * daily_rental_cost


def holiday_cost(hotel_cost, plane_cost,car_rental):
    total_cost = hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days, city_flight)
    return total_cost

#User input
city_flight = input("Enter the city you will be flying to (Port of Spain, Venice, Tokyo, Melbourne): ").upper()
num_nights = int(input("Enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print("\nHoliday Details:")
print(f"Destination: {city_flight}")
print(f"Number of nights at hotel: {num_nights}")
print(f"Number of days for car rental: {rental_days}")
print(f"Total holiday cost: £{total_cost}")
