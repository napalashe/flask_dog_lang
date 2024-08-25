from flask import Flask, render_template, redirect, url_for, request
import random

app = Flask(__name__)


languages = ['Python', 'Java', 'JavaScript', 'C#', 'Ruby', 'Go', 'C++', 'Swift']


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
    
    selected_language = random.choice(languages)
    selected_paradigm = random.choice(paradigms)

    return selected_language, selected_paradigm


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/start', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dog_type = request.form.get('dog_type')
        activity = request.form.get('activity')

        if dog_type and activity:
            programming_language, programming_paradigm = determine_language_and_paradigm(dog_type, activity)
            return redirect(url_for('results', language=programming_language, paradigm=programming_paradigm))

    return render_template('index.html')


@app.route('/results')
def results():
    language = request.args.get('language')
    paradigm = request.args.get('paradigm')
    return render_template('results.html', language=language, paradigm=paradigm)

if __name__ == '__main__':
    app.run(debug=True)
