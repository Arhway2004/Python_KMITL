# max=[100,80,70,60,50]
# min=[80,70,60,50]
# X=[90,75,65,55,45]
# def grade(X):
#     if min[x]<=X<=max[x]:
#         return "A"
#     elif min[x]<=X<max[x]:
#         return "B"
#     elif min[x]<=X<max[x]:
#         return "C"
#     elif min[x]<=X<max[x]:
#         return "D"
#     elif max[x]<X:
#         return "F"

# for x in range(5):
#     X1 = X[x]  # Get the current score
#     grade_result = grade(X1)
#     print(f"A student will get {grade_result}if {min}<= his/her mark <={max}")
max_scores = [100, 80, 70, 60, 50]
min_scores = [80, 70, 60, 50, 0]
scores = [90, 75, 65, 55, 45]

def grade(score):
    if max_scores[x] >= score >= min_scores[x]:
        return "A"
    elif max_scores[x] > score >= min_scores[x]:
        return "B"
    elif max_scores[x] > score >= min_scores[x]:
        return "C"
    elif max_scores[x] > score >= min_scores[x]:
        return "D"
    elif score > max_scores[x]:
        return "F"

for x in range(5):
    X = scores[x]
    grade_result = grade(X) 
    print(f"A student will get {grade_result} if {min_scores[x]} <= his/her mark <= {max_scores[x]}")

