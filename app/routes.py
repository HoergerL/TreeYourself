from flask import render_template
from app import app
from app.forms import SurveyForm
from app.personas import woman30
import os
from app.classification import tags_from_answers

tags = []
with open('tags.txt') as file:
    for line in file:
        tags.append(line.strip('\n'))

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    print("Test")
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result = tags_from_answers(answers, tags) 
        print(result) 
    print(form.errors)
    return render_template('index.html', form=form)

@app.route('/persona1', methods=['GET', 'POST'])
def persona():
    form = SurveyForm()
    form.question1.data = "blub"
    for field, answer in zip(form,woman30):
        if field.type == "StringField":
            field.data = answer
            
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result = tags_from_answers(answers, tags)
        print(result)
    print(form.errors)
    return render_template('index.html', form=form)


@app.route('/tree', methods=['GET', 'POST'])
def tree():
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    return render_template('tree.html')

@app.route('/icon1', methods=['GET', 'POST'])
def icon1():
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    return "icon1 found, just wow!"
