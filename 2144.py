class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        t=0
        for i in range(0,len(cost)):
            if i%3!=2:
                t+=cost[i]
        return t
 