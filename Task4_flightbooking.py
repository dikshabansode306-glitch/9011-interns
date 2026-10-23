from abc import ABC, abstractmethod

# ==============================================================================
# 1. ABSTRACTION & INHERITANCE: Passenger Classes
# ==============================================================================
class Passenger(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @abstractmethod
    def get_discount_percentage(self) -> float:
        pass

    @abstractmethod
    def get_passenger_type(self) -> str:
        pass


class RegularPassenger(Passenger):
    def get_discount_percentage(self) -> float:
        return 0.0

    def get_passenger_type(self) -> str:
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount_percentage(self) -> float:
        return 0.10

    def get_passenger_type(self) -> str:
        return "Student"


# ==============================================================================
# 2. ENCAPSULATION: Flight Class
# ==============================================================================
class Flight:
    def __init__(self, flight_code: str, airline: str, source: str, destination: str, available_seats: int, base_fare: float):
        self._flight_code = flight_code
        self._airline = airline
        self._source = source
        self._destination = destination
        self._available_seats = available_seats
        self._base_fare = base_fare

    @property
    def flight_code(self) -> str:
        return self._flight_code

    @property
    def airline(self) -> str:
        return self._airline

    @property
    def source(self) -> str:
        return self._source

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def available_seats(self) -> int:
        return self._available_seats

    @property
    def base_fare(self) -> float:
        return self._base_fare

    def allocate_seats(self, count: int) -> bool:
        if count <= self._available_seats:
            self._available_seats -= count
            return True
        return False


# ==============================================================================
# 3. CLASS & OBJECT: Booking Class
# ==============================================================================
class Booking:
    _id_counter = 1001

    def __init__(self, flight: Flight, passenger: Passenger, ticket_count: int):
        self._booking_id = f"BK{Booking._id_counter}"
        Booking._id_counter += 1
        
        self._flight = flight
        self._passenger = passenger
        self._ticket_count = ticket_count
        
        self._subtotal = self._flight.base_fare * self._ticket_count
        self._discount = self._subtotal * self._passenger.get_discount_percentage()
        self._final_amount = self._subtotal - self._discount

    def display_summary(self):
        print("\n" + "="*40)
        print("         BOOKING CONFIRMED!         ")
        print("="*40)
        print(f"Booking ID         : {self._booking_id}")
        print(f"Flight             : {self._flight.flight_code} | {self._flight.source} to {self._flight.destination}")
        print(f"Passenger Name     : {self._passenger.name}")
        print(f"Passenger Type     : {self._passenger.get_passenger_type()}")
        print(f"Tickets Booked     : {self._ticket_count}")
        print(f"Base Fare per ticket: {self._flight.base_fare}")
        print(f"Subtotal           : {self._subtotal}")
        print(f"Student discount (10%): {self._discount}" if self._passenger.get_passenger_type() == "Student" else f"Regular discount (0%): {self._discount}")
        print(f"Final amount       : {self._final_amount}")
        print("="*40)


# ==============================================================================
# 4. SYSTEM CONTROLLER: FlightBookingSystem Class
# ==============================================================================
class FlightBookingSystem:
    def __init__(self):
        self._flights = {}
        self._bookings = []
        self._initialize_predefined_flights()

    def _initialize_predefined_flights(self):
        f1 = Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000.0)
        f2 = Flight("MB202", "IndiGo", "Mumbai", "Bengaluru", 15, 3500.0)
        f3 = Flight("PH303", "Air India", "Pune", "Hyderabad", 5, 2500.0)
        
        self._flights[f1.flight_code] = f1
        self._flights[f2.flight_code] = f2
        self._flights[f3.flight_code] = f3

    def view_flights(self):
        print("\n" + "-"*65)
        print(f"{'Code':<8}{'Airline':<15}{'Source':<12}{'Destination':<15}{'Seats':<8}{'Fare':<8}")
        print("-"*65)
        for flight in self._flights.values():
            print(f"{flight.flight_code:<8}{flight.airline:<15}{flight.source:<12}{flight.destination:<15}{flight.available_seats:<8}{flight.base_fare:<8.0f}")
        print("-"*65)

    def find_flight(self, code: str) -> Flight:
        return self._flights.get(code.upper().strip())

    def book_flight(self):
        choice_2 = input("Enter choice: ")
        if choice_2 != "2":
            return
            
        flight_code = input("Enter flight code: ").strip()
        flight = self.find_flight(flight_code)
        
        if not flight:
            print("Booking failed: Invalid Flight Code.")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Booking failed: Passenger name cannot be blank.")
            return

        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Booking failed: Age must be greater than 0.")
                return
        except ValueError:
            print("Booking failed: Age must be a number.")
            return

        pass_type = input("Passenger type (Regular/Student): ").strip().capitalize()
        if pass_type == "Student":
            passenger = StudentPassenger(name, age)
        elif pass_type == "Regular":
            passenger = RegularPassenger(name, age)
        else:
            print("Booking failed: Invalid passenger category.")
            return

        try:
            tickets = int(input("Enter number of tickets: "))
            if tickets <= 0:
                print("Booking failed: Ticket count must be greater than 0.")
                return
        except ValueError:
            print("Booking failed: Ticket count must be an integer.")
            return

        if tickets > flight.available_seats:
            print("Booking failed: Not enough seats available.")
            print("No booking was created. Available seats remain unchanged.")
            return

        if flight.allocate_seats(tickets):
            new_booking = Booking(flight, passenger, tickets)
            self._bookings.append(new_booking)
            print("\nBooking confirmed!")
        else:
            print("Booking failed: Internal error.")

    def view_latest_booking(self):
        choice_3 = input("Enter choice: ")
        if choice_3 != "3":
            return
        if not self._bookings:
            print("No booking exists.")
            return
        self._bookings[-1].display_summary()

    def run(self):
        # Initial Welcome Message
        print("Welcome to Kiran Air Booking")
        print("1. View Flights")
        print("2. Book Flight")
        print("3. View Booking")
        print("4. Exit")
        
        while True:
            choice = input("Enter choice: ").strip()
            
            if choice == "1":
                self.view_flights()
            elif choice == choice:
                if choice == "2":
                    # Prints options again immediately to match assignment flow layout
                    print("Welcome to Kiran Air Booking")
                    print("1. View Flights")
                    print("2. Book Flight")
                    print("3. View Booking")
                    print("4. Exit")
                    self.book_flight()
                elif choice == "3":
                    self.view_latest_booking()
                elif choice == "4":
                    print("Thank you for using Kiran Air Booking!")
                    break
                else:
                    print("Invalid choice.")


# ==============================================================================
# THIS MAKES IT RUN: Entry point execution block
# ==============================================================================
if __name__ == "__main__":
    system_engine = FlightBookingSystem()
    system_engine.run()



