import pickle
from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# The original code likely loaded the models from the wrong files.
# We are swapping the file paths to match the intended variable names.
# 'models/scaler.pkl' should contain the scaler object.
# 'models/lassoCV_regression.pkl' should contain the LassoCV regression model.
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))
lassoCV_model = pickle.load(open('models/lassoCV_regression.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictprice',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Open_val = float(request.form.get('Open'))
        Volume_val = float(request.form.get('Volume'))

        # The correct object (standard_scaler) is now called to transform the data.
        new_scaled_data = standard_scaler.transform([[Open_val,Volume_val]])
        result = lassoCV_model.predict(new_scaled_data)
        
        return render_template('predict.html',results=result[0])
    else:
        return render_template('predict.html')

    

if __name__=="__main__":
    app.run(host="0.0.0.0")
