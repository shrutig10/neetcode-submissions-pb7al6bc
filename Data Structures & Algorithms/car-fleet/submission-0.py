class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # put car speed and positions together
        # sort by closest to target (positions)
        # calculate time to finish
        # put time to finish in stack
        # if time is shorter than top of stack --> add to fleet
        # if greater than top of stack --> add to stack

        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        timeToFinish = []

        for car in cars:
            timeToFinish.append(float((target - car[0])) / float(car[1]))

        fleets = []
        for time in timeToFinish:
            if not fleets or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)