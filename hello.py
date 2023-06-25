from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# create flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key no one is supposed to know"

#if __name__ == "__main__":
    #app.run(debug=True)
# Create A FORM CLASS
class NameForm(FlaskForm):
    name = StringField("Whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

#create a route decorator
@app.route('/')
#def index():
    #return "<h1>Hello World!</h1>"
#FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags
def index():
    first_name = "Aisha"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

#localhost:5000/user/Aisha
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Create custom Error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("name.html",
                           name = name,
                           form = form)