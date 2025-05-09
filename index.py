import streamlit as st
import pandas as pd
import os
from io import BytesIO 
import random

# Page Config

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

# Sidebar
st.sidebar.header("What do you want to perform")
page = st.sidebar.radio("Select:", ["Data Filter", "Number Guessing Game", "Calculator", "BMI Calculator" , "Word Counter"])

if page == "Data Filter":
    st.title("Data Filter and File Sweeper 📊")
    st.write("This is a simple data filter application")
    upload_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"] , accept_multiple_files=False)

    if upload_file:
        file_ext = os.path.splitext(upload_file.name)[-1]
        if file_ext == ".csv":
            st.success("Your CSV file uploaded successfully")
            df = pd.read_csv(upload_file)
        elif file_ext == ".xlsx":
            st.success("Your Excel file uploaded successfully")
            df = pd.read_excel(upload_file, engine='openpyxl')
        else:
            st.error(f"Unsupported file format {file_ext}")
        
        st.write(f"Filename: {upload_file.name}")
        st.write(f"File Size: {upload_file.size/1024:.2f} KB")

        st.write("Preview of the data")
        st.dataframe(df.head())

        st.subheader("Analysis of the data")
        filter_checkbox = st.checkbox("Filter the data")
        convert_checkbox = st.checkbox("Convert the data file into another format")

        if filter_checkbox and convert_checkbox:
            st.warning("Please select only one option")
            st.stop()

        elif filter_checkbox:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Remove Dupicates from the data"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed successfully")
            with col2:
                if st.button("Fill Missing Values"):
                    df.fillna(0, inplace=True)
                    st.success("Missing values filled successfully")

            st.subheader("Filter the data")
            columns = st.multiselect(f"Choose the columns to filter", df.columns, default=df.columns)
            df = df[columns]
            st.subheader("Filtered Data Preview")
            st.dataframe(df)

            select_ext = st.selectbox("Select the file format", ["CSV", "Excel"])
                
            buffer = BytesIO()
            if st.button(f"Convert into {select_ext} file"):
                if select_ext == "CSV":        
                    df.to_csv(buffer, index=False)
                    file_name = upload_file.name.replace(file_ext,".csv")
                    mime_type = "text/csv"
                    buffer.seek(0)
                    st.download_button(label="Download CSV", data=buffer, file_name=file_name, mime=mime_type)
                
                else:
                    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Sheet1')
                        buffer.seek(0)
                        file_name = upload_file.name.replace(file_ext,".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        st.download_button(label="Download Excel", data=buffer, file_name=file_name, mime=mime_type)

        elif convert_checkbox:
            col1,col2 = st.columns(2)
            with col1:
                select_ext = st.selectbox("Select the file format", ["CSV", "Excel"])
                
            buffer = BytesIO()
            if st.button(f"Convert into {select_ext} file"):
                if select_ext == "CSV":        
                    df.to_csv(buffer, index=False)
                    file_name = upload_file.name.replace(file_ext,".csv")
                    mime_type = "text/csv"
                    buffer.seek(0)
                    st.download_button(label="Download CSV", data=buffer, file_name=file_name, mime=mime_type)
                
                else:
                    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Sheet1')
                        buffer.seek(0)
                        file_name = upload_file.name.replace(file_ext,".xlsx")
                        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        st.download_button(label="Download Excel", data=buffer, file_name=file_name, mime=mime_type)


# Number Guessing Game Page

elif page == "Number Guessing Game":
    st.title("Number Guessing Game 🤷‍♂️")
    st.write("Guess a number between 1 and 10")

    if "guessed" not in st.session_state:
        st.session_state.guessed = random.randint(1, 10)
        st.session_state.attempt = 0
        st.session_state.result = []

    guess = st.number_input("Enter your guessed number", min_value=1, max_value=10, step=1)
    
    if st.button("Check"):
        st.session_state.attempt += 1
        if guess > st.session_state.guessed:
            st.warning("You guessed too high!")
            st.write("Try again! ☹")
        elif guess < st.session_state.guessed:
            st.warning("You guessed too low!")
            st.write("Try again! ☹")
        else:
            st.subheader("Congratulations! You guessed it right! 🎉🎊")
            st.balloons()
            st.write(f"It took you {st.session_state.attempt} attempts.")
            st.session_state.result.append(f"Your Guessed number is {guess}. You got it after {st.session_state.attempt} attempts")
            st.session_state.guessed = random.randint(1, 10)
            st.session_state.attempt = 0
    
    st.markdown("---")
    st.subheader("Game History")
    if len(st.session_state.result) == 0:
        st.write("No game played yet")
    else:
        for res in st.session_state.result:
            st.write(res)

# Calculator Page

elif page == "Calculator":
    if "calculatorHistory" not in st.session_state:
        st.session_state.calculatorHistory = []
    st.title("Calculator 🖩")
    st.write("Perform basic arithmetic operations")
    first_input = st.number_input("Enter the first number", step=1)
    second_input = st.number_input("Enter the second number", step=1)
    operation = st.selectbox("Select the operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        if operation == "Addition":
            result = first_input + second_input
            st.success(f"Anwser is {result}")
            st.session_state.calculatorHistory.append(f"{first_input} + {second_input} = {result}")
        elif operation == "Subtraction":
            result = first_input - second_input
            st.success(f"Anwser is {result}")
            st.session_state.calculatorHistory.append(f"{first_input} - {second_input} = {result}")
        elif operation == "Multiplication":
            result = first_input * second_input
            st.success(f"Anwser is {result}")
            st.session_state.calculatorHistory.append(f"{first_input} * {second_input} = {result}")
        elif operation == "Division":
            if second_input == 0:
                st.error("Division by zero is not allowed")
            else:
                result = first_input / second_input
                st.success(f"Anwser is {result}")
                st.session_state.calculatorHistory.append(f"{first_input} / {second_input} = {result}")

    st.markdown("---")

    col1, col2= st.columns([4,1])
    with col1:
        st.subheader("Calculator History")
    with col2:
        if st.button("Clear History"):
            st.session_state.calculatorHistory = []

    if len(st.session_state.calculatorHistory) == 0:
        st.write("No calculations performed yet")
    else:
        for history in st.session_state.calculatorHistory:
            st.warning(history)

# BMI Calculator Page

elif page == "BMI Calculator" :
    if "bmiCalculatorHistory" not in st.session_state:
        st.session_state.bmiCalculatorHistory = []
    col1, col2 = st.columns([2,1])
    with col1:
        st.title('BMI Calculator 📱')
        st.write('This is a simple BMI calculator')
        weight = st.number_input('Enter your weight (in kg)', step=0.1)
        height = st.number_input('Enter your height (in m)', step=0.1)

        if st.button('Calculate BMI', key='bmi'):
            if weight == 0 or height == 0:
                st.error('Please enter valid values')
            else:
                bmi = weight / (height**2)
                st.write(f'Your BMI is {bmi:.2f}')
                st.session_state.bmiCalculatorHistory.append(f'Your BMI is {bmi:.2f}')
                if bmi < 18.5:
                    st.info('You are underweight')
                elif bmi >= 18.5 and bmi < 25:
                    st.balloons()
                    st.success('You are normal weight')
                elif bmi >= 25 and bmi < 30:
                    st.warning('You are overweight')
                else:
                    st.error('You are obese')
    with col2:
        st.subheader("Converter 🔁")
        st.write('This is a simple length converter')
        selectConvert = st.selectbox('Convert from:',('Foot','Meter','Centimeter'))
        if selectConvert =="Foot":
            selectConverted= st.selectbox('Convert into:',('Meter','Centimeter'))
            if selectConverted == "Meter":
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput / 3.281
            else:
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput * 30.48
        elif selectConvert =="Meter":
            selectConverted= st.selectbox('Convert into:',('Foot','Centimeter'))
            if selectConverted == "Foot":
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput * 3.281
            else:
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput * 100
        else:
            selectConverted= st.selectbox('Convert into:',('Foot','Meter'))
            if selectConverted == "Foot":
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput / 30.48
            else:
                userInput = st.number_input('Enter your value', step=0.1)
                valueAnswer = userInput / 100
        if st.button('Convert', key='convertor'):
            if userInput == 0:
                st.error('Please enter valid values')
            else:
                st.success(f'Your converted value answer is {valueAnswer:.2f} {selectConverted}')


# Word Counter Page

elif page == "Word Counter":

    st.title("Word Counter 📝")
    st.write("Count the number of words in a text")

    para = st.text_area("Enter your text here")
    if st.button("Count"):
        split_words = para.split()
        number_of_words = len(split_words)
        st.success(f"Total number of words: {number_of_words}")
