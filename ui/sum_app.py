import streamlit as st
import requests

st.title("Add to Number via FastAPI")

# User input
num = st.number_input("Enter a number", step=1)

# Button
if st.button("Add via FastAPI"):
    response = requests.post("http://fastapi-app:8000/add", json={"value": num})
    if response.status_code == 200:
        result = response.json()
        st.success(f"{result['input']} + 10 = {result['result']}")
    else:
        st.error("Something went wrong!")
