class Activity:
    def __init__(self, name, description, cost, capacity, destination):
        self.name = name
        self.description = description
        self.cost = cost
        self.capacity = capacity
        self.destination = destination
        self.enrolled_passengers = []

    def is_full(self):
        return len(self.enrolled_passengers) >= self.capacity

class Destination:
    def __init__(self, name):
        self.name = name
        self.activities = []

class Passenger:
    def __init__(self, name, passenger_number, passenger_type, balance=0):
        self.name = name
        self.passenger_number = passenger_number
        self.passenger_type = passenger_type
        self.balance = balance
        self.activities_signed_up = []

    def sign_up_for_activity(self, activity):
        if activity.is_full():
            print("Sorry, the activity is full.")
            return

        if self.passenger_type == "standard":
            if self.balance < activity.cost:
                print("Insufficient balance to sign up for the activity.")
                return
            self.balance -= activity.cost
        elif self.passenger_type == "gold":
            discounted_cost = 0.9 * activity.cost
            if self.balance < discounted_cost:
                print("Insufficient balance to sign up for the activity.")
                return
            self.balance -= discounted_cost
        # Premium passengers can sign up for activities for free.

        activity.enrolled_passengers.append(self)
        self.activities_signed_up.append(activity)

class TravelPackage:
    def __init__(self, name, passenger_capacity):
        self.name = name
        self.passenger_capacity = passenger_capacity
        self.destinations = []

    def print_itinerary(self):
        print(f"Travel Package: {self.name}")
        for destination in self.destinations:
            print(f"\nDestination: {destination.name}")
            for activity in destination.activities:
                print(f"  - Activity: {activity.name}")
                print(f"    Description: {activity.description}")
                print(f"    Cost: {activity.cost}")
                print(f"    Capacity: {activity.capacity}")

    def print_passenger_list(self):
        print(f"Passenger List for {self.name}")
        print(f"Capacity: {self.passenger_capacity}")
        print(f"Enrolled Passengers: {len(self.get_enrolled_passengers())}")
        for passenger in self.get_enrolled_passengers():
            print(f"  - Name: {passenger.name}, Number: {passenger.passenger_number}")

    def get_enrolled_passengers(self):
        enrolled_passengers = []
        for destination in self.destinations:
            for activity in destination.activities:
                enrolled_passengers.extend(activity.enrolled_passengers)
        return list(set(enrolled_passengers))

    def print_passenger_details(self, passenger):
        print(f"Passenger Details: {passenger.name}")
        print(f"Number: {passenger.passenger_number}")
        if passenger.passenger_type == "standard" or passenger.passenger_type == "gold":
            print(f"Balance: {passenger.balance}")
        print("Activities Signed Up:")
        for activity in passenger.activities_signed_up:
            print(f"  - Activity: {activity.name}")
            print(f"    Destination: {activity.destination.name}")
            print(f"    Price Paid: {activity.cost}")

    def print_available_activities(self):
        print("Available Activities:")
        for destination in self.destinations:
            for activity in destination.activities:
                if not activity.is_full():
                    spaces_available = activity.capacity - len(activity.enrolled_passengers)
                    print(f"  - Activity: {activity.name}")
                    print(f"    Destination: {activity.destination.name}")
                    print(f"    Spaces Available: {spaces_available}")


# Example Usage:

# Create Destinations
destination1 = Destination("Destination 1")
destination2 = Destination("Destination 2")

# Create Activities for Destinations
activity1 = Activity("Activity 1", "Description 1", 50, 10, destination1)
activity2 = Activity("Activity 2", "Description 2", 100, 5, destination2)

destination1.activities.append(activity1)
destination2.activities.append(activity2)

# Create Travel Package
travel_package = TravelPackage("Package 1", 20)
travel_package.destinations.extend([destination1, destination2])

# Create Passengers
passenger1 = Passenger("John", 1, "standard", 200)
passenger2 = Passenger("Alice", 2, "gold", 300)
passenger3 = Passenger("Bob", 3, "premium")

# Sign up passengers for activities
passenger1.sign_up_for_activity(activity1)
passenger2.sign_up_for_activity(activity2)
passenger3.sign_up_for_activity(activity1)

# Print Itinerary
travel_package.print_itinerary()

# Print Passenger List
travel_package.print_passenger_list()

# Print Passenger Details
travel_package.print_passenger_details(passenger1)

# Print Available Activities
travel_package.print_available_activities()
