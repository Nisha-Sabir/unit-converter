
import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return None
    
    value_in_meters = value / conversion_factors[from_unit]
    converted_value = value_in_meters * conversion_factors[to_unit]
    return converted_value

st.title("🔢 Unit Converter")
st.subheader("Convert Length Units")

# Input Fields
value = st.number_input("Enter Value", min_value=0.0, value=1.0, step=0.1)
from_unit = st.selectbox("From Unit", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"])
to_unit = st.selectbox("To Unit", ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"])

# Convert Button
if st.button("Convert"):
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
