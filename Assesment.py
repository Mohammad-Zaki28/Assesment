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
    {"question": "When must you use indicators?", "options": ["Always", "Never", "Only on highways"], "answer": "Always"},
    {"question": "What should you do in heavy rain?", "options": ["Ride faster", "Be more cautious", "Stop immediately"], "answer": "Be more cautious"},
    {"question": "Can you ride without a licence?", "options": ["Yes", "No", "Sometimes"], "answer": "No"},
    {"question": "Who has right of way at roundabouts?", "options": ["Vehicles on your left", "You always", "Vehicles from your right"], "answer": "Vehicles from your right"},
    {"question": "What is the speed limit in urban areas?", "options": ["30 km/h", "50 km/h", "70 km/h"], "answer": "50 km/h"},
    {"question": "Why should you shoulder check?", "options": ["For fun", "To check blind spots", "To impress others"], "answer": "To check blind spots"},
    {"question": "What does a flashing red light mean?", "options": ["Go", "Slow down", "Stop"], "answer": "Stop"},
    {"question": "When should you use high beam?", "options": ["In daylight", "When alone at night", "In fog"], "answer": "When alone at night"},
    {"question": "What is the purpose of road signs?", "options": ["Confuse riders", "Give information", "Decorate streets"], "answer": "Give information"},
    {"question": "Can you park on a footpath?", "options": ["Yes", "No", "Only at night"], "answer": "No"},
]


#This is the main class that manages the quiz application
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Motorcycle Learner Test - Version 1")
        self.master.geometry("600x400")

        #initialize score and question index
        self.question_index = 0
        self.score = 0

        #create a label to display the question
        self.question_label = tk.Label(master, text="", wraplength=500, font=("Arial", 14), justify="center")
        self.question_label.pack(pady=20)

        #create radio buttons for answers options
        self.selected_option = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.selected_option, value="", font=("Arial", 12))
            btn.pack(anchor="w", padx=100)
            self.radio_buttons.append(btn)

        #button to go to the next question
        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        #load the first question
        self.load_question()

      #this methos loads the current question and its answers
    def load_question(self):
        if self.question_index < len(questions): # Changed 'question' to 'questions'
            current_q_data = questions[self.question_index] # Get the dictionary for the current question
            self.question_label.config(text=f"Q{self.question_index + 1}: {current_q_data['question']}")
            self.selected_option.set(None) # Reset the selected option

            # Update radio buttons with options from the current question
            for i in range(len(current_q_data['options'])):
                self.radio_buttons[i].config(text=current_q_data['options'][i], value=current_q_data['options'][i])
                self.radio_buttons[i].pack(anchor="w", padx=100) # Ensure the button is visible

            # Hide any extra radio buttons if there are fewer options for a question
            for i in range(len(current_q_data['options']), len(self.radio_buttons)):
                self.radio_buttons[i].pack_forget()

        else:
            self.show_result()

    #this method checks the selected and moves to the next question
    def next_question(self):
        selected = self.selected_option.get() 
        if selected:
            correct_answer = questions[self.question_index]['answer'] # Access 'answer' key
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