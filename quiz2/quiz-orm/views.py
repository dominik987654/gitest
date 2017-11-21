from flask import render_template, request, redirect, url_for, abort, flash
from app import app
from models import Pytanie, Odpowiedz
from forms import *


@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')


@app.route('/lista')
def lista():
    """Pobranie wszystkich pytań z bazy i zwrócenie szablonu z listą pytań"""
    pytania = Pytanie().select().annotate(Odpowiedz)
    if not pytania.count():
        flash('Brak pytań w bazie.', 'kom')
        return redirect(url_for('index'))

    return render_template('lista.html', pytania=pytania)
