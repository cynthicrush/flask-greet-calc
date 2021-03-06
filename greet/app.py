from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """Return 'welcome' greeting"""
    return """
    <html>
      <body>
        <h1>welcome</h1>
      </body>
    </html>"""


@app.route('/welcome/home')
def welcome_home():
    """Return 'welcome home' greeting"""
    return """
    <html>
      <body>
        <h1>welcome home</h1>
      </body>
    </html>"""


@app.route('/welcome/back')
def welcome_back():
    """Return 'welcome back' greeting"""
    return """
    <html>
      <body>
        <h1>welcome back</h1>
      </body>
    </html>"""
