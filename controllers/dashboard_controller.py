from flask import render_template, request, redirect, url_for, jsonify
from database.replica_set import replica_status

def home():
    if request.method == 'POST':
        return redirect(url_for('dashboard.home'))
        
    return render_template('dashboard.html') 

# <-- 3. ADICIONADO AQUI NO FINAL: A função que vai processar o botão de Login
def login_controller():
    if request.method == 'POST':
        # Aqui você pode capturar os dados para validar no MongoDB depois:
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        # Redireciona para a página inicial (home) após clicar em Entrar
        return redirect(url_for('dashboard.home'))
        
    return render_template('login.html')

def health():
    return jsonify({"status": "ok"})

def status_replica():
    return jsonify(replica_status())