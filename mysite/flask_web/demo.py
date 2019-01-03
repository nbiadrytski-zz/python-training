from flask import Flask, render_template
# importing Flask class object from flask library and render_template method

# instantiating Flask class object
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


# to run in browser: localhost:5000

# Case 1 - If you execute the script, then
# __name__ == "__main__"

# Case 2 - If script is imported, then:
# __name__ == "__demo__"