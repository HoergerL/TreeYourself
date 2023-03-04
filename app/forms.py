from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea

class SurveyForm(FlaskForm):
    question1 = TextAreaField("One Thing You Could Do Better", render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question2 = StringField("Things to Learn About", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question3 = StringField("Improve Your Habits", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question4 = StringField("Your Social Life in the Future", render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'}, widget=TextArea())
    question5 = StringField("Your Leisure Activity in the Future", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question6 = StringField("Your Family Life in the Future", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question7 = StringField("Your Career in the Future", widget=TextArea(),render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question8 = StringField("Qualities You Admire", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question9 = StringField("The Ideal Future", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    question10 = StringField("A Future to Avoid", widget=TextArea(), render_kw={'class': 'form-control', 'rows': 20, 'style': 'width: 1000px'})
    submit = SubmitField('Submit')

# Not used yet
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')