import pickle
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Load the model
par_loaded_model = pickle.load(open('D:/anaconda/par_model.sav', 'rb'))

def lon_pred(par_input):
    par_input_as_numpy_array = np.asarray(par_input)
    par_input_reshaped = par_input_as_numpy_array.reshape(1, -1)
    scaler = StandardScaler()
    par_std = scaler.fit_transform(par_input_reshaped)
    par_pred = par_loaded_model.predict(par_std)
    print(par_pred)

    if par_pred[0] == 0:
        return "The Person does not have Parkinson's Disease"
    else:
        return "The Person has Parkinson's Disease"

def main():
    st.title('Parkinsons Disease Prediction Web App')

    Fo = st.text_input('Fo')
    Fhi = st.text_input('Fhi')
    Flo = st.text_input('Flo')
    Jitter_per = st.text_input('Jitter_per')
    Jitter_Abs = st.text_input('Jitter_Abs')
    RAP = st.text_input('RAP')
    PPQ = st.text_input('PPQ')
    Jitter_DDP = st.text_input('Jitter_DDP')
    Shimmer = st.text_input('Shimmer')
    Shimmer_dB = st.text_input('Shimmer_dB')
    Shimmer_APQ3 = st.text_input('Shimmer_APQ3')
    Shimmer_APQ5 = st.text_input('Shimmer_APQ5')
    APQ = st.text_input('APQ')
    Shimmer_DDA = st.text_input('Shimmer_DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    status = ''

    if st.button('Submit'):
        par_input = [float(Fo), float(Fhi), float(Flo), float(Jitter_per), float(Jitter_Abs), float(RAP), float(PPQ), float(Jitter_DDP), float(Shimmer), float(Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), float(APQ), float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]
        status = lon_pred(par_input)

    st.success(status)

if __name__ == "__main__":
    main()
