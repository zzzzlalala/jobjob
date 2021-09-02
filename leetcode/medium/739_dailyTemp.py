class solution:
    def dailyTemp(self, temperatures):
        length = len(temperatures)
        res = [0] * length
        stack = []
        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res


if __name__ == '__main__':
    solution = solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemp(temperatures))
