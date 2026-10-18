import random

def start_chatbot():
    # Predefined Data: Cab types and rates per km
    cab_rates = {
        "1": {"name": "Auto", "rate": 12},
        "2": {"name": "Sedan", "rate": 18},
        "3": {"name": "SUV", "rate": 25}
    }
    
    # Predefined Data: Routes and distances
    routes = {
        "1": {"source": "Pune Station", "dest": "Shivajinagar", "dist": 5},
        "2": {"source": "Swargate", "dest": "Kothrud", "dist": 8},
        "3": {"source": "Hinjawadi", "dest": "Wakad", "dist": 10}
    }

    print("--- Welcome to the Cab Booking Chatbot ---")

    while True:
        # Step 1: Main Menu
        print("\n===== MAIN MENU =====")
        print("1. Book Ride")
        print("2. Exit")
        main_choice = input("Enter your choice (1 or 2): ").strip()

        if main_choice == "2":
            print("\nThank you for using our Cab Booking Chatbot. Goodbye!")
            break  # Stop the loop and exit program cleanly
        
        elif main_choice == "1":
            # Step 2: Choose Cab Type
            print("\n--- Available Cab Types ---")
            print("1. Auto  (Rs. 12/km)")
            print("2. Sedan (Rs. 18/km)")
            print("3. SUV   (Rs. 25/km)")
            cab_choice = input("Select a cab type (1-3): ").strip()
            
            if cab_choice not in cab_rates:
                print("Invalid cab choice! Returning to Main Menu.")
                continue

            # Step 3: Choose Route
            print("\n--- Available Routes ---")
            print("1. Pune Station to Shivajinagar (5 km)")
            print("2. Swargate to Kothrud (8 km)")
            print("3. Hinjawadi to Wakad (10 km)")
            route_choice = input("Select a route number (1-3): ").strip()
            
            if route_choice not in routes:
                print("Invalid route choice! Returning to Main Menu.")
                continue

            # Step 4: Calculate Fare
            selected_cab = cab_rates[cab_choice]
            selected_route = routes[route_choice]
            
            distance = selected_route["dist"]
            rate = selected_cab["rate"]
            fare = distance * rate

            print("\n--- Ride Calculation Summary ---")
            print(f"Cab Type   : {selected_cab['name']}")
            print(f"Route      : {selected_route['source']} to {selected_route['dest']}")
            print(f"Distance   : {distance} km")
            print(f"Rate       : Rs. {rate}/km")
            print(f"Total Fare : Rs. {fare}")
            print("--------------------------------")

            # Step 5: Cancellation before OTP
            print("\nWould you like to finalize your booking?")
            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")
            confirm_choice = input("Enter option (1 or 2): ").strip()

            if confirm_choice == "2":
                print("\n[Notification] Ride cancelled successfully. Returning to main menu.")
                continue
            elif confirm_choice == "1":
                # Step 6: OTP and ride lock
                otp = random.randint(1000, 9999)
                print("\n==========================================")
                print(f"Your 4-digit booking OTP is: {otp}")
                print("CRITICAL RULE: The OTP has been shared. This ride is now locked and CANNOT be cancelled!")
                print("Your booking is officially confirmed.")
                print("==========================================")
            else:
                print("Invalid selection. Booking discarded. Returning to main menu.")
                continue

        else:
            print("Invalid input! Please enter 1 to book a ride or 2 to exit.")

if __name__ == "__main__":
    start_chatbot()
