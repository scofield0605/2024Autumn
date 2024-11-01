from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session handling

# Dictionary mapping employee IDs to names
member_dictionary = {'1': 'Amy', '2': 'Bob', '3': 'John'}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    account = request.form.get('account')
    password = request.form.get('password')
    employee_id = request.form.get('employee_id')

    # Check if admin credentials are correct
    if account == 'admin' and password == '123456':
        # Verify if the employee_id exists in member_dictionary
        admin_name = member_dictionary[employee_id]

        session['name'] = admin_name
        return redirect(url_for('profile'))
    elif employee_id != member_dictionary[employee_id] :
        flash("You are not an admin!")
        return redirect(url_for('index'))
    

app.run()