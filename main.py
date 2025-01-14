import tkinter as tk
from tkinter import messagebox
from question_generator import generate_questions

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Summative I Math Quiz")
        self.root.geometry("800x600")
        self.score = 0
        self.correct_answer = 0
        self.wrong_answers = 0
        self.question_number = 0
        self.correct_answer = None
        self.difficulty = tk.StringVar(value="easy")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Select Difficulty:").pack()
        for level in ["easy", "medium", "hard"]: 
            tk.Radiobutton(self.root, text=level.capitalize(), variable=self.difficulty, value=level).pack()
            
        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)      
        self.start_button.pack(pady=10)
        
        self.question_label = tk.Label(self.root, text="", font=("TimesNewRoman", 16))
        self.question_label.pack(pady=20)
        
        tk.Label(self.root, text="Enter answer:").pack()
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        self.submit_button.config(state=tk.DISABLED)
        
        self.feedback_label = tk.Label(self.root, text="",  font=("TimesNewRoman", 16))
        self.feedback_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="", font=("TimesNewRoman", 16))
        self.score_label.pack(pady=10)
    
    def start_quiz(self):    
        self.start_button.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.NORMAL) 
        self.next_question()
    
    def next_question(self):
        self.question_number += 1
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        question, self.correct_answer = generate_questions(self.difficulty.get())
        self.question_label.config(text=question)
        
    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer: 
                self.score += 1
                self.feedback_label.config(text="Correct!", fg="green")
            else:
                self.wrong_answers += 1
                self.feedback_label.config(text="Incorrect!", fg="red")
            self.update_score()
            self.root.after(1500, self.next_question)
        except ValueError:
            self.feedback_label.config(text="Please enter a number", fg="red") 
    
    def update_score(self):
        self.score_label.config(text=f"Correct: {self.score} | Wrong: {self.wrong_answers}")
    
    def display_final_score(self):
        if self.score >= 8:
            result_message = "Amazing job 👏👏👏🏆🏆🏆"
        elif 5 <= self.score < 8:
            result_message = "Not bad!, keep practicing to get top marks."
        else:
            result_message = "Looks like studying would be a good idea."
        messagebox.showinfo("Final Score", result_message)

def main():
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()