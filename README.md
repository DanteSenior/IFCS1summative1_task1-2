# Quiz game documentation

## Introduction
This game displays a window to the user for interactivity, and generates 10 questions, based on the difficulty level selected easy, medium, or hard allowing the user to customize the game to their skill level. The game then displays the questions to the user one at a time, the user then attempts to answer the question, the program will then display if the answer is correct or incorrect before moving on to the next question. Once all 10 questions have been answered, the final score is displayed, along with a message that varies based on the final score. 

## User guide

### Features 
This quiz outputs questions of 3 different difficulty levels.
Gives feedback if the answer is correct or incorrect while completing the quiz.
Displays a window for ease of use.
Displays total score and a message at the end of the game.


### What you’ll need to play
Python, a popular, and free programming language is needed to run the program. To install the latest version visit the following website https://www.python.org/downloads/ or search “Python install” on a web browser. Follow the installation instructions on the website provided.

### Starting the program

### How to play
Selecting difficulty 
Once open please select a difficulty level by clicking on the circle or the word corresponding to the desired difficulty level. if none is selected, easy will be used by default. 

### Starting the quiz
Press the “Start quiz” button to begin. A question will now be displayed.

### Entering questions 
The user can enter answers by typing into the box, which is selected by default, and then by pressing the “Enter” key on the keyboard, or by pressing the “Submit” button on screen.

### Viewing the score
A running total of correct and incorrect answers is displayed during the quiz. Once an answer to a question has been submitted, the program will display “Correct” or “Incorrect”, before moving onto the next question. At the end of the quiz the final score is displayed, along with a message based on how many questions were answered correctly by the user.

### Example gameplay
![Gameplay](https://github.com/DanteSenior/IFCS1summative1_task1/blob/main/QuizgameS1.PNG)

Here the user asked 10 * 10 * 7 = ?, In the enter answer box the user has typed 107, they then clicked submit.
As there answer is correct the quiz is displaying "Correct!"

### Troubleshooting
“Please enter a number”
This program requires the user to enter numbers only. If the message “Please enter a number” is displayed by the program, please ensure only numbers are entered into the “Enter answer” box.


## Technical documentation

### Introduction
This program is comprised of two modules;
main.py
question_generator.py
The program uses a graphical user interface (GUI) to display and allow responses from the user based on their selected difficulty.

### Technical explanation 
### main.py
This module contains functions for the GUI for this program tkinter, and for user input. A class is defined class QuizGUI containing the following functions: 

#### def __init__(self, root): 
Which is a constructor method that takes the parameters **(self, root)** and initializes the attributes for the **class QuizGUI** e.g. the GUI title i.e. **self.root.title("Summative I Math Quiz")**, **size self.root.geometry("800x600")**, and **self.score = 0**, allowing the quiz to start with a score of 0 as no questions have been answered.

#### def create_widgets(self):  
Which using the tkinter import creates the widgets i.e. labels and buttons allowing user to interact with and receive visual feedback from the GUI e.g. **self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)** which creates and assigns a tkinter button to **self.start_button** which now holds a reference to the button widget.

#### def start_quiz(self):
Changes the state of tkinter to enable/disable the start button e.g. **self.start_button.config(state=tk.DISABLED)** to disable the start button, preventing multiple starts, and calls the next question function **self.next_question()**.

#### def next_question(self):
Increase the value stored in the attribute self.question_number by 1 **self.question_number += 1**, clears the feedback and user entered text, and retrieves a new question from **generate_questions(self.difficulty.get())** with difficulty retrieved from **self.difficulty = tk.StringVar(value="easy")**

#### def check_answer(self):
Takes **user_answer = int(self.answer_entry.get())** and compares to **self.correct_answer**, displays message, and updates scores accordingly.

### def update_score(self):
Updates the f-string displayed on the GUI via a widget, showing score to user **self.score_label.config(text=f"Correct: {self.score} | Wrong: {self.wrong_answers}")**

### def display_final_score(self):
Uses an if-elif-else statement to assign a message to **result_message** based on end user quiz score 

### def main():
Creates the main GUI window, passes the root window to the class **QuizGUI**, and With **root.mainloop()** starts the tkinter event loop.

### if __name__ == "__main__":
Checks if the script is being run directly if the yes **def main()** function is called and the program is run.



### question_generator.py
This module contains one function **def generate_questions(difficulty):** with the parameter **difficulty**, using if-elif statements to run the appropriate function based on user input from main.py. Based on the function selected e.g. **elif difficulty == "medium"** then the variables **a, b, c** will be assigned random integer values from 1 to 12 (inclusive) using **random.randint(1, 12)** by importing the module **random** which uses functions to generate random integers. In this case the three variables are then assigned to **medium_question_ans** in the following format: **a * b + c** , this allows the users answer to be compared to the correct answer i.e. **medium_question_ans** the function then returns **“f"{a} * {b} + {c} = ?", medium_question_ans** with **f"{a} * {b} + {c} = ?** with the assigned integers being passed to main.py and subsequently displayed to the user, and **medium_question_ans** being used in main.py to compare to user answers.

### How to run locally
To run locally download or clone the github repo at git clone git@github.com:myrepo link
#### Depenacies 
Tkinter installed
Python 3.15+
