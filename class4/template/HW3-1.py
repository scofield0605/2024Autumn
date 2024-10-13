from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the form
@app.route('/investigation', methods=['GET'])
def investigate():
    return render_template('spring_class3.html')

# Route to handle form submission and display the result
@app.route('/submit', methods=['POST'])
def invest_submit():
    # Extract form data from the request
    name = request.values.get('name')
    email = request.values.get('email')
    comments = request.values.get('comments')
    birthday = request.values.get('birthday')
    technology = request.values.get('tech')

    # Print all form data (for debugging purposes)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Comments: {comments}")
    print(f"Birthday: {birthday}")
    print(f"Technology: {technology}")
    
    # Render the result page with form data
    return render_template('submit.html', name=name, email=email, comments=comments, birthday=birthday, technology=technology)

app.run()
    
