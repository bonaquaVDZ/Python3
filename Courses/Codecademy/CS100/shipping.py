import sys
import time


# Function is not called.
def calculate_shipping_cost():
    # Get the weight of the package from the user
    while True:
        try:
            weight = float(input("Enter the weight of your possible package in kg: "))
            if weight > 0:
                break
            else:
                print("Weight must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def loading_animation(message="Loading"):
        """Prints an animated dot sequence for the specified number of seconds.

        Args:
            message (str): The message to display before the animation (default 'Loading').
        """
        animation = "|/-\\"
        idx = 0
        start_time = time.time()  # get the start time
        try:
            while time.time() - start_time < 5:  # run for 5 seconds
                print("\r" + message + " " + animation[idx % len(animation)], end="")
                sys.stdout.flush()
                idx += 1
                time.sleep(0.1)
            print("\r" + message + " Done!    ")
        except KeyboardInterrupt:
            # Handle keyboard interrupt (e.g. Ctrl+C)
            print("\nAnimation interrupted by user.")

    # Calculate cost of ground shipping
    if weight <= 2:
        cost_ground = weight * 1.50 + 20
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
    else:
        cost_ground = weight * 4.75 + 20

    # Convert kg to lb
    lbs = weight / 0.45359237

    # Request is loading
    print("Calculating shipping costs...")
    loading_animation()

    # Print the cost of ground shipping in kg and lb
    print(
        f"\nCost of ground shipping for {weight} kg ({lbs:.2f} lb) package: ${cost_ground:.2f}"
    )

    # Calculate the cost of premium ground shipping in kg and lb
    cost_ground_premium = 125
    print(
        f"Cost of premium ground shipping for {weight} kg ({lbs:.2f} lb) package: ${cost_ground_premium:.2f}"
    )

    # Calculate cost of drone shipping
    if weight <= 2:
        cost_drone = weight * 4.50
    elif weight <= 6:
        cost_drone = weight * 9.00
    elif weight <= 10:
        cost_drone = weight * 12.00
    else:
        cost_drone = weight * 14.25

    # Print the cost of drone shipping in kg and lb
    print(f"Cost of drone shipping for {weight} kg ({lbs:.2f} lb) package: ${cost_drone:.2f}")


# Run this part of code in another program
# import shipping
# shipping.calculate_shipping_cost()
