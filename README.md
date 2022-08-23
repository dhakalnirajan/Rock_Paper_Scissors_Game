# Rock Paper Scissors Game


This game is a computerized version of the
Classic **Rock 🥌, Paper 🧻, Scissors ✂️**.

In the classic game, **Two Players stand off against each other.** After they chant ** "Scissor, Paper, Rock, Shoot!"**, their hand is then subjected to the **three of the orientation that decides which players wins and which player loses.**
The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward; and scissors is a fist with the index and middle fingers fully extended toward the opposing player.

In This game, I created a computerized Rock, Paper, Scissors game in easy level.

The step-by-step Algorithm is below:

1. Step-1: Initializing all the score and rounds to zero.     Create a list to store round results.
2. Step-2: Take a number of rounds as input; rounds = input.
3. Step-3: Run the steps 4, 5 and 6 'round' times:
4. Step-4: Ask the user choice, choice_of_player = input() and generate a computer choice, comp_choice = random().
5. Step-5: Check who wins based on the game rules and the entered choice.
6. Step-6: Update the score as: If Win, then Win += 1. If Loss then loss += 1. Else tie = 1
7. Step-7: At the end of rounds, display:
        i. Total score i.e. Wins - loss
        ii. Total Wins, Losses and ties
        iii. Roundwise result list.
End

                R U L E S    O F    T H E    G A M E
          Players start each round by entering the choice. The computer program makes choice randomly without looking at the user's choice. Then, a hidden layer of algorithm processes the two choices and sends the output to the result. The basic rule-of-thumb of the game is: Rock crushes scissors, scissors cut paper, and paper covers rock.
