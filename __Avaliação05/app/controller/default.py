from flask import *
from app import app
from app.model.Clientes import *


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


# post -- CREATE
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == 'POST':

        if len(request.form) < 3:
            flash('Favor entrar todos os valores dos campos', 'error')

        else:
            create_crud(request.form)
            flash("Seu cliente foi criado, olhe no fim da lista")
            return redirect(url_for('read'))

    return render_template('create.html')


# get -- READ
@app.route("/read", methods=["GET", "POST"])
def read():
    clientes_str = read_crud()
    return render_template('read.html', clientes=clientes_str)


# put -- UPDATE
@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == 'POST':

        if len(request.form) < 4:
            flash('Favor entrar todos os valores dos campos', 'error')

        else:
            update_crud(request.form)
            flash("Seu cliente foi atualizado")
            return redirect(url_for('read'))

    return render_template('update.html')


# delete -- DELETE
@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":

        if len(request.form) < 1:
            flash('Favor entrar todos os valores dos campos', 'error')

        else:
            delete_crud(request.form["idcliente"])
            flash("Seu cliente foi deletado")
            return redirect(url_for('read'))

    return render_template('delete.html')
