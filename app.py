from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        testString = request.form["wrds"]
        return redirect(url_for("words", wrds=testString))
    else:
        return render_template("test.html")


@app.route("/<wrds>")
def words(wrds):
    cut = [x for x in wrds]
    cut2 = cut[2::3]
    return f"<h1>{(''.join(cut2))}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
