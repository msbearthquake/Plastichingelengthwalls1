import   streamlit  as st; from PIL import Image; import numpy  as np
from  sklearn.ensemble   import   RandomForestRegressor
import pandas  as pd; import pickle

import os

dirname = os.path.dirname(__file__)
filename1 = os.path.join(dirname, 'Capture1.png')
filename2 = os.path.join(dirname, 'Capture2.png')


st.title('Plastic hinge length of reinforced concrete structural walls (RCSWs) ')
with st.container():
    image1 = Image.open(filename1)
    image2 = Image.open(filename2)

    st.image(image1)
    st.image(image2)

SCR1 = st.number_input('Insert secondary cracking ratio:',0.0)
WL1 = st.number_input('Insert wall length (m):',0.0)
HE1 = st.number_input('Insert wall effective height (m):',0.0)
ALR1 = st.number_input('Insert axial load ratio:',0.0)
SSP1 = st.number_input('Insert shear stress variable:',0.0)
WL2 = WL1*1000.0; HE2 = HE1*1000.0;
inputvec = np.array([SCR1, WL2, HE2, ALR1, SSP1])


filename3 = os.path.join(dirname, 'finalized_model.sav')
### save the model to disk
# pickle.dump(model, open(filename, 'wb'))
 
### some time later...
### load the model from disk


with st.container():

    if st.button('Run'):
        if WL2!=0 and HE2!=0:
            loaded_model = pickle.load(open(filename3, 'rb'))

            # trainx1 = pd.read_excel('./trainx.xlsx')
            # trainy1 = pd.read_excel('./trainy.xlsx')
            # trainy = trainy1['PHL']
            # trainx = trainx1.iloc[:,6:11]
            # model = RandomForestRegressor (n_estimators  = 180  , max_features= 5, max_depth= 12, min_samples_split = 2, min_samples_leaf = 1 )
            # model.fit(trainx, trainy)
            # yhat1 = model.predict(inputvec.reshape(1, -1))
            yhat1 = loaded_model.predict(inputvec.reshape(1, -1))
            st.write("Plastic hinge length is: " , round(yhat1[0]/1000.0, 4), "m")
        else:
            st.write("Secondary cracking ratio, wall length and wall effective height should not be zero.")

# st.write(trainx)

filename4 = os.path.join(dirname, 'Capture3.png')
filename5 = os.path.join(dirname, 'Capture4.png')
st.header("Developers:")
with st.container():
    image3 = Image.open(filename4)
    image4 = Image.open(filename5)

    st.image(image3)
    st.image(image4)