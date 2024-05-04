from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Go to /<name> for a custom screen :D\nExample: /Tyler or /Bob'

@app.route("/<username>/") # Flash will look at <username> and see that it's something we can pass into the function
def custom_user(username=None, post_id=None):
    return render_template('./index.html', name=username)


@app.route("/<username>/<int:post_id>") # We can go to index.html or an html and do a dynamic function by the double {}
def custom_user_and_post_id(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)

@app.route("/about")
def blog():
    return render_template("./aboutme.html")

@app.route("/blog/2024/dogs")
def blog2():
    return "This is my dog Riley!!"
