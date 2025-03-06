import streamlit as st 
import random

# Page Config

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

# Sidebar
st.sidebar.header("What do you want to perform")
page = st.sidebar.radio("Select:", ["Number Guessing Game", "Calculator", "BMI Calculator" , "Word Counter"])



# Number Guessing Game Page

if page == "Number Guessing Game":
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
            st.write("Try again!")
        elif guess < st.session_state.guessed:
            st.warning("You guessed too low!")
            st.write("Try again!")
        else:
            st.subheader("Congratulations! You guessed it right!")
            st.balloons()
            st.write(f"It took you {st.session_state.attempt} attempts.")
            st.session_state.result.append(f"Your Guessed number is {guess}. After {st.session_state.attempt} attempts")
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

    col1, col2 = st.columns([4,1])
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
    st.title('BMI Calculator 📱')
    st.write('This is a simple BMI calculator')

    weight = st.number_input('Enter your weight (in kg)', step=0.1)
    height = st.number_input('Enter your height (in m)', step=0.1)

    if st.button('Calculate BMI', key='bmi'):
        if weight == 0 or height == 0:
            st.write('Please enter valid values')
        else:
            bmi = weight / (height**2)
            st.write(f'Your BMI is {bmi:.2f}')
            st.session_state.bmiCalculatorHistory.append(f'Your BMI is {bmi:.2f}')
        if bmi < 18.5:
            st.write('You are underweight')
        elif bmi >= 18.5 and bmi < 25:
            st.write('You are normal weight')
        elif bmi >= 25 and bmi < 30:
            st.write('You are overweight')
        else:
            st.write('You are obese')

# Word Counter Page

elif page == "Word Counter":

    st.title("Word Counter 📝")
    st.write("Count the number of words in a text")

    para = st.text_area("Enter your text here")
    if st.button("Count"):
        split_words = para.split()
        number_of_words = len(split_words)
        st.success(f"Total number of words: {number_of_words}")