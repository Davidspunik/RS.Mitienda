from flask import Flask, render_template, request, redirect, url_for
from database import init_db
from models import insert_audit, get_all_audits, get_audit_by_id, update_audit

app = Flask(__name__)
app.secret_key = 'clave_secreta_auditpro'

# Inicializar la base de datos
init_db()

# Rutas principales
@app.route("/")
def index():
    audits = get_all_audits()
    return render_template("index.html", audits=audits)

@app.route("/add", methods=["GET", "POST"])
def add_audit():
    if request.method == "POST":
        date = request.form["date"]
        area = request.form["area"]
        objective = request.form["objective"]
        responsible = request.form["responsible"]
        insert_audit(date, area, objective, responsible)
        return redirect(url_for("index"))
    return render_template("add_audit.html")

@app.route("/edit/<int:audit_id>", methods=["GET", "POST"])
def edit_audit(audit_id):
    audit = get_audit_by_id(audit_id)
    if request.method == "POST":
        date = request.form["date"]
        area = request.form["area"]
        objective = request.form["objective"]
        responsible = request.form["responsible"]
        update_audit(audit_id, date, area, objective, responsible)
        return redirect(url_for("index"))
    return render_template("edit_audit.html", audit=audit)

# Ejecutar la aplicación
if __name__== "_main_":
    app.run(debug=True)
    
    