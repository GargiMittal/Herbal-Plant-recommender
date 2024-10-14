from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_state_soil_data():
    state_soil_map = {}
    with open('states_soil.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            state_soil_map[row['State']] = row['Common Soil Type']
    return state_soil_map

def load_herbal_plant_data():
    soil_plant_map = {}
    with open('herbal_plants_soil.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            soil_plant_map[row['Soil Type']] = [
                row['Herbal Plant 1'], row['Herbal Plant 2'], row['Herbal Plant 3'], row['Herbal Plant 4'], row['Herbal Plant 5']
            ]
    return soil_plant_map

def load_plant_info():
    plant_info_map = {}
    with open('herbal_plants_info.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            plant_info_map[row['Herbal Plant']] = {
                'Scientific Name': row['Scientific Name'],
                'Uses': row['Uses'],
                'Description': row['Description'],
                'Growing Conditions': row['Growing Conditions']
            }
    return plant_info_map

state_soil_map = load_state_soil_data()
herbal_plant_map = load_herbal_plant_data()
plant_info_map = load_plant_info()


@app.route('/')
def index():
    states = list(state_soil_map.keys())
    soils = list(herbal_plant_map.keys())
    return render_template('index.html', states=states, soils=soils)

@app.route('/recommend', methods=['POST'])
def recommend():
    state = request.form.get('state')
    soil_type = request.form.get('soil_type')

    if not soil_type:
        soil_type = state_soil_map.get(state)

    plants = herbal_plant_map.get(soil_type, [])

    return render_template('results.html', plants=plants, soil_type=soil_type, state=state)

@app.route('/plant/<plant_name>')
def plant_details(plant_name):
    plant_info = plant_info_map.get(plant_name, {})
    return render_template('plant_details.html', plant_name=plant_name, plant_info=plant_info)


if __name__ == '_main_':
    app.run(debug=True)