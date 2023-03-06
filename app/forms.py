from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea

class SurveyForm(FlaskForm):
    question1 = StringField("What is one thing you could do better right now?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question2 = StringField("What would you like to learn more about?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question3 = StringField("What habits would you like to improve?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question4 = StringField("Consider your social life, what would you like to improve in the future?", render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, widget=TextArea(), validators=[DataRequired()])
    question5 = StringField("What leisure activity do you wish to focus on in the future?", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question6 = StringField("How would you like your family life to be in the future?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question7 = StringField("Considering your career, where do you want to be in six months? Two years? Five years? Why? What are you trying to accomplish?", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question8 = StringField("Think about the people you admire, which qualities do they possess that you wish you had?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question9 = StringField("If you could imagine an ideal future, what would it look like?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question10 = StringField("What future would you like to avoid for yourself?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    mentor = BooleanField("I'm a Mentor!")
    submit = SubmitField('Submit',  render_kw={'class': 'btn btn-default'})

# Not used yet
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')