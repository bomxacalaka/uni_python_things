# Coding Challenge 4 Individual Programming Project
# Name: Jorge Eduardo Dal Santo Caetano
# Student No: 2038025
import random

from time import sleep

def intro():
    print("This is Le Dungem, a game made for those lore hungry")

nice = "cordial,ducky,fair,friendly,good,kind,lovely,okay,superior,swell,welcome,winning,admirable,amiable,approved,attractive,becoming,charming,commendable,considerate,copacetic,courteous,decorous,delightful,favorable,fine and dandy,genial,gentle,gracious,helpful,ingratiating,inviting,kindly,nifty,obliging,peachy,pleasant,pleasurable,polite,prepossessing,seemly,simpatico,unpresumptuous,well-mannered,winsome"



def narr():
    print("Imagine you are an engineer who randomly felt like exploring an exotic part of the Rain Forest")

def defeatus():
    s = "G A M E   O V E R"
    for i in s:
        if i.isalpha():
            print(i,end="")
            sleep(.3)
        else:
            print(i,end="")
    exit(666)

def grats(nice):
    k=nice.upper().split(',')
    s =  f"{k[random.randint(0,len(k))]} VICTORY"
    for i in s:
        print(i, end="")
        sleep(.1)
    exit(69)
#grats(nice)



def kek(d):
    while True:
        answer = input("You: ")
        for i in d:
            if i == answer:
                return answer
        for i in d:
            for o in i:
                for p in answer:
                    if o == p:
                        print("There is a %s on one of the correct answer(s)"%o)

def dif(s):
    if s == "easy":
        a,b,c = 7,13,26
    elif s == "medium":
        a, b, c = 42, 64, 69
    elif s == "hard":
        a, b, c = 128, 420, 666
    return a,b,c

def vibe_check():
    he = input("easy  -  medium  -  hard\n ")
    score = 0
    a1,b1,c1 = dif(he)
    print("After walking for hours you step on something hard on the floor near a river, you could ignore as you are tired after the long walk")
    d = a,b,c = ('floor', 'river', 'ignore')
    answer = kek(d)


    if answer == b:
        print("As you walk to the river you see some ingenious wooden constructions\n they seem to harvest the energy of the flowing river\n but you stop for a second almost as if\n you were going to think about something")
        score+=c1

        d = a, b, c = ("construction","river","think")
        answer = kek(d)

        if answer == a:
            score+=b1
            print("After a quick check you realise its some red and really old wood\n You are surprised at how it is still operational and running\n so you think there might be something under the hard floor")
        elif answer==b:
            score+=c1
            print("After a refreshing and long shower in the crystaline but algaesh water\n you suddently fill something touching your feet and without thinking\n jump right out of the water and realise it was just a fish\n but since you are out and refreshed you continue your exploring")
        elif answer ==c:
            score+=a1
            print("Perhaps this has something I stepped on before,\n I might after all not be alone here\n and if thats the case then I better be prepared")

    elif answer == c:
        print("You keep walking and and find a massive temple\n which might be filled with mysteries\n but you decide that it's job for someone else\n and you would be more suitable as the camera man\n so you ignore and go back home to live a boring life\n where you will ignore your wife\n and then your kids\n and then when you die\n everyone will ignore you")
        defeatus()
        score = "loser"

    elif answer == a:
        score+=b1
        print("Huh!?")

    print("As you see that hard dirt you step on it harder to see what it is\n and you are meet with resistance from the floor and almost breaks your feet\n after brushing some dust off the floor with your hands\n you realise there is some clay but not just clay\n its harden clay, the one you need an oven to produce")

    d = a, b, c = ("oven", "clay", "feet")
    answer = kek(d)

    if answer == a:
        score+=a1
        print("You walk around at the search for some sort of charcoal remains\n but instead you are welcomed with a shiny sun\n on some wide open space and at 50 meters away you see\n a huge box made of the same harden clay from the floor\n but covered by vines and nature like stuff")
    if answer == b:
        score+=b1
        print("You cautiously analise the clay and see some black patches\n but it isnt clear if those dark patches are charcoal or just limestone")
    if answer == c:
        print("Now that your little baby feet are scratched you call it a day\n and go back to your ordinary lonely life\n where you spend the rest of your life making programs\n for Tesla cars to mine 69 ElonCoins")
        defeatus()
    if c1+b1<=score:
        saveScore(input("What is your name son"),score)
        return True
    else:
        defeatus()

def menu():
    print("Would you like to 'play'?\nOr perhaps you wanna peek into the 'leaderboard'?")
    print("Tip: type a word you read on the question above")
    return input(" ")



def saveScore(name,score):
    input_file = open('scores.txt', 'r')
    temp = open('temp.txt', 'w')

    empty_str = ''
    line = input_file.readline()
    while line != empty_str:
        temp.write(line)
        line = input_file.readline()
    temp.close()

    temp = open('temp.txt', 'r')
    output = open('scores.txt', 'w')
    empty_str = ''
    line = temp.readline()
    if line == empty_str:
        output.write(f"{name}_{score}")
    else:
        o = True
        while line != empty_str:
            k = line.split('_')
            if k[0] == name:
                o = False
            output.write(f"{k[0]}_{k[1]}")
            line = temp.readline()
        if o:
            output.write(f"\n{name}_{score}")
        output.close()



def showScore():
    input_file = open('scores.txt', 'r')
    empty_str = ''
    l=[]
    line = input_file.readline()
    while line != empty_str:
        k = line.split('_')
        kk = k[1].replace('\n','')
        l+=k[0],kk
        line = input_file.readline()

    for i in range(0, len(l), 2):
        print('%s - %d' % (l[i], int(l[i + 1])))




def main():
    intro()
    while input("PRESS ENTER") == '':
        answer=menu()
        if answer == "play":
            if vibe_check():
                grats(nice)
        elif answer == "leaderboard":
            showScore()



# Driver function for the program
if __name__ == "__main__":
    main()