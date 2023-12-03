# def bank(money):
#     result={}
#     if money >=1000:
#         result[1000]=money%1000
#         money%=1000
#     if money >=100:
#         result[100]=money%100
#         money%=100
#     if money >=1:
#         result[1]=money%1
#         money%=1
#     return result

# def main()
while True:
    withdrawal_amount = int(input("How much you want to withdraw: "))
    
    if withdrawal_amount % 100 != 0:
        print("Withdrawal amount must be a multiple of 100 Baht.")
        break
    else:
        if withdrawal_amount >= 1000:
            x = withdrawal_amount // 1000
            print(f"You get {x} note(s) of 1000 Bahts")
            withdrawal_amount %= 1000
        if withdrawal_amount >= 500:
            y = withdrawal_amount // 500
            print(f"{y} note(s) of 500 Bahts")
            withdrawal_amount %= 500
        if withdrawal_amount >= 100:
            z = withdrawal_amount // 100
            print(f"{z} note(s) of 100 Bahts")
            withdrawal_amount %= 100
        
        if withdrawal_amount == 0:
            break
