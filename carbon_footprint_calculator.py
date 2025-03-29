from flask import Flask, render_template, request, send_from_directory
import os
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    user="root",
    password="admin",
    database="CarbonCalc"
)

cursor = db.cursor()

def get_carbon_emission_factor(activity):
    emission_factors = {
        'food': 12.5,        # Example value (2.5 kg CO2 per kWh)
        'electricity': 0.6, # Example value (0.6 kg CO2 per kWh)
        'travel': 2.0,      # Example value (2.0 kg CO2 per kWh)
        'services': 1.2,    # Example value (1.2 kg CO2 per kWh)
        # Add other activities and their emission factors as needed
    }

    return emission_factors.get(activity, 0.0)  # Return the emission factor or 0.0 if activity not found

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get form data
    activity = request.form['activity']
    energy_used = float(request.form['energy_used'])

    # Calculate carbon footprint based on activity and energy_used
    carbon_emission_factor = get_carbon_emission_factor(activity) 
    carbon_footprint = energy_used * carbon_emission_factor

    # Store data in the MySQL database
    query = "INSERT INTO carbon_footprints (activity, energy_used, carbon_footprint) VALUES (%s, %s, %s)"
    data = (activity, energy_used, carbon_footprint)
    cursor.execute(query, data)
    db.commit()

    return "Success"  # Return a success message or redirect to a result page

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = app.root_path
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)
