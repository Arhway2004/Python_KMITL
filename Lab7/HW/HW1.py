# class Time:
#     def __init__(self,H,M,S,P):
#         self.H=H
#         self.M=M
#         self.S=S
#         self.P=P
#     def period(self,H):
#         if H>=12:
#             self.P=PM
#         elif H<=12 or H==24:
#             self.P=AM
#     def second(self,period):
#         self.S+=1
#         if self.H >=12:
#             H-=12
#             self.period="PM"
#         else:
#             if self.H==24:
#                 H=00
#                 self.period="AM"

#         # if self.S >= 60:
#         #     self.S = 0
#         #     self.M += 1
#         #     if self.M >= 60:
#         #         self.M = 0
#         #         self.H += 1
#         #         if self.H >= 24:
#         #             self.H = 0

#     def __str__(self):
#         return f"{self.H},{self.M}.{self.S}.{period}"
#     def print(self):
#         print(self)

# Time = Time(13,43,32)
# # print('Time')
# Time.second()
# print(Time)

class Time:
    def __init__(self, H, M, S):
        self.H = H
        self.M = M
        self.S = S
        self.P = ""

    def period(self):
        if self.H >= 12:
            self.P = "PM"
        else:
            self.P = "AM"

    def tick(self):
        self.S += 1
        if self.S >= 60:
            self.S = 0
            self.M += 1
            if self.M >= 60:
                self.M = 0
                self.H += 1
                if self.H >= 24:
                    self.H = 0
        self.period() 

    def __str__(self):
        return f"{self.H}:{self.M}:{self.S} {self.P}"

    def print(self):
        print(self)

time = Time(10, 43, 32)
time.tick()
print(time)

