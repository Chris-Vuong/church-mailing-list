from flask import render_template
from app import app
from app.forms import EmailContactForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris'}
    return render_template('index.html', title='Home', user=user)


@app.route('/emailsignup')
def emailSignup():
    form = EmailContactForm()
    return render_template(
        'emailsignup.html', 
        title='Email Newsletter Signup',
        form=form)