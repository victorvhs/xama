from flask import render_template, url_for, request, redirect, flash
from flask_login import login_manager, login_user, login_required, logout_user, current_user
from app import app
from app.models import tables
from app import db

db.create_all()

@app.login_manager.user_loader
def load_user(user_id):
    return tables.Users.query.get(int(user_id))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("login.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if nome != "vh" or senha != "123":
            return "Erro de senha"
        else:
            return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template("index.html",classe1="active")

@app.route("/novo")
@login_required
def novochamado():
    user = current_user.name # Nome de usuario será pego do loguin,talvez fique num cookei
    return render_template("novochamado.html",
                            user=user,
                            classe3="active")


@app.route("/novo", methods=['GET', 'POST'])
@login_required
def addnovo():
    if request.method == "POST":
        chamado = request.form.get("chamado")
        data = request.form.get("data")
        cidade = request.form.get("cidade")
        pedido = request.form.get("pedido")
        pedido_of = request.form.get("pedido_of")
        rota = request.form.get("rota")
        obs = request.form.get("obs")

        if chamado and data and rota and cidade and pedido:
            p = tables.Chamados(chamado,data,cidade, pedido, pedido_of, rota, obs)
            db.session.add(p)
            db.session.commit()
            flash("Chamado Incluido com Sucesso")
        else:
            if not chamado:
                flash("Insira do número do chamado")
            if not data:
                flash("Insira data de abertura")
            if not rota:
                flash("Insira Rota")
            if not cidade:
                flash("Insira Cidade")
            if not pedido:
                flash("Pedido não incluso.")

    return redirect(url_for("novochamado"))
@app.route("/busca")
@login_required
def listar():
    chamados = tables.Chamados.query.all()
    return render_template("lista.html", chamados=chamados, classe2="active")
