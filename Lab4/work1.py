score = int(input("input score in range 0 to 100")) 
if 80 <= score <=100:
    print("Grade A")
elif 70 <= score <80:
    print("Grade B")
elif 60 <= score <70:
    print("Grade C")
elif 50 <= score<60:
    print("Grade D")
elif score<50:
    print("GradeF")
else :
    print("Error")
