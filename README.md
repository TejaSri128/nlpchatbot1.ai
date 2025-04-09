🧠 Chatbot with NLP Preprocessing & GUI
This project is a simple chatbot built using Python. It reads a CSV file of questions and answers, preprocesses the data using NLP (tokenization, stopword removal, lemmatization, etc.), and allows users to ask questions through a graphical interface (Tkinter).

📂 Project Structure
graphql
Copy
Edit
chatbot_project/
│
├── questions_answers.csv       # Input CSV file with 'question' and 'answer' columns
├── processed_qa.csv            # Output generated after preprocessing
├── chatbot_gui.py              # Main script to launch the chatbot GUI
├── preprocess_data.py          # Script for Module-1 (Data Preparation)
├── README.md                   # This file
✅ Features
Word tokenization

Stopword removal

POS tagging + Lemmatization

Question formatting (joined with hyphens)

GUI with Tkinter for interaction

📦 Requirements
Install the necessary packages using pip:

bash
Copy
Edit
pip install pandas nltk
Also, download required NLTK datasets (done automatically in the code):

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
🧾 Step-by-Step Usage
🔹 1. Prepare the CSV
Create a file named questions_answers.csv with two columns:

question	answer
What is AI?	AI stands for Artificial Intelligence.
How does machine learning work?	It learns patterns from data.
🔹 2. Run Preprocessing (Module-1)
This step processes your questions and creates processed_qa.csv.

bash
Copy
Edit
python preprocess_data.py
Note: You can also integrate this directly into the GUI script if preferred.

🔹 3. Launch the GUI (Module-2)
Start the chatbot with:

bash
Copy
Edit
python chatbot_gui.py
Ask a question in the GUI, and it will return the best-matched answer.

⚙️ Customization
Add more Q&A pairs in questions_answers.csv and rerun the preprocessing script.

Modify NLP steps (e.g., add stemming, synonyms, etc.) for improved matching.

🛠 Files Description
File	Description
questions_answers.csv	Original dataset with questions and answers
preprocess_data.py	Script for processing and saving cleaned data
processed_qa.csv	Output CSV of processed questions + answers
chatbot_gui.py	Tkinter GUI to interact with the chatbot
💡 Example Interaction
User input: What's AI?
Bot output: AI stands for Artificial Intelligence.

📌 Notes
Make sure the processed version of the question exactly matches after preprocessing.

You can improve fuzzy matching using libraries like fuzzywuzzy or difflib.
