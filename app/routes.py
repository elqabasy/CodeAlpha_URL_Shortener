import string
import random
from flask import render_template, request, redirect, flash
from app import app, db
from app.models import URL

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['original_url']
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'http://' + original_url
        short_url = generate_short_url()
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('result.html', short_url=short_url)
    return render_template('index.html')


@app.route('/short/<short_url>')
def redirect_to_original(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)

# @app.route('/all_urls')
# def display_all_urls():
#     urls = URL.query.all()
#     return render_template('all_urls.html', urls=urls)
