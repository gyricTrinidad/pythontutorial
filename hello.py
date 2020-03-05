from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def yo(name):
    quotes = [ "'Yeah yeah yeah yeah yeah' -- John Louis von Neumann ",
    "'Go go go go' --  Edsger Dijkstra ",
    "'To understand recursion you must first understand recursion..' -- Unknown",
    "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
    "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
    "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = randint(0,len(quotes)-1)
    quoted = quotes[randomNumber] 
    return render_template('template1.html', **locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)