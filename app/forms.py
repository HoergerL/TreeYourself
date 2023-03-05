from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea

class SurveyForm(FlaskForm):
    question1 = StringField("What is one thing you could do better?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question2 = StringField("What would you like to learn about?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question3 = StringField("How could you improve your habits?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question4 = StringField("How could you improve your social life in the future?", render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, widget=TextArea(), validators=[DataRequired()])
    question5 = StringField("What leisure activity do you wish to focus on in the future?", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question6 = StringField("How would you like your family life to be in the future?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question7 = StringField("How do you imagine your career to unfold?", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
    question8 = StringField("What qualities do you admire?", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 10, 'style': 'width: 1000px'}, validators=[DataRequired()])
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