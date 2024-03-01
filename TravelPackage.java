import java.util.ArrayList;
import java.util.List;

class TravelPackage {
    private String name;
    private int passengerCapacity;
    private List<Destination> destinations;
    private List<Passenger> passengers;

    public TravelPackage(String name, int passengerCapacity) {
        this.name = name;
        this.passengerCapacity = passengerCapacity;
        this.destinations = new ArrayList<>();
        this.passengers = new ArrayList<>();
    }

    public void printItinerary() {
        // Implementation
    }

    public void printPassengerList() {
        // Implementation
    }

    public void printPassengerDetails(int passengerNumber) {
        // Implementation
    }

    public void printAvailableActivities() {
        // Implementation
    }
}

class Destination {
    private String name;
    private List<Activity> activities;

    public Destination(String name) {
        this.name = name;
        this.activities = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Activity> getActivities() {
        return activities;
    }

    public void addActivity(Activity activity) {
        // Implementation
    }
}

class Activity {
    private String name;
    private String description;
    private double cost;
    private int capacity;
    private Destination destination;
    private List<Passenger> enrolledPassengers;

    public Activity(String name, String description, double cost, int capacity, Destination destination) {
        this.name = name;
        this.description = description;
        this.cost = cost;
        this.capacity = capacity;
        this.destination = destination;
        this.enrolledPassengers = new ArrayList<>();
    }

    public boolean isFull() {
        // Implementation
        return false;
    }
}

class Passenger {
    private String name;
    private int passengerNumber;
    private String passengerType;
    private double balance;
    private List<Activity> activitiesSignedUp;

    public Passenger(String name, int passengerNumber, String passengerType, double balance) {
        this.name = name;
        this.passengerNumber = passengerNumber;
        this.passengerType = passengerType;
        this.balance = balance;
        this.activitiesSignedUp = new ArrayList<>();
    }

    public void signUpForActivity(Activity activity) {
        // Implementation
    }
}
