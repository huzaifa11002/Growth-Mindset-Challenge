import streamlit as st


if "history" not in st.session_state:
    st.session_state.history = []

st.title("Unit Converter App")
selectConvert= st.selectbox('Choose the Convertor',('Foot','Meter','Centimeter','Kilometer','Inch'))
if selectConvert =="Foot":
    selectConverted= st.selectbox('Convert into:',('Meter','Centimeter' ,'Kilometer','Inch'))
    if selectConverted == "Meter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 0.3048
    elif selectConverted == "Centimeter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 30.48
    elif selectConverted == "Kilometer":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 0.0003048
    else:
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 12
elif selectConvert =="Meter":
    selectConverted= st.selectbox('Convert into:',('Foot','Centimeter' ,'Kilometer','Inch'))
    if selectConverted == "Foot":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 0.3048
    elif selectConverted == "Centimeter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 100
    elif selectConverted == "Kilometer":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 0.001
    else:
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 39.3701
elif selectConvert =="Centimeter":
    selectConverted= st.selectbox('Convert into:',('Foot','Meter','Kilometer','Inch'))
    if selectConverted == "Foot":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 30.48
    elif selectConverted == "Meter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 100
    elif selectConverted == "Kilometer":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 100000
    else:
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 2.54
elif selectConvert =="Kilometer":
    selectConverted= st.selectbox('Convert into:',('Foot','Meter','Centimeter','Inch'))
    if selectConverted == "Foot":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 0.0003048
    elif selectConverted == "Meter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 0.001
    elif selectConverted == "Centimeter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 100000
    else:
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 39370.1
else:
    selectConverted= st.selectbox('Convert into:',('Foot','Meter','Centimeter','Kilometer'))
    if selectConverted == "Foot":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 12
    elif selectConverted == "Meter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 39.3701
    elif selectConverted == "Centimeter":
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput * 2.54
    else:
        userInput = st.number_input('Enter your value', step=0.1)
        valueAnswer = userInput / 39370.1

if st.button('Convert', key='convertor'):
    st.success(f'Your converted value answer is {valueAnswer:.2f} {selectConverted}')

    st.session_state.history.append(f"{userInput:.2f} {selectConvert} = {valueAnswer:.2f} {selectConverted}")


st.markdown("---")

col1, col2 = st.columns([4,1])

with col1:
    st.header("History")
with col2:
    if st.button("Clear History"):
        st.session_state.history = []

if len(st.session_state.history) == 0:
    st.write("No history yet.")
else:
    for item in st.session_state.history:
        st.warning(item)
