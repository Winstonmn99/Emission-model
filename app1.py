import pickle
import streamlit as st

pickle_in = open('Final_real_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs
def prediction(BSFC,NOx,SO2,PM10,PM25,VOC,CO,PAH):

     prediction = classifier.predict( [[BSFC,NOx,SO2,PM10,PM25,VOC,CO,PAH]])
     print(prediction)
     return prediction


def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:black;text-align:center;">Predictive Modelling of Ship Carbon Emission using Machine Learning</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # following lines create boxes in which user can enter data required to make prediction
    BSFC = st.number_input('Fuel consumed')
    NOx = st.number_input('NOx')
    SO2 = st.number_input("SO2")
    PM10 = st.number_input("PM 10")
    PM25 = st.number_input("PM 2.5")
    VOC = st.number_input("Volatile Organic Compound")
    CO = st.number_input("Carbon-monoxide")
    PAH = st.number_input("Polycyclic Auromatic Hydrocarcon")
    result =""


    if st.button("Predict"):
        result = prediction(BSFC,NOx,SO2,PM10,PM25,VOC,CO,PAH)
        st.success('The Carbon Emission is {}kiloton'.format(result))
        print(result)
    if st.button("About"):
        st.success("Final year Engineering project work")
        st.success("Developed by: Sheryl Austin")

if __name__=='__main__':
    main()
