from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index():
    # Pass variables from Python to HTML!
    name_data = "natalie"
    lucky_num = 13
    return render_template("index.html", name=name_data, num=lucky_num)


# function to handle form submission
# the app.route decorate maps to the submit button
@app.route("/submit", methods=['POST'])
def submit():
    # create python variable to hold form data
    form_data = {
        'name': request.form.get('name'),
        'age': request.form.get('age'),
        'hobby': request.form.get('favorite_hobby'),
        'color': request.form.get('favorite_color'),
        'lucky': request.form.get('lucky_number')
    }
    # pass data into results page
    return render_template("results.html", form_data=form_data)


# TO RUN YOUR APP enter "flask run" into the TERMINAL
# (if you closed your terminal, open it again with CTRL + `)
# TO STOP click CTRL + C in the TERMINAL

# Set up main method so we can use the RUN button
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)