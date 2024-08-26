import json
import os

def load_questions():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'questions.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions

#python
####################################################################################

def python_easy():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'py_easy.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions

def python_inter():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'py_inter.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions

def python_adv():
    # Adjust the path based on where your JSON file is stored
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'py_adv.json')
    with open(json_path, 'r') as file:
        questions = json.load(file)
    return questions

####################################################################################