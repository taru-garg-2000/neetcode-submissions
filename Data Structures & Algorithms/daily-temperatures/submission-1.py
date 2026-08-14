class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        result = []

        for i in range(len(temperatures)-1, -1, -1):
            while len(temps) > 0 and temps[-1][0] <= temperatures[i]:
                temps.pop()

            if len(temps) == 0:
                result.append(0)
            else:
                result.append(temps[-1][1] - i)
            
            temps.append([temperatures[i], i])

        return result[::-1]