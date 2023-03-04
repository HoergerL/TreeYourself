from flask import render_template
from app import app
from app.forms import SurveyForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        tags_from_answers(answers)  
    return render_template('index.html', form=form)

def tags_from_answers(answers_list):
    print(answers_list)