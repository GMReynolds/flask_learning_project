from flask import Flask, render_template, make_response, request, redirect
import csv
# Creating flask application
app = Flask(__name__)

duckionary = {'SpiderDuck': 7, 'Friar Duck': 2, 'Mr T Duck': 10}

#Creating class of ducks for data to be stored in a python object
class Ducks:
    # Objects of this class will have a name, price , score and image
    def __init__(self, name, price, score, image):
        self.name = name
        self.price = price
        self.score = score
        self.image = image


global name
name = "New User"

global duckList
duckList = []

# Created home page where it greets the user
@app.route('/')
def hello_world():
    if name == "New User":
        return redirect("/signup", code=302)
    # Returns the index.html page and returns the user set in the template
    return make_response(render_template("index.html", user = name, list=duckList))

# Create sign up page where user can enter details to sign up
# Allowing both get and post requests
@app.route('/signup' , methods = ['GET','POST'])
def signuppage():
    # if post method set name to user inputted name
    if request.method == 'POST':
        global name
        name = request.form.get('username')
        return hello_world()
    return make_response(render_template("sign_up.html", list=duckList))

# Logs out user and send back to login page
@app.route('/logout')
def logout():
    name = "New User"
    # Code 302 redirect code to send user back to intro page
    return redirect("/signup", code=302)

# reads in data from csv
def getdata():
    with open('./resources/Ducks.csv', 'rb') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',' , quotechar= '|')
        # Reads in the rows of csv and creates a new duck object for each row
        for row in readcsv:
            if row[3] == "_":
                newDuck = Ducks(row[0], row[1], row[2], "https://cdnph.upi.com/ph/st/th/5491469211157/2016/i/14692123251060/v1.5/Giant-inflatable-duck-missing-from-New-Jersey-town.jpg?lg=2")
            else:
                newDuck = Ducks(row[0], row[1], row[2], row[3])
            # add on new duck to the list of ducks
            duckList.append(newDuck)

# Run the flask application
if __name__ == "__main__":
    getdata()
    app.run(debug=True)
# get request gets information
# post passes it back to the system


