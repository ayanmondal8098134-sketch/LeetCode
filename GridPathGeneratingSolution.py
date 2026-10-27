class Solution(object):
    def createGrid(self, m, n):
        grid= []
        grid.append("." * n)

        for i in range(m-1):
            grid.append("#" * (n-1)+ ".")

        return grid
        
        