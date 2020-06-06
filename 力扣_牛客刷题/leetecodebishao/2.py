class Solution:
    def minimalSteps(self, maze):
        if len(maze) == 0:
            return -1
        maze = [[i for i in row] for row in maze]
        

s = Solution()
s.minimalSteps(["S#O", "M..", "M.T"])
