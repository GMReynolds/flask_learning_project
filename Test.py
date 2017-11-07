#Flask tutorial
from flask import Flask

# Main app - pass in name to determine root path
app = Flask(__name__)


# connect to python route / homepage of web page
@app.route('/')
def index():
    return 'This is my homepage'


# tying URL of website to python function

# kick server check only run when called directly
if __name__ == "__main__":
    app.run(debug=True)