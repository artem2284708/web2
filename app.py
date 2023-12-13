from flask import Flask, request, render_template, url_for

app = Flask(__name__)


def countries_name(x):
    if x == 'Spain': return 'es1'
    if x == 'France': return 'fr1'
    if x == 'England': return 'gb1'
    if x == 'Greece': return 'gr1'
    if x == 'Italy': return 'it1'
    if x == 'Germany': return 'l1'
    if x == 'Russia': return 'ru1'
    return 'Options: Spain France England Greece Italy Germany Russia'


@app.route('/', methods=["GET", "POST"])
def check():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'Options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('home.html')


@app.route('/es1', methods=["GET", "POST"])
def es1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('es1.html')


@app.route('/fr1', methods=["GET", "POST"])
def fr1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('fr1.html')


@app.route('/gb1', methods=["GET", "POST"])
def gb1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('gb1.html')


@app.route('/gr1', methods=["GET", "POST"])
def gr1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('gr1.html')


@app.route('/it1', methods=["GET", "POST"])
def it1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('it1.html')


@app.route('/ru1', methods=["GET", "POST"])
def ru1():
    if request.method == 'POST':
        query = request.form['our_params']
        ans = countries_name(query)
        if ans != 'options: Spain France England Greece Italy Germany Russia':
            return render_template(f'{ans}.html', result=query)
        else:
            return render_template('home.html')
    else:
        return render_template('ru1.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4708)
