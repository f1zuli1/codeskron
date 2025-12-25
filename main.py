from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/hediye")
def hediye():
    return render_template("hediye.html")

if __name__ == "__main__":
    app.run(debug=True)
