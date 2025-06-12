import tkinter as tk
from tkinter import messagebox

# Version 2: Updated to 20 medium difficulty questions (replace or expand as needed)
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
    {"question": "How should you ride in wet weather?", "options": ["Faster", "Slower", "Same speed"], "answer": "Slower"},
    {"question": "What is the legal alcohol limit for learner riders?", "options": ["Zero", "50mg", "80mg"], "answer": "Zero"},
    {"question": "When should you use your indicators?", "options": ["Always when turning", "Only at roundabouts", "Never"], "answer": "Always when turning"},
    {"question": "Where do you place your hands when riding?", "options": ["On the tank", "Near brakes", "On handlebars"], "answer": "On handlebars"},
    {"question": "What must your motorcycle have to be road legal?", "options": ["WOF & Reg", "Helmet", "Radio"], "answer": "WOF & Reg"},
    {"question": "What should you do at a pedestrian crossing?", "options": ["Stop", "Beep", "Speed up"], "answer": "Stop"},
    {"question": "When can you overtake on the left?", "options": ["When safe", "Never", "In bus lanes"], "answer": "When safe"},
    {"question": "What does a blue sign mean?", "options": ["Mandatory", "Warning", "Stop"], "answer": "Mandatory"},
    {"question": "Who gives way at a T intersection?", "options": ["Top road", "Bottom road", "Right side"], "answer": "Bottom road"},
    {"question": "Where should you park your motorcycle?", "options": ["On the footpath", "Anywhere", "Designated spot"], "answer": "Designated spot"},
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Motorcycle Learner Test - Version 2")
        self.master.geometry("650x500")

        self.question_index = 0
        self.score = 0


        self.question_frame = tk.Frame(master, bd=2, relief="groove", padx=10, pady=10)
        self.question_frame.pack(pady=20)

        
        self.question_label = tk.Label(self.question_frame, text="", wraplength=500, font=("Arial", 14), justify="center")
        self.question_label.pack()

        self.selected_option = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.selected_option, value="", font=("Arial", 12), anchor="w", justify="left")
            btn.pack(anchor="w", padx=100)
            self.radio_buttons.append(btn)

 
        self.next_button = tk.Button(master, text="Next", command=self.next_question, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.next_button.pack(pady=10)

       
        self.warning_label = tk.Label(master, text="", fg="red", font=("Arial", 10))
        self.warning_label.pack()

      
        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.question_index < len(questions):
            current_q = questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {current_q["question"]}")
            self.selected_option.set(None)

       
            for i in range(len(current_q['options'])):
                text = f"{i + 1}. {current_q['options'][i]}"
                self.radio_buttons[i].config(text=text,value=current_q['options'][i])
                self.radio_buttons[i].pack(anchor="w", padx=100)

            for i in range(len(current_q['options']), len(self.radio_buttons)):
                self.radio_buttons[i].pack_forget()

        else:
            self.show_result()

    def next_question(self):
        selected = self.selected_option.get()
        if selected == "" or selected is None: 
            self.warning_label.config(text="Please select an answer before continuing.")
            return
        else:
            self.warning_label.config(text="") 

            correct_answer = questions[self.question_index]['answer']
            if selected == correct_answer:
                self.score += 1
            self.question_index += 1
            self.load_question()

    def show_result(self):
        total_score = 20 
        passed = self.score >= 17
        result_msg = f"You scored {self.score} out of {total_score}"
        if passed:
            self.result_label.config(text=result_msg + "\nCongratulations! You have passed.", fg="green")
        else:
            self.result_label.config(text=result_msg + "\nCongratulations! You have failed.", fg="red")

        self.next_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
