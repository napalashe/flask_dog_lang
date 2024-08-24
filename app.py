from flask import Flask, render_template, request


app = Flask(__name__)

dog_to_language = {
    'Golden Retriever': 'Python',
    'German Shepherd': 'Java',
    'Bulldog': 'JavaScript',
    'Poodle': 'C#',
    'Beagle': 'Ruby',
    'Dachshund': 'Go',
    'Siberian Husky': 'C++',
    'Chihuahua': 'Swift'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dog_type = request.form.get('dog_type')
        programming_language = dog_to_language.get(dog_type, 'Python')
        return render_template('index.html', result=True, language=programming_language)
    
    return render_template('index.html', result=False)

if __name__ == '__main__':
    app.run(debug=True)