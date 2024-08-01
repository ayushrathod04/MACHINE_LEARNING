# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

loaded_model = pickle.load(open("D:/anaconda/trained_model.sav",'rb'))

input_data = (7,160,54,32,175,30.5,0.588,39)

input_data_np = np.asarray(input_data)

input_reshape = input_data_np.reshape(1,-1)

pred = loaded_model.predict(input_reshape)
print(pred)

if pred[0] == 0:
  print('Person is non-diabetic')
else:
  print('Person is diabetic')