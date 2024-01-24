'''
Task: 
  1. Define a function that will calculate the area of a circle. Choose a name for the function and specify that it should take the radius as a 
  parameter.
  
  2. Inside the function, use the formula for calculating the area of a circle: Area = π * r^2.
  
  3. Implement a mechanism to get user input for the radius. Use the input function to prompt the user to enter the radius of the circle. Ensure 
  that you convert the input to a float to handle decimal values.
  
  4. Call the function you defined in step 3, passing the user-provided radius as an argument.
  
  5. Display the calculated area to the user. Use the print function to show the result. Format the output to show only two decimal places.
'''
import math

# Define a function that calculates the area of the circle, taking radius as a parameter.

def calculate_circle_area(radius):
    area = math.pi * radius ** 2 
    return area

# Get user information
while True: 
    try:
        # Prompt the user to enter the radius as a numerical value
        radius = float(input("Please enter the radius: "))
        break

    except ValueError:
        # Handle the case where the user enters a non-numeric value
        print("Invalid input! Please enter a numerical value.")

# Call the function to calculate the area using the user-provided radius
area = calculate_circle_area(radius) # Calling "area = 3.14159 * radius ** 2 "

# Get user measurement and display the calculated area with 2 decimal places 

while True:
    measurement = input("Which measurement are you using (mm, cm, m, or km): ").lower()
    if measurement == "mm":
        print(f"The area of the circle is: {area:.2f} mm")
        break

    elif measurement == "cm":
        print(f"The area of the circle is: {area:.2f} cm")
        break

    elif measurement == "m":
        print(f"The area of the circle is: {area:.2f} m")
        break 

    elif measurement == "km":
        print(f"The area of the circle is: {area:.2f} km")
        break 

    else: 
        print("Invalid measurement. Please try again")
