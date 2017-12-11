import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<user>")

def index(user=None):
    return render_template("user.html", user=user)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

"""
@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
"""

"""
@app.route('/')
def index():
    return '<h2>Method used {}</h2>'.format(request.method)

@app.route("/sushi", methods=['GET', 'POST'])
def sushi():
    if request.method == 'GET':
        return "<h2>GET!!</h2>"
    elif request.method == 'POST':
        return "<h2>POST!!</h2>"
    else:
        return "<h2>Method used {}</h2>".format(request.method)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

"""

"""    
@app.route('/')
def index():
    return '<h2>This is the homepage</h2>'
    
@app.route('/krystal')
def krystal():
    return "<h2>This is Krystal's secret page</h2>"

using int
@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>Heya there {}</h2>".format(post_id)


@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey there, {}!</h2>".format(username)
"""

