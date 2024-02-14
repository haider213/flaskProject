from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword'].lower()
        abbreviation = request.form['abbreviation'].lower()
        age = int(request.form['age'])
        response_type = request.form['response_type']
        response = request.form['response']

        # Create folder for age group if it doesn't exist
        age_folder = os.path.join(app.root_path, f"age_{age}")
        if not os.path.exists(age_folder):
            os.makedirs(age_folder)

        # Create a text file for the keyword within the age group folder
        keyword_file = os.path.join(age_folder, f"{keyword}.txt")
        with open(keyword_file, 'a') as f:
            f.write(f"{response_type}: {response}\n")

        # Also create a text file for the abbreviation
        abbreviation_file = os.path.join(age_folder, f"{abbreviation}.txt")
        with open(abbreviation_file, 'w') as f:
            f.write(f"{response_type}: {response}\n")

        flash(f"New {response_type} added for the keyword '{keyword}' ({abbreviation}) in age group {age}", 'success')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
