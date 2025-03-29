import random

class AutonomousVehicle:
    def __init__(self, vehicle_id, speed):
        self.id = vehicle_id
        self.speed = speed

    def negotiate(self, other_vehicle):
        if self.speed > other_vehicle.speed:
            return self.id
        elif self.speed < other_vehicle.speed:
            return other_vehicle.id
        else:
            return random.choice([self.id, other_vehicle.id])

def simulate_traffic_intersection(vehicle1, vehicle2):
    negotiation_result = vehicle1.negotiate(vehicle2)

    print(f"Negotiation Result: Vehicle {negotiation_result} has the right of way.")

# Example Usage
vehicleA = AutonomousVehicle("CarA", 60)
vehicleB = AutonomousVehicle("CarB", 50)

simulate_traffic_intersection(vehicleA, vehicleB)
