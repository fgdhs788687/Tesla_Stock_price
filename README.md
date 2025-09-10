# Tesla Stock Price Predictor API
A Flask-based web application and machine learning pipeline for predicting Tesla stock prices. This project demonstrates a complete end-to-end workflow from data preprocessing to model deployment.

# 🏛️ Project Architecture
This project is structured as a two-part system: a machine learning pipeline and a RESTful API.
1. Data & Modeling Pipeline: The tesla_eda_fe.ipynb and model_training.ipynb notebooks detail the process of cleaning raw stock data, engineering new features, and training a LassoCV regression model.
   The trained model and data scaler are persisted using Python's pickle library.
2. API & Web Server: The application.py Flask server exposes an endpoint (/predictprice) that accepts stock data, preprocesses it using the saved scaler, and returns a prediction from the saved model.
   
# ⚙️ Environment Setup
To get this project running locally, ensure you have Python 3.8+ installed.
- Clone the Repository:
  git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
  cd your-repo-name
  
- Install Dependencies:
  pip install -r requirements.txt
  
- Run the Flask Server:     
  python application.py
The application will launch on your local machine, accessible at http://127.0.0.1:5000/.

# Repository Contents
- application.py: The Flask application.
- models/: Persisted machine learning assets (.pkl files).
- templates/: HTML front-end files (.html files).
- data/: Raw and processed datasets (.csv files).
- requirements.txt: Python dependencies.
- tesla_eda_fe.ipynb: Data cleaning and EDA notebook.
- model_training.ipynb: Model training and evaluation notebook.

# 🤝 Contribution
Contributions are welcome! If you find a bug or have an improvement, please open an issue or submit a pull request.
