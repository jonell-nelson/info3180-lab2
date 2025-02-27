from app import app
from datetime import datetime
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

###
# The profile view function using the format_date_joined function
### 
@app.route("/profile")
def profile():

    profile_data = {
        'full_name' : 'Jonell Nelson',
        'username' : 'jonellnelson1',
        'location' : 'Kingston, Jamaica',
        'bio': 'I love coding and building cool projects!',
        'posts': 20,
        'followers': 1000,
        'following': 50,
        'date_joined': datetime(2022, 9, 7)
    }    

    return render_template('profile.html', **profile_data)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

def format_date_joined(date):
    return date.strftime('%B, %Y')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
