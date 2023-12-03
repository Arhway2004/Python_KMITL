# from abc import ABC, abstractmethod

# class Transportation(ABC):
#     def __init__(self):
#         self.start = ""
#         self.end = ""

#     @abstractmethod
#     def find_cost(self):
#         pass

# class Walk(Transportation):
#     def __init__(self, dist):
#         super().__init__()
#         self.dist = dist
#         self.station = "-"
#     def find_cost(self):
#         return 0

# class Taxi(Transportation):
#     def __init__(self, dist):
#         super().__init__()
#         self.dist = dist
#         self.station = "-"
#     def find_cost(self):
#         return self.dist*40
    
# class Train(Transportation):
#     def __init__(self, station):
#         super().__init__()
#         self.station = station
#     def find_cost(self):
#         return self.station*5
    
# walk = Walk(0.6)
# taxi1 = Taxi(5)
# train = Train(40)
# taxi2 = Taxi(3)

# print(f"Start: KMITL,End:Lawson at KMITL{str(walk.find_cost())}(walk)")
# print(f"Start: Lawson at KMITL,End:Ladkrabang Station{str(taxi1.find_cost())}(taxi1)")
# print(f"Start: Ladkrabang Station,End:Payathai Station{str(train.find_cost())}(train)")
# print(f"Start: Payathai Station,End:The British Conncil{str(taxi2.find_cost())}(taxi2)")

class Transportation:
    def __init__(self):
        self.start = ""
        self.end = ""

    def find_cost(self):
        # raise NotImplementedError("Subclasses must implement find_cost method")
        pass

class Walk(Transportation):
    def __init__(self, dist):
        super().__init__()
        self.dist = dist
        self.station = "-"

    def find_cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, dist):
        super().__init__()
        self.dist = dist
        self.station = "-"

    def find_cost(self):
        return self.dist * 40

class Train(Transportation):
    def __init__(self, station):
        super().__init__()
        self.station = station

    def find_cost(self):
        return self.station * 5

walk = Walk(0.6)e
taxi1 = Taxi(5)
train = Train(40)
taxi2 = Taxi(3)

print(f"Start: KMITL, End: Lawson at KMITL, Cost: {str(walk.find_cost())} (walk)")
print(f"Start: Lawson at KMITL, End: Ladkrabang Station, Cost: {str(taxi1.find_cost())} (taxi1)")
print(f"Start: Ladkrabang Station, End: Payathai Station, Cost: {str(train.find_cost())} (train)")
print(f"Start: Payathai Station, End: The British Council, Cost: {str(taxi2.find_cost())} (taxi2)")
