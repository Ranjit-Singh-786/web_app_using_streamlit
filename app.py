import streamlit as st
import joblib
import numpy as np

model = joblib.load('updated_model.lb')

def get_predict(model, test_point):
    prediction = model.predict(test_point)
    output = str(prediction[0])
    return output

st.title("Old Bikes Price Prediction App.")
st.subheader("Get a prediction for your old bike's price")

# get brand as a input
brand_list = ['Royal Enfield', 'KTM', 'Bajaj', 'Harley', 'Yamaha', 'Honda', 'Suzuki', 'TVS', 'Kawasaki', 'Hyosung', 'Benelli', 'Mahindra', 'Triumph', 'Ducati', 'BMW']
brand = st.selectbox("Choose your brand", brand_list)
brand_encode = {'Royal Enfield':1,'KTM':2,'Bajaj':3,'Harley':4,'Yamaha':5,'Honda':6,'Suzuki':7,'TVS':8,'Kawasaki':9,'Hyosung':10,'Benelli':11,'Mahindra':12,'Triumph':13,'Ducati':14,'BMW':15}
brand = brand_encode[brand]

owner_list = ["First Owner","Second Owner","Third Owner","Fourth Owner Or More"]
owner = st.selectbox("OwnerShip", owner_list)
dic={'First Owner':1,'Second Owner':2,'Third Owner':3,'Fourth Owner Or More':4}
owner= dic[owner]

kms_driven = st.number_input("Kilometers driven", min_value=0, step=1)

age = st.number_input("Age", min_value=0, step=1,max_value=15)
power = st.number_input("Power of bike", min_value=0, step=1,max_value=700)


submit = st.button('Get Price')

if submit:
    test_point = [[kms_driven, owner, age, power, brand]]
    test_point = np.array(test_point)
    output = get_predict(model, test_point)
    st.write("Your Price is here :")
    st.success(f"The predicted price for your old bike is: {output}")





