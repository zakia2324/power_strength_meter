import streamlit as st
import re

# Password Strength Function
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Medium"
    elif not re.search("[0-9]", password):
        return "Strong"
    elif not re.search("[!@#$%^&*()]", password):
        return "Very Strong"
    return "Very Strong"

# Streamlit App
st.title("Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"Password Strength: {strength}")
else:
    st.write("Please enter a password to check its strength.")
