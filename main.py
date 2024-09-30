from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'tits'  # Required for session encryption

costs = {
    "badminton-men-single": 472,
    "badminton-men-double": 826,
    "badminton-mixed-double": 826,
    "basketball-women": 5074,
    "basketball-men": 5074,
    "frisbee-open": 5310,
    "handball-women": 1180,
    "handball-male": 1180,
    "sqaush-women-single": 413,
    "swimming-4x50-relay-freestyle-men": 708,
    "swimming-4x50-relay-freestyle-women": 708,
    "swimming-50m-freestyle-men": 295,
    "swimming-50m-backstroke-men": 295,
    "swimming-50m-breaststroke-men": 295,
    "swimming-50m-butterfly-men": 295,
    "swimming-50m-freestyle-women": 295,
    "swimming-50m-backstroke-women": 295,
    "swimming-50m-breaststroke-women": 295,
    "swimming-50m-butterfly-women": 295,
    "table-tennis-mens-team": 1180,
    "table-tennis-womens-team": 1003,
    "table-tennis-mens-doubles": 295,
    "table-tennis-mixed-doubles": 295,
    "tennis-mens-singles": 472,
    "tennis-mens-doubles": 826,
    "tennis-mixed-doubles": 826,
    "sprints-100m-male": 212,
    "volleyball-male": 2596,
    "volleyball-women": 1534,
    "chess-open": 319,
    "snooker-open": 354,
    "rhythm-solo-dance": 295,
    "step-off-group-dance": 1180,
    "group-dance-classical": 1180,
    "music-solo": 295,
    "art": 59,
    "photography": 59,
    "marcurious": 590,
    "digi-quest": 590,
    "bull-bear-brawl": 590,
    "mystery-maze": 826
}


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
    user_cost = 0
    chosen_sports = []
    chosen_culturals = []
    chosen_management = []

    if request.method == "POST":
        chosen_sports = request.form.getlist('sports')
        chosen_culturals = request.form.getlist('culturals')
        chosen_management = request.form.getlist('management')

        for i in chosen_culturals:
            user_cost += costs[i]
        
        for i in chosen_sports:
            user_cost += costs[i]
        
        for i in chosen_management:
            user_cost += costs[i]

    # User-friendly names
    # User-friendly names for sports
    sport_names = {
        "badminton-men-single": "Men's Singles (Badminton)",
        "badminton-men-double": "Men's Doubles (Badminton)",
        "badminton-mixed-double": "Mixed Doubles (Badminton)",
        "basketball-women": "Women (Basketball)",
        "basketball-men": "Men (Basketball)",
        "frisbee-open": "Open (Frisbee)",
        "handball-women": "Women (Handball)",
        "handball-male": "Men (Handball)",
        "sqaush-women-single": "Women's Singles (Squash)",
        "swimming-4x50-relay-freestyle-men": "4x50m Relay Freestyle Men (Swimming)",
        "swimming-4x50-relay-freestyle-women": "4x50m Relay Freestyle Women (Swimming)",
        "swimming-50m-freestyle-men": "50m Freestyle Men (Swimming)",
        "swimming-50m-backstroke-men": "50m Backstroke Men (Swimming)",
        "swimming-50m-breaststroke-men": "50m Breaststroke Men (Swimming)",
        "swimming-50m-butterfly-men": "50m Butterfly Men (Swimming)",
        "swimming-50m-freestyle-women": "50m Freestyle Women (Swimming)",
        "swimming-50m-backstroke-women": "50m Backstroke Women (Swimming)",
        "swimming-50m-breaststroke-women": "50m Breaststroke Women (Swimming)",
        "swimming-50m-butterfly-women": "50m Butterfly Women (Swimming)",
        "table-tennis-mens-team": "Men's Team (Table Tennis)",
        "table-tennis-womens-team": "Women's Team (Table Tennis)",
        "table-tennis-mens-doubles": "Men's Doubles (Table Tennis)",
        "table-tennis-mixed-doubles": "Mixed Doubles (Table Tennis)",
        "tennis-mens-singles": "Men's Singles (Tennis)",
        "tennis-mens-doubles": "Men's Doubles (Tennis)",
        "tennis-mixed-doubles": "Mixed Doubles (Tennis)",
        "sprints-100m-male": "Sprints - 100m Male (Athletics)",
        "volleyball-male": "Men (Volleyball)",
        "volleyball-women": "Women (Volleyball)",
        "chess-open": "Open (Chess)",
        "snooker-open": "Open (Snooker)"
    }


    cultural_names = {
        "rhythm-solo-dance": "Rhythm - Solo Dance",
        "step-off-group-dance": "Step Off - Group Dance",
        "group-dance-classical": "Natyanjali - Group Dance Classical",
        "music-solo": "Spotlight - Music Solo",
        "art": "Pixelate - Art",
        "photography": "Kahaani - Photography"
    }

    management_names = {
        "marcurious": "Marcurious",
        "digi-quest": "Digi Quest",
        "bull-bear-brawl": "Bull & Bear Brawl",
        "mystery-maze": "Mystery Maze"
    }

    return render_template('summary.html', 
                           chosen_sports=chosen_sports, 
                           chosen_culturals=chosen_culturals,
                           chosen_management=chosen_management,
                           total_cost=user_cost,
                           costs=costs,
                           sport_names=sport_names,
                           cultural_names=cultural_names,
                           management_names=management_names)



if __name__ == '__main__':
    app.run(debug=True)
