# author: Aaron Stichter
# created: 2025-04-30
# game selector tool for gamers
# NO CODING ASSISTANCE was used in this program


# pseudocode
# output welcome messages
# collect responses from user
# find associated game based on responses
# find associated info for selected game
# output recommended game and game info
# ask to run program again
# closing messages


def welcome_messages():
    """outputs some opening remarks"""
    print(f'SDEV 140 - Game Selector - Final Project by:(ATS)')
    print(f'Welcome to my Game Selector Tool')
    print(" ")


def games_library(key):
    """Defines a dictionary of games"""
    library = {(1,1,1): "Candy Crush",
               (1,1,2): "Minecraft",
               (1,1,3): "Animal Crossing: Pocket Camp",
               (1,2,1): "Fortnite",
               (1,2,2): "Tetris Effect",
               (1,2,3): "Animal Crossing: New Horizons",
               (1,3,1): "Castle of Illusion",
               (1,3,2): "It Takes Two",
               (1,3,3): "Forza Horizon 5",
               (2,1,1): "Clash Royale",
               (2,1,2): "Balatro",
               (2,1,3): "Baldur's Gate: Dark Alliance",
               (2,2,1): "Ori and the Blind Forest",
               (2,2,2): "The Elder Scrolls: Skyrim Special Edition",
               (2,2,3): "The Legend of Zelda: Breath of the Wild",
               (2,3,1): "Enter the Gungeon",
               (2,3,2): "The Witcher 3: Wild Hunt",
               (2,3,3): "Diablo IV",
               (3,1,1): "Chrono Trigger",
               (3,1,2): "Final Fantasy Tactics",
               (3,1,3): "Dead Cells",
               (3,2,1): "Cuphead",
               (3,2,2): "Death Stranding: Director's Cut",
               (3,2,3): "Monster Hunter: Wilds",
               (3,3,1): "Counter-Strike 2",
               (3,3,2): "Slay the Spire",
               (3,3,3): "Baldur's Gate 3"}
    return library[key]


def games_info():
    """shows price, difficulty, platform, and Metacritic rating for each associated game"""
    Games = {"Candy Crush": ["Free-to-Play", "Easy", "Mobile", "79"],
             "Minecraft": ["6.99", "Easy", "Mobile", "93"],
             "Animal Crossing: Pocket Camp": ["19.99", "Easy", "Mobile", "69"],
             "Fortnite": ["Free-to-Play", "Easy", "Console", "78"],
             "Tetris Effect": ["39.99", "Easy", "Console", "89"],
             "Animal Crossing: New Horizons": ["59.99", "Easy", "Console", "90"],
             "Castle of Illusion": ["14.99", "Easy", "PC", "67"],
             "It Takes Two": ["39.99", "Easy", "PC", "88"],
             "Forza Horizon 5": ["59.99", "Easy", "PC", "92"],
             "Clash Royale": ["Free-to-Play", "Intermediate", "Mobile", "85"],
             "Balatro": ["9.99", "Intermediate", "Mobile", "90"],
             "Baldur's Gate: Dark Alliance": ["12.99", "Intermediate", "Mobile", "87"],
             "Ori and the Blind Forest": ["19.99", "Intermediate", "Console", "88"],
             "The Elder Scrolls: Skyrim Special Edition": ["39.99", "Intermediate", "Console", "96"],
             "The Legend of Zelda: Breath of the Wild": ["59.99", "Intermediate", "Console", "97"],
             "Enter the Gungeon": ["14.99", "Intermediate", "PC", "82"],
             "The Witcher 3: Wild Hunt": ["39.99", "Intermediate", "PC", "92"],
             "Diablo IV": ["49.99", "Intermediate", "PC", "86"],
             "Chrono Trigger": ["4.99", "Expert", "Mobile", "92"],
             "Final Fantasy Tactics": ["6.99", "Expert", "Mobile", "88"],
             "Dead Cells": ["8.99", "Expert", "Mobile", "89"],
             "Cuphead": ["19.99", "Expert", "Console", "86"],
             "Death Stranding: Director's Cut": ["39.99", "Expert", "Console", "85"],
             "Monster Hunter: Wilds": ["69.99", "Expert", "Console", "88"],
             "Counter-Strike 2": ["Free-to-Play", "Expert", "PC", "82"],
             "Slay the Spire": ["24.99", "Expert", "PC", "89"],
             "Baldur's Gate 3": ["59.99", "Expert", "PC", "96"]}
    return Games


def questionnaire():
    """asks a series of questions and adds responses to list"""
    # declarations
    answers = []

    # first question
    question1 = input(f'What level of experience do you have with gaming (Beginner - 1, Intermediate - 2, Expert - 3)?: ')

    # validate input
    while True:
        try:
            question1 = int(question1)
            if 0 < question1 < 4:
                break
            else:
                question1 = input(f'Invalid number. Please enter the number next to your level of experience (Beginner - 1, Intermediate - 2, Expert - 3): ')
        except ValueError:
            question1 = input(f'Invalid input. Please enter the number next to your level of experience (Beginner - 1, Intermediate - 2, Expert - 3): ')

    # add question1 to list answers
    answers.append(question1)

    # second question
    question2 = input(f'What platform will you be using to game (Mobile - 1, Console - 2, PC - 3)?: ')

    # validate input
    while True:
        try:
            question2 = int(question2)
            if 0 < question2 < 4:
                break
            else:
                question2 = input(f'Invalid number. Please enter the number next to the platform you will be gaming on (Mobile - 1, Console - 2, PC - 3): ')
        except ValueError:
            question2 = input(f'Invalid input. Please enter the number next to the platform you will be gaming on (Mobile - 1, Console - 2, PC - 3): ')

    # add question2 to list answers
    answers.append(question2)

    # third question
    question3 = input(f'What is your budget for a new game (Low - 1, Medium - 2, High - 3)?: ')

    # validate input
    while True:
        try:
            question3 = int(question3)
            if 0 < question3 < 4:
                break
            else:
                question3 = input(f'Invalid number. Please enter the number next to your level of budget (Low - 1, Medium - 2, High - 3): ')
        except ValueError:
            question3 = input(f'Invalid input. Please enter the number next to your level of budget (Low - 1, Medium - 2, High - 3): ')

    # add question3 to list answers
    answers.append(question3)

    return answers


def list_to_tuple(list):
    """turns list of answers into a tuple"""
    list = tuple(list)

    return list


def fetch_info(answers):
    """finds and returns info from game_info()"""
    # declarations
    game = games_library(list_to_tuple(answers))
    info = games_info()

    # find game info from game_info() dictionary
    price = info[game][0]
    difficulty = info[game][1]
    platform = info[game][2]
    rating = info[game][3]

    return game, price, difficulty, platform, rating


def print_game_selection(info):
    """Prints info about selected game"""
    # output info
    print(" ")
    print(f'The game I recommend for you is: {info[0]}')
    print(f'Price: {info[1]}')
    print(f'Difficulty: {info[2]}')
    print(f'Platform: {info[3]}')
    print(f'Metacritic score: {info[4]}')


def repeat_program():
    """user decides if they want to run the program again"""

    print(" ")
    repeat = input(f'Would you like to choose another game (y or n)?: ')

    return repeat


def closing_messages(answers):
    """outputs some closing remarks"""
    # declarations
    game = games_library(list_to_tuple(answers))

    # game is last recommended game
    print(" ")
    print(f"I hope you enjoy playing {game}! It's a good one! ")


def main():
    """main program loop"""
    # print opening remarks just once
    welcome_messages()

    # loops until user enters sentinel
    while True:
        answers = list_to_tuple(questionnaire())
        print_game_selection(fetch_info(answers))
        repeat = repeat_program()

        if repeat != "y":
            closing_messages(answers)
            break

main()
