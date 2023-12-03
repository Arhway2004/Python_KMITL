while True: 
        wordss = ord(input(">: "))
        if wordss == 0x2E:
            print("break")
            break;
        elif 0x30 <= wordss and wordss <= 0x39:
            print ("It's a numeric charater")
        elif 0x41 <= wordss and wordss <= 0x5A:
            print ("It's a Capital Letter")


# words = input(">:")
# print(ASCLL(words))