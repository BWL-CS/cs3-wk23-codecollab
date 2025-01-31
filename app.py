from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect form data
    user_input = {
        "adjective": request.form.get("adjective"),
        "noun": request.form.get("noun"),
        "verb": request.form.get("verb"),
        "number": request.form.get("number"),
        "place": request.form.get("place"),
        "animal": request.form.get("animal"),
        "food": request.form.get("food"),
        "mood": request.form.get("mood"),
        "superpower": request.form.get("superpower")
    }
    
    # Fill in to MadLibs story template
    story_template = [
        f"One day, a {user_input['adjective']} {user_input['animal']} decided to visit {user_input['place']} on a whim.",
        f"There, it found a {user_input['noun']} that could {user_input['superpower']}, and they instantly became best friends.",
        f"They spent {user_input['number']} hours {user_input['verb']} and laughing uncontrollably, attracting a crowd of confused onlookers.",
        f"To celebrate, they feasted on an absurd amount of {user_input['food']} while feeling {user_input['mood']}.",
        "It was a day no one would ever forget... mostly because someone recorded it and posted it online!"
    ]
    
    return render_template('result.html', story=story_template)

if __name__ == '__main__':
    app.run(debug=True)