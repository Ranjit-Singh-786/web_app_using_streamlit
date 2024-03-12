## Get prediction by machine learning model

import joblib
import warnings
warnings.filterwarnings('ignore')
import sklearn 
print(sklearn.__version__)


model = joblib.load('updated_model.lb')

def get_predict(model, test_point):
    prediction = model.predict(test_point)
    output = str(prediction[0])
    return output
test_point = [[2500, 2, 5, 125, 2]]

pred = get_predict(model=model,test_point=test_point)
print(pred)