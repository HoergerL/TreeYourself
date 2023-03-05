from flask import render_template
from app import app
from app.forms import SurveyForm
import app.personas as personas
from app.icons import icons
import os
from app.classification import tags_from_answers

tags = list(icons.keys())
#with open('tags.txt') as file:
#    for line in file:
#        tags.append(line.strip('\n'))

result_dict = dict()
used_tags = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global result_dict
    form = SurveyForm()
    print("Test")
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result_dict = tags_from_answers(answers, tags)
        tags = result_dict.keys() 
        print(result_dict) 
    print(form.errors)
    return render_template('index.html', form=form)

@app.route('/mentor', methods=['GET', 'POST'])
def mentor():
    return render_template('mentor.html')


@app.route('/persona1', methods=['GET', 'POST'])
def persona1():
    global result_dict
    form = SurveyForm()
    form.question1.data = "blub"
    for field, answer in zip(form,personas.woman40):
        if field.type == "StringField":
            field.data = answer
            
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result_dict = personas.woman40_result
        shared_keys = result_dict.keys() & icons.keys()
        print(shared_keys)
        filtered_keys = {}
        for key in shared_keys:
            filtered_keys[key] = icons[key]
        return render_template("tree.html", tags=list(filtered_keys.values()))
    print(form.errors)
    return render_template('index.html', form=form)

@app.route('/persona2', methods=['GET', 'POST'])
def persona2():
    global result_dict
    form = SurveyForm()
    form.question1.data = "blub"
    for field, answer in zip(form,personas.transgender_woman20):
        if field.type == "StringField":
            field.data = answer
            
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result_dict = personas.transgender_woman20_result
        shared_keys = result_dict.keys() & icons.keys()
        print(shared_keys)
        filtered_keys = {}
        for key in shared_keys:
            filtered_keys[key] = icons[key]
        return render_template("tree.html", tags=list(filtered_keys.values()))
    print(form.errors)
    return render_template('index.html', form=form)

@app.route('/persona3', methods=['GET', 'POST'])
def persona3():
    global result_dict
    print("reached persona1!")
    form = SurveyForm()
    form.question1.data = "blub"
    for field, answer in zip(form,personas.woman30):
        if field.type == "StringField":
            field.data = answer
    if form.validate_on_submit():
        answers = []
        print(f"submited!")
        for field in form:
            if field.type == "StringField":
                print(f"{field.name}={field.data}")
                answers.append(field.data)
        result_dict = personas.woman30_result
        shared_keys = result_dict.keys() & icons.keys()
        print(shared_keys)
        filtered_keys = {}
        for key in shared_keys:
            filtered_keys[key] = icons[key]
        return render_template("tree.html", tags=list(filtered_keys.values()))
    print(form.errors)
    return render_template('index.html', form=form)


@app.route('/tree', methods=['GET', 'POST'])
def tree():
    global result_dict
    print("/tree route reached")
    if not result_dict:
        result_dict = personas.transgender_woman20_result
    shared_keys = result_dict.keys() & icons.keys()
    print(shared_keys)
    filtered_keys = {}
    for key in shared_keys:
        filtered_keys[key] = icons[key]
    return render_template("tree.html", tags=list(icons.values()))
    # return render_template("tree.html", tags=list(filtered_keys.values()))

@app.route('/icon/<tag>', methods=['GET', 'POST'])
def icon(tag):
    # print(f"/icon/{tag} result dict: \n")
    # print(result_dict[tag])
    #return f"Tag {tag} found, just wow! Tag answer: \n" + str(tag_answer)
    answer=result_dict[tag][0]
    return render_template("icon.html", tag=tag, answer=answer)
