
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route('/')
def contact_form():
    return render_template('contact.html')


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
        # (using Markup.escape for HTML escaping)
        def sanitize(input_str):
            return Markup.escape(input_str)
        
        first_name = sanitize(first_name)
        last_name = sanitize(last_name)
        email = sanitize(email)
        message = sanitize(message)
        
        
        # If errors exist, return to the form with error messages
        if errors:
            return render_template('contact.html', errors=errors,
                                   first_name=first_name, last_name=last_name,
                                   email=email, country=country, message=message)


        # If all validations pass, prepare a thank you message
        subject_list = []
        if subject_repair:
            subject_list.append("Repair")
        if subject_order:
            subject_list.append("Order")
        if subject_others:
            subject_list.append("Others")

        # Prepare feedback message
        feedback = f"Thank you for contacting us!\n\n"
        feedback += f"Name: {first_name} {last_name}\n"
        feedback += f"Email: {email}\n"
        feedback += f"Country: {country}\n"
        feedback += f"Gender: {gender}\n"
        feedback += f"Subjects: {', '.join(subject_list)}\n"
        feedback += f"Message:\n{message}"


        # Return a thank you message to the user
        return feedback.replace("\n", "<br>")

if __name__ == '__main__':
    app.run(debug=True)
