import tkinter as tk
from tkinter import messagebox

qustions = [
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


#This is the main class that manages the quiz application
class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Motorcycle Learner Test - Version 1")
        self.master.geometry("600x400")

        #initialize score and question index
        self.question_index = 0
        self.score = 0

        