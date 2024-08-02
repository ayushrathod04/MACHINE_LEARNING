# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:50:17 2024

@author: ayush
"""

import pickle
import numpy as np
import streamlit as st

# Load the model (ensure the correct path)
loaded_model = pickle.load(open('D:/anaconda/aps_model.sav', 'rb'))

def aps_pred(input_data):
    input_np = np.asarray(input_data)
    input_reshaped = input_np.reshape(1, -1)
    prediction = loaded_model.predict(input_reshaped)
    if prediction[0] == 0:
        return 'neutral or dissatisfied'
    else:
        return 'satisfied'

def main():
    st.title('Satisfaction Prediction Web App')

    # Collect user input
    Gender = st.text_input('Gender (0 for Male, 1 for Female)')
    ct = st.text_input('Customer Type (0 for Loyal, 1 for Disloyal)')
    age = st.text_input('Age')
    tot = st.text_input('Type of Travel (0 for Personal, 1 for Business)')
    Class = st.text_input('Class (0 for Eco, 1 for Eco Plus, 2 for Business)')
    fd = st.text_input('Flight Distance')
    iws = st.text_input('Inflight WiFi Service (0 to 5)')
    dtc = st.text_input('Departure/Arrival Time Convenient (0 to 5)')
    eob = st.text_input('Ease of Online Booking (0 to 5)')
    gl = st.text_input('Gate Location (0 to 5)')
    fad = st.text_input('Food and Drink (0 to 5)')
    ob = st.text_input('Online Boarding (0 to 5)')
    sc = st.text_input('Seat Comfort (0 to 5)')
    ie = st.text_input('Inflight Entertainment (0 to 5)')
    obs = st.text_input('On-board Service (0 to 5)')
    lrs = st.text_input('Leg Room Service (0 to 5)')
    bh = st.text_input('Baggage Handling (0 to 5)')
    cs = st.text_input('Check-in Service (0 to 5)')
    ise = st.text_input('Inflight Service (0 to 5)')
    Cleanliness = st.text_input('Cleanliness (0 to 5)')
    ddm = st.text_input('Departure Delay in Minutes')
    adm = st.text_input('Arrival Delay in Minutes')

    satisfaction = ''

    if st.button('Get Satisfaction Result'):
        try:
            input_data = [int(Gender), int(ct), int(age), int(tot), int(Class), int(fd), int(iws), int(dtc),
                          int(eob), int(gl), int(fad), int(ob), int(sc), int(ie), int(obs), int(lrs),
                          int(bh), int(cs), int(ise), int(Cleanliness), int(ddm), float(adm)]
            satisfaction = aps_pred(input_data)
            st.success(satisfaction)
        except ValueError:
            st.error('Please enter valid inputs for all fields.')

if __name__ == "__main__":
    main()
