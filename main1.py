"""

#################################################################
NOTES

## project structure

test_flask_v2 (project root)

   - main1.py
   - static (directory)
   - templates (package)
       -- __init__.py
       -- welcome.html


#################################################################
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")
