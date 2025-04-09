import pandas as pd
import nltk
import tkinter as tk
from tkinter import messagebox

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from chatbot_backend import *

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# ========== NLP PREPROCESSING SETUP ==========

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def preprocess_question(question):
    tokens = word_tokenize(question)
    filtered = [w for w in tokens if w.lower() not in stop_words]
    pos_tags = pos_tag(filtered)
    lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
    return '-'.join(lemmatized)

# ========== LOAD PROCESSED QA DATA ==========

try:
    qa_data = pd.read_csv("processed_qa.csv")
except FileNotFoundError:
    print("Error: 'processed_qa.csv' not found. Please run Module-1 to generate it.")
    exit()

# ========== GUI APP ==========

def get_answer():
    user_q = question_entry.get()
    if not user_q.strip():
        messagebox.showwarning("Input Error", "Please enter a question.")
        return
    
    processed_q = preprocess_question(user_q)
    match = qa_data[qa_data['processed_question'] == processed_q]
    
    if not match.empty:
        answer = match.iloc[0]['answer']
        answer_display.config(state="normal")
        answer_display.delete("1.0", tk.END)
        answer_display.insert(tk.END, answer)
        answer_display.config(state="disabled")
    else:
        answer_display.config(state="normal")
        answer_display.delete("1.0", tk.END)
        answer_display.insert(tk.END, "Sorry, I don’t have an answer for that.")
        answer_display.config(state="disabled")

# Create GUI window
window = tk.Tk()
window.title("Simple Chatbot")
window.geometry("500x300")

# Label
label = tk.Label(window, text="Ask a question:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
question_entry = tk.Entry(window, width=60)
question_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(window, text="Get Answer", command=get_answer)
submit_button.pack(pady=10)

# Text box for displaying answer
answer_display = tk.Text(window, height=5, width=60, wrap="word", state="disabled")
answer_display.pack(pady=5)

# Run GUI loop
window.mainloop()
