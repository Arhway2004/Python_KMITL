# class Time:
#     def __str__(HH,MM,SS):
#         return(f"{HH}:{MM}:{SS} Hrs.")
# time1 = Time(9,30,0)
# time1.print()
class Time:
    def __init__(self, HH, MM, SS):
        self.HH = HH
        self.MM = MM
        self.SS = SS
    
    def __str__(self):
        return f"{self.HH:02}:{self.MM:02}:{self.SS:02} Hrs."
    
    def print(self):
        print(self)

time1 = Time(9, 30, 00)

time1.print()
