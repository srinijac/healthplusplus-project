# views.py

from flask import render_template

from app import app

@app.route('/tictactoe')
def.index():
    return render_template("reactTTT.js")
