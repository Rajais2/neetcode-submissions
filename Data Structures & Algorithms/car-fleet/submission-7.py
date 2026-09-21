class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's position with its speed
        cars = list(zip(position, speed))

        # Sort cars by position descending
        cars.sort(reverse = True)

        # Stack to store fleet arrival times
        stack = []

        # Process cars from closest to target to farthest
        for pos, speed in cars:
            time = (target - pos) / speed

            # New fleet if this car takes longer than the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
