from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, RadioField
from wtforms import SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Please select your Country:', choices=[
        ('Belgium', 'Belgium'), ('France', 'France'), ('Germany', 'Germany'),
        ('Netherlands', 'Netherlands'), ('United Kingdom', 'United Kingdom'),
        ('USA', 'USA'), ('Canada', 'Canada'), ('Mexico', 'Mexico')])
    gender = RadioField('Gender', choices=[
        ('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    subject_repair = BooleanField('Repair')
    subject_order = BooleanField('Order')
    subject_other = BooleanField('Others')
    honeypot = StringField('Honeypot')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        if form.honeypot.data:  # If honeypot is filled = a bot
            return redirect(url_for('index'))

        data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'country': form.country.data,
            'gender': form.gender.data,
            'message': form.message.data,
            'subjects': []
        }

        if form.subject_repair.data:
            data['subjects'].append('Repair')
        if form.subject_order.data:
            data['subjects'].append('Order')
        if form.subject_other.data:
            data['subjects'].append('Others')

        return redirect(url_for('thank_you', **data))

    return render_template('index.html', form=form)


@app.route('/thank_you')
def thank_you():
    data = request.args
    return render_template('thank_you.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
