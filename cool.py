log_in = input("Would you like to log in? ")
user_names = ["John", "Jim", "jimin", "Jungkook", "jin", "J-hope", "Jihyo", "Jayani", "Jingo", "Jeremy", "Jema"]
if log_in.strip().lower() == "yes":
    print("Logging In")
    user_input = input("What is your name?")
elif log_in.strip().lower() == "yep":
    print("Logging In")
    user_input = input("What is your name?")
elif log_in.strip().lower() == "ye":
    print("Logging In")
    user_input = input("What is your name?")
elif log_in == "no":
    print("Joining without logging in. Top secret huh?")
    print("Codename user_Sunray.")
    user_input = "user_Sunray"
else:
    print("Please enter a valid input.")
user_names.append(user_input)
#score variable
score = 0
#List/tuple for riddles :)
riddles = [("You buy me to eat, but you never eat me. What am I?","A fork."),
           ("The more you take the more you leave behind.","Footsteps."),
           ("What kind of tree do you carry in your hand?","Palm."),
           ("What has four legs but can't walk?","A table."),
           ("How many months have 28 days?","All of them."),
           ("What is full of holes but can still hold water?","A sponge."),
           ("Why are teddy bears never hungry?","Because they are stuffed"),
           ("I’m tall when I’m young, and short when I’m old. What am I?", "A candle."),
           ("What gets wet as it dries?","A towel."),
           ("What has to be broken before you can use it?","An egg."),
           (" I have branches, but no fruit, trunk, or leaves. What am I?","A bank."),
           ("What can you hold in your left hand but not in your right?","Your right elbow."),
           ("What has a head but no brain?","Lettuce."),
           ("The more of this there is, the less you see. What is it?","Darkness."),
           ("What has many keys but can't open a single lock?","A piano."),
           ("What has one eye but cannot see?","A needle."),
           ("What goes up but never comes back down?"," Your age."),
           ("What has a neck but no head?","A bottle."),
           ("What belongs to you, but everyone else uses it more than you do?","Your name."),
           ("I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?","Breath."),
           ("What has hands but can’t clap?","A clock."),
           ("Cool Kid, What is my name?", "Jodie Starling."),
           ("I say Megane wa doko? Who is my friend?", "Megan.E")
           ]
print(f"GERALD THE WIZARD: Welcome young hero {user_input}, to our mansion, to find your celebrity solve the riddles.")
print("But before that you will pair up to solve quests ")

import random
user_names.append(user_input)
random.shuffle(user_names)
# Shuffle names by switching order around
pairs = [(user_names[i], user_names[i+1])for i in range(0, len(user_names) -1, 2)]
if len(user_names) %2 != 0:
    pairs.reverse()
    print(f"The pairs are: {pairs}")
    print(f"Extra person :{user_names[-1]}")
else:
    print(f"The pairs are: {pairs}")
print("To reach the celebrity (Jungkook) you must get more than 10 riddles right! BEgin")
print("Yes, Yes Jungkook is participating online to save himself.")
##Add if elif else before final riddle
#I also made a list for final riddle for some reason
final_riddle = [("I have a body of names and keys to a door,I grow shorter as I explain myself more.I am broken the moment my secret is told,A bottle of truth that no hand can hold.I am darkness for some, yet a light for the wise,I’m a bank for the mind with no fruit in my eyes.You can catch me in breath, but I’m gone in a blink,I’m the harder you look, the less that you think.","A Riddle.")]
#Random function was in the loop so it keeps repeating 14 times so im keeping it outside
random.shuffle(riddles)
for i in range(22):
    Q,answer = riddles[i]
    print(Q)
    user_answer = input("Your answer:")
    if user_answer == answer:
        print("Correct!")
        score+=1
    else:
        print("Incorrect! Be careful now")
print("Riddle solving score is",score,"/",22)
# Score analysis system
if score < 8:
    print("Failure")
elif score < 16:
    print("better luck next time")
elif score >= 19:
    print("Amazing! You have reached the final stage now battle the witch!")
    print("")
#For some reason this doesn't work
if score >= 19:
    Q1,answer1 = final_riddle[0]
    print(Q1)
    user_answer1 = input("Your answer: ")
    if user_answer1 == answer1:
        print("Correct!You have now completed your quest. Congratulations!")
        print("Cookie is in the fridge.")
    else:
        print("Incorrect! Bad luck you couldn't save the celebrity")
