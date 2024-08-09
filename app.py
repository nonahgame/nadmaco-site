from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template')

@app.route("/")
def template():
    return render_template("home.html")

JOBS = [
        {
        "id": 1,
        "title": "Data Scintist",
        "location": "Nigeria",
        "salary": "NGN 50000"
    },
    {
        "id": 2,
        "title": "Front-Backend Engineer",
        "location": "S-Africa, Liberia"
    },
    {
    "id": 3,
    "title": "Data Analyst",
    "location": "US, UK",
    "salary": "$, 200"
    }
]

@app.route("/page1")
def pages():
    return render_template('home.html',jobs=JOBS)

@app.route("/api")
def pagejs():
    return jsonify(render_template('page.html'), JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
