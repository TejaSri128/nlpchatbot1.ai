import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Step 1: Read the CSV file
data = pd.read_csv('questions_answers.csv')  # Change this to your file path
print("Original Data:")
print(data.head())

# Step 2: Word Tokenization
data['tokens'] = data['question'].apply(word_tokenize)

# Step 3: Remove Stopwords
stop_words = set(stopwords.words('english'))
data['filtered_tokens'] = data['tokens'].apply(lambda tokens: [w for w in tokens if w.lower() not in stop_words])

# Helper function to convert POS tags for lemmatization
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

# Step 4: Apply Lemmatization with POS Tagging
lemmatizer = WordNetLemmatizer()
def lemmatize_tokens(tokens):
    pos_tags = pos_tag(tokens)
    return [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]

data['lemmatized'] = data['filtered_tokens'].apply(lemmatize_tokens)

# Step 5: Combine Words with a Hyphen
data['processed_question'] = data['lemmatized'].apply(lambda tokens: '-'.join(tokens))

# Step 6: Map Respective Answers (already preserved in DataFrame)

# Step 7: Store Results in Output CSV File
output = data[['processed_question', 'answer']]
output.to_csv('processed_qa.csv', index=False)
print("Processed data saved to 'processed_qa.csv'")
def preprocess_user_input(question):
    tokens = word_tokenize(question)
    filtered = [w for w in tokens if w.lower() not in stop_words]
    pos_tags = pos_tag(filtered)
    lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
    return '-'.join(lemmatized)

# Step 1: Ask the User a Question
user_question = input("Ask me a question: ")

# Step 2: Preprocess the Question
processed_user_question = preprocess_user_input(user_question)

# Step 3: Find the Answer from Output CSV File
qa_data = pd.read_csv('processed_qa.csv')

match = qa_data[qa_data['processed_question'] == processed_user_question]

# Step 4: Display Output
if not match.empty:
    print("Answer:", match.iloc[0]['answer'])
else:
    print("Sorry, I don’t have an answer for that.")
