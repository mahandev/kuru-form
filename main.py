from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session encryption

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/choosing', methods=["GET","POST"])
def choosing():
    # Retrieve chosen_areas from session, if available, else an empty list
    chosen_areas = session.get('chosen_areas', [])
    return render_template('choose_culs_sports_etc.html', chosen_categories=chosen_areas)


@app.route('/areas')
def areas():
    return render_template('choose_area.html')


@app.route('/area_submit', methods=["GET", "POST"])
def area_choice():
    if request.method == "POST":
        # Store the chosen areas in session
        chosen_areas = request.form.getlist('areas')
        session['chosen_areas'] = chosen_areas
        print(chosen_areas)
        return redirect(url_for('choosing'))  # Redirect to 'choosing' page after submission

    return "No areas selected"


@app.route('/submit_basic', methods=["GET", "POST"])
def submit_basic():
    if request.method == "POST":
        print(request.form.get("first_name"))
        print(request.form.get("last_name"))
    return redirect(url_for('areas'))

@app.route('/submit_full', methods=["GET", "POST"])
def everything_submit():
    if request.method == "POST":
        chosen_sports = request.form.getlist('sports')
        chosen_culturals = request.form.getlist('culturals')
        chosen_somethings = request.form.getlist('somethings')
        print(chosen_sports)
        print(chosen_culturals)
        print(chosen_somethings)
    return "hi"


if __name__ == '__main__':
    app.run(debug=True)
