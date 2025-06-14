import tkinter as tk
from tkinter import messagebox

questions = [
    {"question": "What does a red traffic light mean?", "options": ["Stop", "Go", "Slow down"], "answer": "Stop"},
    {"question": "What side do you ride on in NZ?", "options": ["Left", "Right", "Middle"], "answer": "Left"},
    {"question": "What should you wear while riding?", "options": ["Helmet", "Hat", "Cap"], "answer": "Helmet"},
    {"question": "What does a yellow light mean?", "options": ["Speed up", "Stop if safe", "Go faster"], "answer": "Stop if safe"},
    {"question": "How old must you be to get a learner licence?", "options": ["14", "15", "16"], "answer": "16"},
    {"question": "What should you check before starting a ride?", "options": ["Tyres", "Brakes", "Both"], "answer": "Both"},
    {"question": "Can you use your phone while riding?", "options": ["Yes", "No", "Only at red lights"], "answer": "No"},
    {"question": "Where should you look when turning?", "options": ["Behind", "Left", "Direction you're going"], "answer": "Direction you're going"},
    {"question": "What should you do at a stop sign?", "options": ["Stop completely", "Slow down", "Keep going"], "answer": "Stop completely"},
    {"question": "What does a green light mean?", "options": ["Stop", "Go", "Wait"], "answer": "Go"},
]



class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Motorcycle Learner Test - Version 1")
        self.master.geometry("600x400")


        self.question_index = 0
        self.score = 0


        self.question_label = tk.Label(master, text="", wraplength=500, font=("Arial", 14), justify="center")
        self.question_label.pack(pady=20)


        self.selected_option = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.selected_option, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=100)
            self.radio_buttons.append(btn)


        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)


        self.load_question()
        

    def load_question(self):
        if self.question_index < len(questions): # Changed 'question' to 'questions'
            current_q_data = questions[self.question_index] 
            self.question_label.config(text=f"Q{self.question_index + 1}: {current_q_data['question']}")
            self.selected_option.set(None)


            for i in range(len(current_q_data['options'])):
                self.radio_buttons[i].config(text=current_q_data['options'][i], value=current_q_data['options'][i])
                self.radio_buttons[i].pack(anchor="w", padx=100)


            for i in range(len(current_q_data['options']), len(self.radio_buttons)):
                self.radio_buttons[i].pack_forget()

        else:
            self.show_result()


    def next_question(self):
        selected = self.selected_option.get() 
        if selected:
            correct_answer = questions[self.question_index]['answer'] 
            if selected == correct_answer:
                self.score += 1
            self.question_index += 1
            if self.question_index < len(questions):
                self.load_question()
            else:
                self.show_result()
        else:
            messagebox.showwarning("No selection", "Please select an answer before continuing.")

    #this method displays the final score in a message box
    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(questions)}")
        self.master.quit()

    #this part creates the main windows and runs the application
if __name__ == "__main__":
        root = tk.Tk()
        app = QuizApp(root)
        root.mainloop()