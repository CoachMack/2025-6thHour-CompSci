#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hello_world():
    print("Hello World!")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads, tails
    for i in range(10000):
        coin = random.randint(1,2)
        if coin == 1:
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
coin_flip()
#5. Print the final result of heads and tails here
print("Heads:", heads)
print("Tails:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["green", "black", "brown", "cerulean", "vermillion", "blue", "maroon", "red", "yellow"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean_pull():
    if beanBag == []:
        print("No more beans in the bag!")
    else:
        hand = random.choice(beanBag)
        print(hand)
        beanBag.remove(hand)
        repeat_bean()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat_bean():
    user_repeat = input("Do you want to pull another bean? Y/N").lower()

    if user_repeat == "y":
        bean_pull()
    elif user_repeat == "n":
        print("Okay!")
    else:
        print("Invalid input. Please try again.")
        repeat_bean()
#9. Call the "Bean Pull" function here
bean_pull()