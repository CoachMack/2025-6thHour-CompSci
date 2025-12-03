#Name: Coach Mack
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.


#Ask user for number of players
num_of_players = int(input("Enter number of players: "))
rating_total = []

while num_of_players < 6:
    print("Error: Need at least 6 players.")
    num_of_players = int(input("Enter number of players: "))
#Ask each player to rate the model from 1 to 5
for i in range(1, num_of_players + 1):
    player_rating = int(input("Enter rating from 1 to 5: "))
    while player_rating < 1 or player_rating > 5:
        print("Error: Rating not between 1 and 5")
        player_rating = int(input("Enter rating from 1 to 5: "))
    else:
        rating_total.append(player_rating)

#Calculate the average based on total score divided by the number of players
print(rating_total)
print(f"Rating Average: {sum(rating_total)/num_of_players}")
