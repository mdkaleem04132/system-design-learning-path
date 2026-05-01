import heapq
import time
from enum import Enum


# Elevator direction
class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


# Request object
class Request:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.direction = Direction.UP if destination > source else Direction.DOWN
        self.timestamp = time.time()


class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.direction = Direction.IDLE

        # Separate queues
        self.pickups = []   # (priority, floor)
        self.dropoffs = []  # (priority, floor)

    def add_request(self, request):
        """
        Add pickup first, then drop will be added after pickup is served
        """
        priority = self._calculate_priority(request.source, request.timestamp)
        heapq.heappush(self.pickups, (priority, request))

    def _calculate_priority(self, floor, timestamp):
        """
        Priority based on distance and wait time
        Lower value = higher priority
        """
        wait_time = time.time() - timestamp
        distance = abs(self.current_floor - floor)

        return distance - (wait_time * 2)  # weight wait time

    def step(self):
        """
        Process one step:
        1. Handle pickups
        2. Then handle dropoffs
        """

        # If idle, decide direction
        if self.direction == Direction.IDLE:
            if self.pickups or self.dropoffs:
                self.direction = Direction.UP

        # Priority: pickups first
        if self.pickups:
            _, request = heapq.heappop(self.pickups)
            self._move_to(request.source)

            # After pickup → add drop
            priority = self._calculate_priority(request.destination, request.timestamp)
            heapq.heappush(self.dropoffs, (priority, request.destination))

        elif self.dropoffs:
            _, floor = heapq.heappop(self.dropoffs)
            self._move_to(floor)

        else:
            self.direction = Direction.IDLE

    def _move_to(self, floor):
        print(f"Elevator {self.id}: {self.current_floor} → {floor}")
        self.current_floor = floor


class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators

    def assign_request(self, request):
        """
        Assign request to best elevator using cost function
        """
        best = min(self.elevators, key=lambda e: self._cost(e, request))
        print(f"Assigning {request.source}->{request.destination} to Elevator {best.id}")
        best.add_request(request)

    def _cost(self, elevator, request):
        """
        Cost = distance + direction penalty + load
        """
        distance = abs(elevator.current_floor - request.source)

        direction_penalty = 0
        if elevator.direction != Direction.IDLE and elevator.direction != request.direction:
            direction_penalty = 10

        load = len(elevator.pickups) + len(elevator.dropoffs)
        load_penalty = load * 2

        return distance + direction_penalty + load_penalty

    def step_all(self):
        for e in self.elevators:
            e.step()


# ----------- DRIVER CODE -----------

if __name__ == "__main__":
    e1 = Elevator(1)
    e2 = Elevator(2)

    controller = ElevatorController([e1, e2])

    requests = [
        Request(3, 10),
        Request(5, 1),
        Request(8, 20),
        Request(2, 0)
    ]

    for r in requests:
        controller.assign_request(r)

    for _ in range(10):
        print("\n--- Step ---")
        controller.step_all()