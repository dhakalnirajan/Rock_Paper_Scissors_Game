from random import randint

# taking case insensitive choices
choice = ['rock', 'paper', 'scissors']
ch = 'y'
rounds = 0

# function to take player choice
def player_choice():
    choice_of_player = input("\n Please input complete word. \n Enter your choice Rock / Paper / Scissors:")

# Player can even input other characters for checking to ensure that the code is not broken.
    if choice_of_player.lower() and choice_of_player.lower() in ('rock', 'paper', 'scissors'):
        return choice_of_player.lower()
    else:
        print("\n You made wrong choice! Retry!")
        choice_of_player()

# Function with parameter to get result on every choice
def get_result(choice_of_player):
    comp_choice = choice[randint(0,2)]
    print("\n Computer Chose:", comp_choice,"\n")

    # The Rule of Game
    if choice_of_player == comp_choice:
        result = 'tie'
        print('{} is same as {}! No score change!'.format(choice_of_player.upper(), comp_choice.upper()))
    elif comp_choice == 'scissors' and choice_of_player == 'rock':
        result = 'win'
        print('ROCK crushes SCISSORS! You win! Score +1')
    elif comp_choice == 'paper' and choice_of_player == 'scissors': 
        result = 'win'
        print('SCISSORS cut PAPER! You win! Score +1')
    elif comp_choice == 'rock' and choice_of_player == 'paper': 
        result = 'win'
        print('PAPER covers ROCK! You win! Score +1')

   #If the above 'Win' Conditions are not matched, display 'you lost' message and take one points from the score
    else: 
        result = 'lose'
        print('You lose! Score -1')
    return result

#function to update the scores
def update_score(result):
    global wins, loss, tie
    if result == 'win':
        wins += 1
    elif result == 'lose':
        loss += 1
    else:
        tie += 1

#to take the number of rounds from user
def game_rounds(r = 0):
    r = input("\n Enter the number of rounds in natural number or combination of natural numbers: ")

    #Ensuring that the user-defined number of rounds is a natural number or a combination of natural numbers
    try:
        global rounds
        rounds = int(r)
    except:
        print("\n Wrong Input! Enter a natural number or combination of natural numbers!")
        game_rounds()

#function to run the game till user defined rounds
def game(rounds):
    total_score = 0
    global round_result
    for i in range(0,rounds):
        print("\n Ready for Round", i+1)
        pc = choice_of_player()
        res = get_result(pc)
        round_result.append(res)
        update_score(res)
        total_score = wins - loss  # Ignoring ties as the result doesn't depend on ties
        print("\n After round",(i+1),"your score is: ",total_score)

    #at the end of all rounds we return total score
    return total_score

# Main Module
def main():
    global ch, round_result
    print("\n Welcome to Rock, Paper, Scissors Game.\n Rules are simple")
    print('''\n Winning Rules are as follows:
    Rock vs Paper ----> Paper wins Rock Losses
    Rock vs Scissors ----> Rock wins Scissors Losses
    Paper vs Scissors ----> Scissors wins Paper Losses \n
    For each win you get 1 point 
    For each loss you lose 1 point
    And if tied, you neither gain or lose points. \n''')


    game_rounds()
    ts = game(rounds)

    #displaying results after all  rounds
    print("\n After",rounds,"rounds, your final score is: ",ts)
    print("\n You have {} wins, {} Losses and {} Ties!".format(wins,Loss,Ties))
    print("\n Round wise result is",round_result)
    ch = input("\n Do you want to continue? Enter y for yes. To exit, enter any other key: ")

while(ch == 'y' or ch == 'Y'):
    wins = 0
    loss = 0
    tie = 0

    round_result = []
    rounds
    main()
print("\n See you Again!!")
