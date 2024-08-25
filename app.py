from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)

# Possible programming languages
languages = ['Python', 'Java', 'JavaScript', 'C#', 'Ruby', 'Go', 'C++', 'Swift']

# Possible programming paradigms
paradigms = [
    'Object-Oriented Programming (OOP)', 
    'Functional Programming', 
    'Procedural Programming', 
    'Event-Driven Programming', 
    'Declarative Programming', 
    'Reactive Programming', 
    'Logical Programming'
]

def determine_language_and_paradigm(dog_type, activity):
    # Randomly select a language and paradigm from all possibilities
    selected_language = random.choice(languages)
    selected_paradigm = random.choice(paradigms)

    return selected_language, selected_paradigm

# Route for the welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for the main page
@app.route('/start', methods=['GET', 'POST'])
def index():
    dog_type = request.form.get('dog_type')
    activity = request.form.get('activity')

    if request.method == 'POST' and dog_type and not activity:
        # Render the template to show the activity dropdown after selecting the dog
        return render_template('index.html', result=False, dog_type=dog_type)

    if request.method == 'POST' and dog_type and activity:
        # Continue to the next step after both dog and activity are selected
        programming_language, programming_paradigm = determine_language_and_paradigm(dog_type, activity)
        return render_template('index.html', result=True, language=programming_language, paradigm=programming_paradigm, dog_type=dog_type, activity=activity)
    
    return render_template('index.html', result=False)

if __name__ == '__main__':
    app.run(debug=True)
