from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/investigation', methods=['GET'])
def investigate():
    return render_template('spring_class3.html')

@app.route('/submit', methods=['POST'])
def invest_submit():
    name = request.form.get('name')
    email = request.form.get('email')
    comments = request.form.get('comments')
    birthday = request.form.get('birthday')
    technology = request.form.get('tech')
    
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Comments: {comments}")
    print(f"Birthday: {birthday}")
    print(f"Technology: {technology}")
    
    # Render the result page with form data
    return render_template('submit.html', name=name, email=email, comments=comments, birthday=birthday, technology=technology)

app.run()