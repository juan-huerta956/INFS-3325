#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat July  22 01:52:44 2023

@author: juanhuerta
"""

# Step 2 - List of lists of women's basketball scores
# Manually input the scores for the games starting from Feb 4, 2023, to the end of the season

# Create a list of lists containing the scores
scores = [
    [55, 84],  # UTRGV vs Opponent, Game 1
    [42, 76],  # UTRGV vs Opponent, Game 2
    [75, 71],  # Game 3
    [66, 73],  # Game 4
    [86, 89],  # Game 5
    [66, 58],  # Game 6
    [65, 61],  # Game 7
    [69, 59],  # Game 8
    [76, 81],  # Game 9
    [49, 65]   # Game 10
]

# Print the list of lists
print("Step 2 - List of lists of women's basketball scores:")
for game_num, game_score in enumerate(scores, start=1):
    utrgv_score, opponent_score = game_score
    print(f"Game {game_num}: UTRGV {utrgv_score}, Opponent {opponent_score}")
    
print("\nStep 3 - Game Selector:")
def get_game_score(game_num):
    if 1 <= game_num <= 10:
        utrgv_score, opponent_score = scores[game_num - 1]
        return utrgv_score, opponent_score
    else:
        return None, None

while True:
    try:
        game_number = int(input("Enter a game number (1-10): "))
        if 1 <= game_number <= 10:
            utrgv_score, opponent_score = get_game_score(game_number)
            if utrgv_score is not None:
                print(f"You requested game #{game_number}")
                print(f"The score in game #{game_number} was UTRGV {utrgv_score}, Opponent {opponent_score}")
            else:
                print("Invalid game number requested")
            break  # Exit the loop if a valid input is provided
        else:
            print("Invalid input. Please enter a valid game number (1-10).")
    except ValueError:
        print("Invalid input. Please enter a valid game number (1-10).")

# Step 4 - Count of wins
def count_wins(utrgv_scores, opponent_scores):
    utrgv_wins = 0
    for utrgv_score, opponent_score in zip(utrgv_scores, opponent_scores):
        if utrgv_score > opponent_score:
            utrgv_wins += 1
    return utrgv_wins

# Extract UTRGV and opponent scores from the list of lists
utrgv_scores, opponent_scores = zip(*scores)

utrgv_wins_count = count_wins(utrgv_scores, opponent_scores)
print("\nStep 4 - Count of wins:")
print(f"UTRGV won {utrgv_wins_count} out of 10 games")

# Step 5 - Descriptive Statistics
import pandas as pd

# Create a DataFrame with custom column names
df = pd.DataFrame(scores, columns=['UTRGV', 'Opponent'])

def descriptive_statistics():
    highest_utrgv_score = df['UTRGV'].max()
    lowest_utrgv_score = df['UTRGV'].min()
    avg_utrgv_score = df['UTRGV'].mean()
    avg_opponent_score = df['Opponent'].mean()
    return highest_utrgv_score, lowest_utrgv_score, avg_utrgv_score, avg_opponent_score

# Call the function and report results
highest_utrgv, lowest_utrgv, avg_utrgv, avg_opponent = descriptive_statistics()
print("\nStep 5 - Descriptive Statistics:")
print(f"Highest UTRGV score: {highest_utrgv}")
print(f"Lowest UTRGV score: {lowest_utrgv}")
print(f"Average UTRGV score: {avg_utrgv:.2f}")
print(f"Average Opponent score: {avg_opponent:.2f}")