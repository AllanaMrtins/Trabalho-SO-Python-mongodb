from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/alunos")
def alunos():
    return render_template("alunos.html")

@app.route("/monitores")
def monitores():
    return render_template("monitores.html")

@app.route("/atendimentos")
def atendimentos():
    return render_template("atendimentos.html")

if __name__ == "__main__":
    app.run(debug=True)