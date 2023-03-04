from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Optional
from wtforms.widgets import TextArea

class SurveyForm(FlaskForm):
    question1 = StringField("One Thing You Could Do Better", widget=TextArea(), validators=[DataRequired()])
    question2 = StringField("Things to Learn About", widget=TextArea(), validators=[DataRequired()])
    question3 = StringField("Improve Your Habits", widget=TextArea(), validators=[DataRequired()])
    question4 = StringField("Your Social Life in the Future", widget=TextArea(), validators=[DataRequired()])
    question5 = StringField("Your Leisure Activity in the Future", widget=TextArea(), validators=[DataRequired()])
    question6 = StringField("Your Family Life in the Future", widget=TextArea(), validators=[DataRequired()])
    question7 = StringField("Your Career in the Future", widget=TextArea(), validators=[DataRequired()])
    question8 = StringField("Qualities You Admire", widget=TextArea(), validators=[DataRequired()])
    question9 = StringField("The Ideal Future", widget=TextArea(), validators=[DataRequired()])
    question10 = StringField("A Future to Avoid", widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Submit')

# Not used yet
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')