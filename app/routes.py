from flask import render_template, flash, redirect, Flask, request
from app import app
from app.sql_to_html import sqlQuery
from app.forms import EmailContactForm
import os

@app.route('/')
@app.route('/index')
def index():
    '''Home page'''
    user = {'username': 'Chris'}
    return render_template('index.html', title='Home', user=user)

@app.route('/table')
def query():
    '''Test Query'''
    query = sqlQuery()
    return render_template('table.html', title='Test Query', headings=query[0], data=query[1])


@app.route('/emailsignup', methods=['GET', 'POST'])
def emailSignup():
    '''Email Signup page: Work in progress'''
    form = EmailContactForm()
    if form.validate_on_submit():
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO contacts VALUES (FirstName, LastName, Email) ''',
            (first_name, last_name, email))
            flash('Signup for {first_name}'.format(
                form.email.data
            ))
            return redirect('/success') # TODO: redirect to signup success
    return render_template(
        'emailsignup.html', 
        title='Email Newsletter Signup',
        form=form)
