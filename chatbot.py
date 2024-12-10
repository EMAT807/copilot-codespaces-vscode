# Import the required libraries  
import nltk  
from nltk.stem import WordNetLemmatizer  
lemmatizer = WordNetLemmatizer()  

# Define a function to process user input  
def process_input(input_text):  
    # Tokenize the input text  
    tokens = nltk.word_tokenize(input_text)  
    # Lemmatize the tokens  
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  
    return tokens  

# Define a function to respond to user input  
def respond_to_input(input_text):  
    # Process the input text  
    tokens = process_input(input_text)  
    # Define a simple response  
    response = "You said: " + " ".join(tokens)  
    return response  

# Test the chatbot  
input_text = "Hello, how are you?"  
response = respond_to_input(input_text)  
print(response)
