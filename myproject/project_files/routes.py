from project_files import app
from flask import render_template, url_for, redirect, flash
from project_files.form import City








@app.errorhandler(404)
def handle_404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def handle_500(e):
    return render_template('500.html'), 500