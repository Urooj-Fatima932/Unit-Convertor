import streamlit as st

# Function to perform unit conversion
def unit_conversion(value, unit_from, unit_to):
    conversions = {
        # Length Conversions
        "meters_kilometers": 0.001,
        "meters_miles": 0.000621371,
        "meters_nanometers": 1000000000,
        "meters_micrometers": 1000000,
        "meters_millimeters": 1000,
        "meters_centimeters": 100,
        "kilometers_meters": 1000,
        "nanometers_meters": 0.000000001,
        "micrometers_meters": 0.000001,
        "millimeters_meters": 0.001,
        "centimeters_meters": 0.01,
        "miles_meters": 1609.34,

        # Weight Conversions
        "kilograms_grams": 1000,
        "grams_kilograms": 0.001
    }

    # Temperature Conversion Requires Formulas
    if unit_from == "celsius" and unit_to == "fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "fahrenheit" and unit_to == "celsius":
        return (value - 32) * 5/9
    elif unit_from == "celsius" and unit_to == "kelvin":
        return value + 273.15
    elif unit_from == "kelvin" and unit_to == "celsius":
        return value - 273.15
    elif unit_from == "fahrenheit" and unit_to == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif unit_from == "kelvin" and unit_to == "fahrenheit":
        return (value - 273.15) * 9/5 + 32

    # Check if direct conversion exists in dictionary
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    
    return "Conversion not supported"

# Streamlit UI
st.title("🎯Unit Converter")

# Choose the category of conversion
quantity = st.selectbox("Choose a category:", ["📏Length", "⚖️Weight", "🌡️Temperature"])
value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)

# Select units based on category
if quantity == "📏Length":
    unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "nanometers", "micrometers", "millimeters", "centimeters", "miles"])
    unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "nanometers", "micrometers", "millimeters", "centimeters", "miles"])
elif quantity == "⚖️Weight":
    unit_from = st.selectbox("Convert from:", ["kilograms", "grams"])
    unit_to = st.selectbox("Convert to:", ["kilograms", "grams"])
elif quantity == "🌡️Temperature":
    unit_from = st.selectbox("Convert from:", ["celsius", "fahrenheit", "kelvin"])
    unit_to = st.selectbox("Convert to:", ["celsius", "fahrenheit", "kelvin"])

# Button to trigger conversion
if st.button("🔄 Convert"):
    result = unit_conversion(value, unit_from, unit_to)
    if result == "Conversion not supported":
        st.error("Conversion not supported")
    else:
        st.success(f"The converted value is: **{result} {unit_to}**")



