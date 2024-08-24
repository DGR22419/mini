import json
import os

def load_questions():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'questions.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions

def python_easy():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'python_easy.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions