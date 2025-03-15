
import streamlit as st
# Set the title of the app
st.title("BMI Calculator")

# Input fields for user data
weight = st.number_input("Enter your weight in kilograms", value=70.0)
height = st.number_input("Enter your height in meters", value=1.75)

# Perform calculation only if height is greater than 0 to avoid division errors
if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
    
    # Provide a simple interpretation based on BMI
    if bmi < 18.5:
        st.write("You are underweight.")
    elif bmi < 25:
        st.write("You have a normal weight.")
    elif bmi < 30:
        st.write("You are overweight.")
    else:
        st.write("You are in the obese category.")
