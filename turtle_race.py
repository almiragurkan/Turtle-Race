import random
import time

names = ['A', 'B', 'C']

def printscreen(tracklength, turtles_position):
    for i in range(tracklength):
        print("{:02d}".format(i + 1), end=" ")
    print()
    for i in range(tracklength):
        print("--", end=" ")
    print()
    for t in range(len(turtles_position)):
        for i in range(tracklength):
            if i == turtles_position[t]:
                print(names[t], end="  ")
            else:
                print("--", end=" ")
        print()


def random_move():
    rand = random.randint(0, 100)
    if rand <= 10:  # 10% Two steps back
        return -2
    elif rand <= 30:  # 20% One step back
        return -1
    elif rand <= 50:  # 20% No move
        return 0
    elif rand <= 90:  # 40% One step forward
        return 1
    else:  # 10% Two steps forward
        return 2


def main():
    turtles_position = [0, 0, 0]
    sleepseconds = 0.5
    tracksize = int(input("Please enter the length of the race track: "))
    printscreen(tracksize, turtles_position)
    ended = False
    time.sleep(sleepseconds)
    while not ended:
        print()
        for i in range(len(turtles_position)):
            nextmove = turtles_position[i] + random_move()
            if nextmove < 0:
                nextmove = 0
            elif nextmove >= tracksize:
                nextmove = tracksize - 1
            turtles_position[i] = nextmove
            if nextmove == tracksize - 1:
                ended = True
        printscreen(tracksize, turtles_position)
        if not ended:
            time.sleep(sleepseconds)
    winners = []
    for i in range(len(turtles_position)):
        if turtles_position[i] == tracksize - 1:
            winners.append(names[i])
    if len(winners) == 1:
        print("****** " + winners[0] + " won!!! ****** ")
    else:
        print("TIE BETWEEN " + " and ".join(winners))


main()