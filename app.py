from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def recommend_plan(age, gender, goal):
    if age < 13:
        diet = "Balanced meals rich in essential nutrients and moderate exercise."
        workout = "Light play, fun physical activities, supervised exercises."
        image = "kids.jpg"
    elif 13 <= age < 18:
        diet = "High-protein and moderate carbohydrates, focus on muscle and bone growth."
        workout = "Team sports, bodyweight training, swimming, and jogging."
        image = "teens.jpg"
    elif 18 <= age < 60:
        if goal == "Lose Weight":
            diet = "Low-carb, high-fiber meals with vegetables and lean proteins."
            workout = "High-intensity interval training (HIIT) 4 times a week."
        elif goal == "Gain Muscle":
            diet = "Caloric surplus with lean protein, carbs, and healthy fats."
            workout = "Structured weight training 4-5 times a week."
        else:
            diet = "Balanced diet with all macros and moderate exercise."
            workout = "150 minutes moderate cardio + 2 days strength training."
        image = "adults.jpg"
    else:
        diet = "High-fiber diet, adequate protein, and hydration."
        workout = "Walking, yoga, stretching, and low-impact exercises."
        image = "seniors.jpg"
    
    return diet, workout, image

@app.route('/', methods=['GET', 'POST'])
def index():
    plan = None
    selected_image = None
    if request.method == 'POST':
        age = int(request.form.get('age'))
        gender = request.form.get('gender')
        goal = request.form.get('goal')
        diet, workout, selected_image = recommend_plan(age, gender, goal)
        plan = {
            "diet": diet,
            "workout": workout,
            "age": age,
            "gender": gender,
            "goal": goal.title()
        }
    return render_template('index.html', plan=plan, image=selected_image)

if __name__ == '__main__':
    app.run(debug=True)




