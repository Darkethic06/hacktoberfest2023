from time import *
import random as r


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try: 
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,user_i):
    time_dif = time_e - time_s
    time_R = round(time_dif,2)
    speed = len(user_i) / time_R
    return round(speed)


while True:
    ck = input("Are you ready for the test?(y/n): ")
    print()
    print()
    if ck == "y":
        test = [
        "The quick brown fox jumps over the lazy dog.",
            "Sphinx of black quartz, judge my vow.",
            "How vexingly quick daft zebras jump!",
            "Pack my box with five dozen liquor jugs.",
            "The five boxing wizards jump quickly."
        ]
        test1 = r.choice(test)
        print("         ***Welcome to Typing Speed Test***      ")
        print()
        print()
        print(test1)
        print()
        print()
        time1 = time()
        testInput = input("Start Typing:  ")
        time2 = time()
        print()
        print()
        print("    Speed: ",speed_time(time1,time2,testInput),"w/sec")
        print("    Error: ",mistake(test1,testInput))
    elif ck == "n":
        print("Thank You") 
        break 
    else:
        print("Sorry!Wrong Input")
