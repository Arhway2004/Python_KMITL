print("Please enter a time in 24 hour format")
Hours=int(input("Hours:"))
H=Hours
Minutes=int(input("Minutes:"))
Seconds=int(input("Seconds:"))
if Hours >=12:
    period ="PM"
    Hours-=12
else:
    priod = "AM"
    if Hours == 0:
        Hours =0
print(f"The time you just entered in {H:02d} hour format is{Hours:02d}:{Minutes:02d}:{Seconds:02d}")


