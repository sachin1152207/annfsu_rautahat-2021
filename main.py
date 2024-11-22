from flask import Flask, Blueprint

from blueprints import home
from blueprints import blogs
from blueprints import committes
from blueprints import about
from blueprints import contact

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(blogs)
app.register_blueprint(committes)
app.register_blueprint(about)
app.register_blueprint(contact)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")