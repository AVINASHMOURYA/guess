import random
if __name__ == '__main__':
    try:
        value1 = int(input("Enter the bounds"))
        value2 = int(input())
        if value2 == None or value1 == None:
            print("Baka ga omai? Enter the text first.")
        else:
            i = 1
            answer = random.randint(value1, value2)
            while(i < 6):
                value = int(input("Enter the Guess."))
                if value == None:
                    print("Enter the fuc*king value")
                elif value < answer:
                    print("answer is greater.")
                elif value > answer:
                    print("answer is smaller.")
                elif value == answer:
                    print("Write answer,you won!!")
                    break
                i += 1
    except ValueError:
        print("OPPS! That was no valid number, Try again...")
