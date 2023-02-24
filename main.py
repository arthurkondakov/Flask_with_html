from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "Ivan"
    user_date = {
        "name": "Artur",
        "phone": "+7 123 456 78 90",
        "email": "ivan_dev@gmail.com",
        "telegram": "ivandev"
    }
    page = render_template("name.html", name=name, user=user_date)
    return page

app.run(debug=True)