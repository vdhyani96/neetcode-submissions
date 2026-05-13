class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # This problem uses monotonic stack to store "leaders" of car fleet
        # First sort by position to simplify relative movement
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, speed in cars:
            dist = target - pos
            time = dist/speed

            if not stack or time > stack[-1]:
                stack.append(time)
            # if the next car in position takes longer to arrive
            # than the car ahead, it gets counted as "leader" of the next fleet

        return len(stack)
