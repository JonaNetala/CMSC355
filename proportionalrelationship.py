# -*- coding: utf-8 -*-
# Function to calculate the proportional relationship based on the constant of proportionality
def calculate_proportional_value(x, k):
    proportional_value = k * x
    return proportional_value

# Main function
def main():
    # Problem statement
    print("Lionel loves soccer, but has trouble motivating himself to practice.")
    print("He incentivizes himself through video games.")
    print("There is a proportional relationship between the number of drills Lionel completes (x)")
    print("and the hours he plays video games (y).")
    print("When Lionel completes 10 drills, he plays video games for 0.5 hours.")

    # Get user input
    x = float(input("Enter the number of drills completed by Lionel: "))  # Input for the variable x
    k = 0.05  # Constant of proportionality based on the given problem

    # Calculate the proportional value and get the equation
    proportional_value = calculate_proportional_value(x, k)
    equation = f"y = {k}x"

    # Display the result and the equation
    print(f"When Lionel completes {x} drills, he plays video games for {proportional_value:.2f} hours.")
    print(f"The equation for the relationship is: {equation}")

# Call the main function if the script is run
if __name__ == "__main__":
    main()

