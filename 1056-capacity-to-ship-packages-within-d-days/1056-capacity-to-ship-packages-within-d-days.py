class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)

        while low < high:
            mid=(low+high)//2
            if self.canShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low

    def canShip(self,weights,days,capacity):
        currentWeight=0
        requiredDays=1
        for weight in weights:
            if currentWeight+weight > capacity:
                requiredDays+=1
                currentWeight=0
            currentWeight+=weight
        
        return requiredDays<=days

        