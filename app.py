from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    todo = [t for t in tasks if t["status"] == "todo"]
    progress = [t for t in tasks if t["status"] == "progress"]
    done = [t for t in tasks if t["status"] == "done"]
    return render_template("index.html", todo=todo, progress=progress, done=done)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    tasks.append({"name": task, "status": "todo"})
    return redirect("/")

@app.route("/move/<int:id>/<status>")
def move(id, status):
    tasks[id]["status"] = status
    return redirect("/")

app.run(debug=True)