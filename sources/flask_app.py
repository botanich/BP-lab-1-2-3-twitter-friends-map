from flask import Flask, redirect, render_template, request, url_for
import main


app = Flask(__name__)
app.config['Debug'] = True


def before_request():
    app.jinja_env.cache = {}


app.before_request(before_request)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("startpage.html")

    if request.method == "POST":
        main.main(request.form['contents'])
        return redirect(url_for('map'))


@app.route("/map")
def map():
    return render_template("map.html")


if __name__ == "__main__":
    app.run()
