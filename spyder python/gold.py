import pickle
import numpy as np
import streamlit as st

# Load the model
gold = pickle.load(open('D:/anaconda/gold_model.sav', 'rb'))

def gld_pred(input_data):
    input_np = np.asarray(input_data).reshape(1, -1)
    prediction = gold.predict(input_np)
    return prediction[0]

def main():
    st.title('Gold Price Prediction Web App')
    
    spx = st.text_input('S&P 500 Index (SPX)')
    uso = st.text_input('United States Oil Fund (USO)')
    slv = st.text_input('iShares Silver Trust (SLV)')
    eur_usd = st.text_input('EUR/USD Exchange Rate')
    
    target = ''
    
    if st.button('Predict GLD Price'):
        try:
            input_data = [float(spx), float(uso), float(slv), float(eur_usd)]
            target = gld_pred(input_data)
            st.success(f'The predicted GLD price is: {target:.2f}')
        except ValueError:
            st.error('Please enter valid numerical values for all fields.')
        except Exception as e:
            st.error(f'An error occurred: {e}')
    
if __name__ == "__main__":
    main()
