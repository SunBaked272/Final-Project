# author: Aaron Stichter
# created: 2025-05-08
# Game Recommendation Tool
# SOME CODING ASSISTANCE was used in this program
# see line 121

# pseudocode
# initiate home page
# display header, intro message, start and exit buttons
# switch frame to Question1, display question and 3 answer buttons
# collect response in list userAnswers
# switch frame to Question2, display question and 3 answer buttons
# collect response in list userAnswers
# switch frame to Question3, display question and 3 answer buttons
# collect response in list userAnswers
# switch frame to Recommendation Page, display recommendation, game info, restart and exit buttons
# end


# imports
import tkinter as tk

# declarations
userAnswers = [] # list of responses from user, passed to games_library to find recommended game


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


def add_answers(list, answer):
    """adds user answer to list"""
    list.append(answer)

    # print(list) # debug
    return list


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


# CodeAssist-internet: class for switching frames from https://stackoverflow.com/a/49325719
class GameRecommendation(tk.Tk):
    """initializes frame"""
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)
        self.wm_title("Game Recommendation Tool by:(ATS)")

    def switch_frame(self, frame_class):
        """switches to passed frame"""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class HomePage(tk.Frame):
    """displays home page with header, and two buttons (start, exit)"""
    def __init__(self, master):

        # initialize frame
        tk.Frame.__init__(self, master, bg="sky blue")
        tk.Frame.pack_propagate(self, False)
        tk.Frame.configure(self, width=500, height=300)

        # initialize title label
        titleLabel = tk.Label(self.master,
                              text="Game Recommendation Tool by:(ATS)",
                              font=("PT Sans Caption", 20, "underline"),
                              bg="dark blue",
                              fg="sky blue")
        titleLabel.pack(fill="x")

        # initialize welcome message
        introLabel = tk.Label(self.master,
                              text="Want to play a new game? "
                                   "\nNot sure which one to pick?"
                                   "\nLet me help!",
                              font=("PT Sans Caption", 20),
                              bg="dark blue",
                              fg="sky blue")
        introLabel.pack(fill="x")

        #initialize start button: destroys labels and buttons, switches to Question1 frame
        startButton = tk.Button(self.master,
                                text="Start",
                                font=("PT Sans Caption", 15),
                                fg="dark blue",
                                background="sky blue",
                                command=lambda:[master.switch_frame(Question1),
                                                titleLabel.destroy(),
                                                introLabel.destroy(),
                                                startButton.destroy(),
                                                exitButton.destroy()])
        startButton.place(x=215, y=175)

        # initialize exit button: kills program
        exitButton = tk.Button(self.master,
                               text="Exit",
                               font=("PT Sans Caption", 15),
                               fg="dark blue",
                               background="sky blue",
                               command=lambda:self.master.destroy())
        exitButton.place(x=217, y=250)


class Question1(tk.Frame):
    """frame for first question"""
    def __init__(self, master):

        # initialize frame
        tk.Frame.__init__(self, master, bg="sky blue")
        tk.Frame.pack_propagate(self, False)
        tk.Frame.configure(self, width=500, height=400)

        # initialize question 1 label
        question1Label = tk.Label(self.master,
                              text="Question 1: "
                                   "\nHow experienced are you with gaming?",
                              font=("PT Sans Caption", 20, "underline"),
                              bg="dark blue",
                              fg="sky blue")
        question1Label.pack(fill="x")

        # initialize answer buttons
        answer1 = tk.Button(self.master, # answer 1
                            text="Beginner",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 1), # adds response to list userAnswers
                                            master.switch_frame(Question2), # switches frame to next question
                                            answer1.destroy(), # destroys button
                                            answer2.destroy(), # destroys button
                                            answer3.destroy(), # destroys button
                                            question1Label.destroy()]) # destroys label
        answer1.place(x=10, y=230)

        answer2 = tk.Button(self.master, # answer 2
                            text="Intermediate",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 2), # adds response to list userAnswers
                                            master.switch_frame(Question2), # switches frame to next question
                                            answer1.destroy(), # destroys button
                                            answer2.destroy(), # destroys button
                                            answer3.destroy(), # destroys button
                                            question1Label.destroy()]) # destroys label
        answer2.place(x=190, y=230)

        answer3 = tk.Button(self.master, # answer 3
                            text="Expert",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 3), # adds response to list userAnswers
                                            master.switch_frame(Question2), # switches frame to next question
                                            answer1.destroy(), # destroys button
                                            answer2.destroy(), # destroys button
                                            answer3.destroy(), # destroys button
                                            question1Label.destroy()]) # destroys label
        answer3.place(x=400, y=230)


class Question2(tk.Frame):
    """frame for second question"""
    def __init__(self, master):

        # initialize frame
        tk.Frame.__init__(self, master, bg="sky blue")
        tk.Frame.pack_propagate(self, False)
        tk.Frame.configure(self, width=500, height=400)

        # initialize question 2 label
        question2Label = tk.Label(self.master,
                              text="Question 2: "
                                   "\nWhat platform will you be gaming on?",
                              font=("PT Sans Caption", 20, "underline"),
                              bg="dark blue",
                              fg="sky blue")
        question2Label.pack(fill="x")

        # initialize answer buttons
        answer1 = tk.Button(self.master, # answer 1
                            text="Mobile",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 1),
                                            master.switch_frame(Question3),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question2Label.destroy()])
        answer1.place(x=10, y=230)

        answer2 = tk.Button(self.master, # answer 2
                            text="Console",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 2),
                                            master.switch_frame(Question3),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question2Label.destroy()])
        answer2.place(x=210, y=230)

        answer3 = tk.Button(self.master, # answer 3
                            text="PC",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 3),
                                            master.switch_frame(Question3),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question2Label.destroy()])
        answer3.place(x=410, y=230)


class Question3(tk.Frame):
    """frame for third question"""
    def __init__(self, master):

        # initialize frame
        tk.Frame.__init__(self, master, bg="sky blue")
        tk.Frame.pack_propagate(self, False)
        tk.Frame.configure(self, width=500, height=400)

        # initialize question 3 label
        question3Label = tk.Label(self.master,
                              text="Question 3: "
                                   "\nHow big is your budget?",
                              font=("PT Sans Caption", 20, "underline"),
                              bg="dark blue",
                              fg="sky blue")
        question3Label.pack(fill="x")

        # initialize answer buttons
        answer1 = tk.Button(self.master, # answer 1
                            text="Low",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 1),
                                            list_to_tuple(userAnswers), # changes list userAnswers to tuple for searching in dictionary
                                            master.switch_frame(Recommendation),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question3Label.destroy()])
        answer1.place(x=10, y=230)

        answer2 = tk.Button(self.master, # answer 2
                            text="Medium",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 2),
                                            list_to_tuple(userAnswers), # changes list userAnswers to tuple for searching in dictionary
                                            master.switch_frame(Recommendation),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question3Label.destroy()])
        answer2.place(x=202, y=230)

        answer3 = tk.Button(self.master, # answer 3
                            text="High",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[add_answers(userAnswers, 3),
                                            list_to_tuple(userAnswers), # changes list userAnswers to tuple for searching in dictionary
                                            master.switch_frame(Recommendation),
                                            answer1.destroy(),
                                            answer2.destroy(),
                                            answer3.destroy(),
                                            question3Label.destroy()])
        answer3.place(x=400, y=230)


class Recommendation(tk.Frame):
    """frame shows the recommended game"""
    def __init__(self, master):

        # initialize frame
        tk.Frame.__init__(self, master, bg="sky blue")
        tk.Frame.pack_propagate(self)


        # initialize header label
        headerLabel = tk.Label(self.master,
                               text="Recommendation: \n" + fetch_info(userAnswers)[0],
                               font=("PT Sans Caption", 20, "underline"),
                               bg="dark blue",
                               fg="sky blue")
        headerLabel.pack(fill="x")

        # initialize info label
        infoLabel = tk.Label(self.master,
                             text="Price: $" + fetch_info(userAnswers)[1] + "\n"
                                  "Difficulty: " + fetch_info(userAnswers)[2] + "\n"
                                  "Platform: " + fetch_info(userAnswers)[3] + "\n"
                                  "Metacritic Rating: " + fetch_info(userAnswers)[4],
                             font=("PT Sans Caption", 20),
                             bg="sky blue",
                             fg="dark blue")
        infoLabel.pack(fill="x")

        # create restart button: starts at Question 1
        restartButton = tk.Button(self.master, # answer 3
                            text="Restart?",
                            font=("PT Sans Caption", 15),
                            fg="dark blue",
                            bg="sky blue",
                            command=lambda:[userAnswers.clear(),
                                            headerLabel.destroy(),
                                            infoLabel.destroy(),
                                            restartButton.destroy(),
                                            exitButton.destroy(),
                                            master.switch_frame(Question1)])
        restartButton.pack(side="left", fill='x')

        # create exit button: kills program
        exitButton = tk.Button(self.master,
                               text="Exit",
                               font=("PT Sans Caption", 15),
                               fg="dark blue",
                               background="sky blue",
                               command=lambda:self.master.destroy())
        exitButton.pack(side="right", fill='x')





if __name__ == "__main__":
    run = GameRecommendation()
    run.mainloop()