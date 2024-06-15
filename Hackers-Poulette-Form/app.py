from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
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
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    country = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    message = db.Column(db.Text, nullable=False)
    subject_repair = db.Column(db.Boolean, default=False)
    subject_order = db.Column(db.Boolean, default=False)
    subject_other = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Contact {self.first_name} {self.last_name}>'


class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    country = SelectField('Country:', choices=[
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

        new_contact = Contact(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            country=form.country.data,
            gender=form.gender.data,
            message=form.message.data,
            subject_repair=form.subject_repair.data,
            subject_order=form.subject_order.data,
            subject_other=form.subject_other.data
        )

        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('index.html', form=form)


@app.route('/submissions')
def submissions():
    contacts = Contact.query.all()
    return render_template('submissions.html', contacts=contacts)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
