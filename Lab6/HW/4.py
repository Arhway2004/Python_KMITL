# def calculate_combination(amount):
#     result = {}

#     if amount >= 1000:
#         result[1000] = amount // 1000
#         amount %= 1000
    
#     if amount >= 500:
#         result[500] = amount // 500
#         amount %= 500
    
#     if amount >= 100:
#         result[100] = amount // 100
#         amount %= 100
    
#     if amount >= 50:
#         result[50] = amount // 50
#         amount %= 50
    
#     if amount >= 20:
#         result[20] = amount // 20
#         amount %= 20
    
#     if amount >= 10:
#         result[10] = amount // 10
#         amount %= 10
    
#     if amount >= 5:
#         result[5] = amount // 5
#         amount %= 5
    
#     if amount >= 2:
#         result[2] = amount // 2
#         amount %= 2
    
#     if amount >= 1:
#         result[1] = amount

#     return result

# def main():
#     amount = int(input("Input your amount of money: "))
#     combination = calculate_combination(amount)
    
#     print("Combination:")
#     if 1000 in combination:
#         print(f"1000-Baht notes: {combination[1000]}")
#     if 500 in combination:
#         print(f"500-Baht notes: {combination[500]}")
#     if 100 in combination:
#         print(f"100-Baht notes: {combination[100]}")
#     if 50 in combination:
#         print(f"50-Baht notes: {combination[50]}")
#     if 20 in combination:
#         print(f"20-Baht notes: {combination[20]}")
#     if 10 in combination:
#         print(f"10-Baht coins: {combination[10]}")
#     if 5 in combination:
#         print(f"5-Baht coins: {combination[5]}")
#     if 2 in combination:
#         print(f"2-Baht coins: {combination[2]}")
#     if 1 in combination:
#         print(f"1-Baht coins: {combination[1]}")

# if __name__ == "__main__":
#     main()
def calculate_combination(amount):
    result = {}

    if amount >= 1000:
        result[1000] = amount // 1000
        amount %= 1000
        # return f" ans{result[1000]}"
    
    if amount >= 500:
        result[500] = amount // 500
        amount %= 500
    
    if amount >= 100:
        result[100] = amount // 100
        amount %= 100
        # return f" ans{result[100]}"
    
    if amount >= 50:
        result[50] = amount // 50
        amount %= 50
    
    if amount >= 20:
        result[20] = amount // 20
        amount %= 20
    
    if amount >= 10:
        result[10] = amount // 10
        amount %= 10
    
    if amount >= 5:
        result[5] = amount // 5
        amount %= 5
    
    if amount >= 2:
        result[2] = amount // 2
        amount %= 2
    
    if amount >= 1:
        result[1] = amount

    return result
# print(calculate_combination(amount(result [1000])))
def main():
    amount = int(input("Input your amount of money: "))
    combination = calculate_combination(amount)
    
    print("Combination:")
    if 1000 in combination:
        print(f"1000-Baht notes: {combination[1000]}")
    if 500 in combination:
        print(f"500-Baht notes: {combination[500]}")
    if 100 in combination:
        print(f"100-Baht notes: {combination[100]}")
    if 50 in combination:
        print(f"50-Baht notes: {combination[50]}")
    if 20 in combination:
        print(f"20-Baht notes: {combination[20]}")
    if 10 in combination:
        print(f"10-Baht coins: {combination[10]}")
    if 5 in combination:
        print(f"5-Baht coins: {combination[5]}")
    if 2 in combination:
        print(f"2-Baht coins: {combination[2]}")
    if 1 in combination:
        print(f"1-Baht coins: {combination[1]}")

main()
# def calculate_combination(amount):
#     TO=0
#     FO=0
#     OO=0
#     F=0
#     T=0
#     O=0
#     if amount>=1000:
#         TO+=1
#     elif amout>=500:
#         FO+=1
#     elif amout>=100:
#         FO+=1
#     elif amout>=50:
#         FO+=1
#     elif amout>=20:
#         FO+=1
# def calculate_combination(amount):
#     result = {}

#     if amount >= 1000:
#         result[1000] = amount // 1000
#         amount %= 1000
    
#     if amount >= 500:
#         result[500] = amount // 500
#         amount %= 500
    
#     if amount >= 100:
#         result[100] = amount // 100
#         amount %= 100
    
#     if amount >= 50:
#         result[50] = amount // 50
#         amount %= 50
    
#     if amount >= 20:
#         result[20] = amount // 20
#         amount %= 20
    
#     if amount >= 10:
#         result[10] = amount // 10
#         amount %= 10
    
#     if amount >= 5:
#         result[5] = amount // 5
#         amount %= 5
    
#     if amount >= 2:
#         result[2] = amount // 2
#         amount %= 2
    
#     if amount >= 1:
#         result[1] = amount

#     return result

# amount = int(input("Input your amount of money: "))
# combination_result = calculate_combination(amount)
# print(combination_result)
