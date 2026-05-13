class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, i))
            else:
                top = stack[-1]
                while top[0] < temp:
                    top = stack.pop()
                    prev_idx = top[1]
                    res[prev_idx] = i-prev_idx
                    if not stack:
                        break
                    top = stack[-1]
                stack.append((temp, i))
        return res
