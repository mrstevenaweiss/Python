

print("Legend has it that Josephus wouldn't have lived to become famous without his mathematical talents. During the Jewish/Roman war, he was among a band of 41 Jewish rebels trapped in a cave by the Romans. Preferring suicide to capture, the rebels decided to form a circle and, proceeding around it, to kill every third remaining person until no one was left. But Josephus, along with an unindicted co-conspirator, wanted none of this suicide nonsense; so he quickly calculated where he and his friend should stand in the vicious circle. . . . thereby saving his tale for us to hear.")



while True:
    print("-----------------")
    print("Start with n people numbered 1 to n around a circle, and we eliminate every second remaining person until only one survives. 'q' to quit, hit 'Enter' to see \n")
    print('How many people are in the group?')
    p = int(input())
    if p == 'q':
        break
    else:
        if p % 2 == 0:
            even()
        elif p % 2 == 1:
            odd()
        print(p)
        print("\n")
