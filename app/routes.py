from flask import render_template
from app import app
from app.forms import SurveyForm
from app.personas import woman30

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
        tags_from_answers(answers)  
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
        tags_from_answers(answers)  
    print(form.errors)
    return render_template('index.html', form=form)

def tags_from_answers(answers_list):
    print(answers_list)