
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
import re


app = Flask(__name__)


@app.route('/')
def contact_form():
    return render_template('contact.html')


# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    subject = db.Column(db.String(50), nullable=False)



@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        country = request.form['country']
        message = request.form['message']
        gender = request.form['gender']
        subject_repair = 'Repair' in request.form
        subject_order = 'Order' in request.form
        subject_others = 'Others' in request.form
        
        # Honeypot implementation to detect spam
        honeypot = request.form.get('honeypot')
        if honeypot:
            return "Spam detected!"

        # Server-side validation to ensure inputs are correct
        errors = []
        if not first_name:
            errors.append("First name is required.")
        if not last_name:
            errors.append("Last name is required.")
        if not email:
            errors.append("Email is required.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email address.")
        if not country:
            errors.append("Country is required.")
        if not message:
            errors.append("Message is required.")
        if not gender:
            errors.append("Gender is required.")
        if not (subject_repair or subject_order or subject_others):
            errors.append("Please select at least one subject.")
            
            
        # Sanitize input to neutralize harmful encoding 
        # (using escape to escape HTML content)
        def sanitize(input_str):
            return escape(input_str)
        
        first_name = sanitize(first_name)
        last_name = sanitize(last_name)
        email = sanitize(email)
        message = sanitize(message)
        
        
        # If errors exist, return to the form with error messages
        if errors:
            return render_template('contact.html', errors=errors,
                                   first_name=first_name, last_name=last_name,
                                   email=email, country=country, message=message)


        # Convert selected subjects to a comma-separated string
        subject_list = []
        if subject_repair:
            subject_list.append("Repair")
        if subject_order:
            subject_list.append("Order")
        if subject_others:
            subject_list.append("Others")
            
        # Save to database
        new_contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            message=message,
            gender=gender,
            subjects=', '.join(subject)  # Convert list to string
        )
        db.session.add(new_contact)
        db.session.commit()
        

        # Prepare feedback message
        feedback = f"Thank you for contacting us!\n\n"
        feedback += f"Name: {first_name} {last_name}\n"
        feedback += f"Email: {email}\n"
        feedback += f"Country: {country}\n"
        feedback += f"Gender: {gender}\n"
        feedback += f"Subjects: {subjects}\n"
        feedback += f"Message:\n{message}"

        # Return a thank you message to the user
        return render_template('thank_you.html', feedback=feedback)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
