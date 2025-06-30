from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            feet = float(request.form["height"])
            inches = request.form.get("inches", "0")
            inches = float(inches) if inches else 0.0

            # Convert height to meters
            height_m = ((feet * 12) + inches) * 0.0254

            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"  
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            # Ideal weight range calculation
            min_ideal_weight = round(18.5 * (height_m ** 2), 1)
            max_ideal_weight = round(24.9 * (height_m ** 2), 1)

            result = (
                f"Your BMI is {bmi}. You are {category}. "
                f"Ideal weight range for your height: {min_ideal_weight} kg – {max_ideal_weight} kg."
            )
        except:
            result = "Please enter valid numbers."

    return render_template("Templates.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            feet = float(request.form["height"])
            inches = request.form.get("inches", "0")
            inches = float(inches) if inches else 0.0

            # Convert height to meters
            height_m = ((feet * 12) + inches) * 0.0254

            bmi = round(weight / (height_m ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            # Ideal weight range calculation
            min_ideal_weight = round(18.5 * (height_m ** 2), 1)
            max_ideal_weight = round(24.9 * (height_m ** 2), 1)

            result = (
                f"Your BMI is {bmi}. You are {category}. "
                f"Ideal weight range for your height: {min_ideal_weight} kg – {max_ideal_weight} kg."
            )
        except:
            result = "Please enter valid numbers."

    return render_template("Templates.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)