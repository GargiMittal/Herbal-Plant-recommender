
# Herbal Plant Recommender

### Overview
Herbal Plant Recommender is a Python Flask-based web application that helps users discover suitable herbal plants for their homes or gardens based on their Indian state and the prevalent soil type. The system promotes Ayurveda by suggesting plants that can thrive in the user's region, contributing to a healthier lifestyle and environment.

### Features
- **State Selection**: Users can select their Indian state from a dropdown menu.
- **Soil Type Recommendation**: Based on the selected state, the system identifies the most common soil type.
- **Herbal Plant Suggestions**: Recommends herbal plants suited to the selected soil type and region.
- **Promotes Ayurveda**: Encourages the cultivation of medicinal and herbal plants, fostering traditional health practices.
  
### Technologies Used
- **Python**: The core programming language used for application development.
- **Flask**: A lightweight web framework for building the backend of the application.
- **CSV Files**: The dataset containing information about Indian states, soil types, and plant recommendations is stored in CSV format for easy access and scalability.
  
### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/herbal-plant-recommender.git
   cd herbal-plant-recommender
   ```

2. **Install the required packages**:
   Ensure you have Python installed, then install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access the web app**:
   Open a browser and navigate to `http://127.0.0.1:5000/`.

### How to Use
1. Select your Indian state from the dropdown menu.
2. The application will automatically identify the prevalent soil type in your state.
3. Based on this, it will recommend a list of herbal plants you can grow in your home or garden.
4. Browse through the list and start your herbal garden to promote Ayurveda!

### Data Source
The dataset used for state-soil-plant mapping is stored in CSV files. The data includes:
- Indian States
- Soil types prevalent in each state
- Herbal plants suitable for each soil type

### Future Enhancements
- **User Profiles**: Allow users to save their preferences and past recommendations.
- **Plant Care Tips**: Provide detailed information on how to grow and care for each recommended plant.
- **Soil Testing Integration**: Option for users to manually input their soil characteristics for more tailored recommendations.

### Contribution
If you'd like to contribute to this project, feel free to fork the repository and create pull requests. Contributions are welcome!


