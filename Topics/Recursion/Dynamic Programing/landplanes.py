arr =[155, 55, 2, 96, 67, 203, 3]
class AirCraftSpacing:
    def __init__(self, passengers):
        self.passengers = passengers
        
    def max_passengers(self, i):
        if i >= len(self.passengers):
            return 0
        choosing_first = self.passengers[i] + self.max_passengers(i+2)
        choosing_last = self.max_passengers(i+1)
        return max(choosing_first, choosing_last)

spacing = AirCraftSpacing(arr)
print(spacing.max_passengers(0))





