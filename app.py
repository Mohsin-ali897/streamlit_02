
import streamlit as st
import streamlit.components.v1 as components

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict[from_unit]:
        return value * conversion_dict[from_unit][to_unit]
    return None

def main():
    st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="centered")
    st.markdown("""
        <style>
            .stApp { background-color: #f8f9fa; }
            .title { text-align: center; font-size: 40px; font-weight: bold; color: #ffffff; padding: 15px; background: linear-gradient(90deg, #007bff, #6610f2); border-radius: 10px; }
            .stButton button { background-color: #007bff; color: white; border-radius: 10px; padding: 10px 20px; font-size: 16px; }
            .container { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); }
            .stAlert { font-size: 18px; font-weight: bold; text-align: center; background-color: #28a745; color: white; padding: 15px; border-radius: 8px; }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='title'>Unit Converter App</div>", unsafe_allow_html=True)
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    
    category = st.selectbox("Select a category", ["Length", "Weight", "Temperature", "Volume", "Speed"])
    
    if category == "Length":
        conversion_dict = {
            "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701},
            "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84, "Inches": 39370.1},
            "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280, "Inches": 63360},
            "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Inches": 12},
            "Inches": {"Meters": 0.0254, "Kilometers": 0.0000254, "Miles": 0.0000157828, "Feet": 0.0833333}
        }
    elif category == "Weight":
        conversion_dict = {
            "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
            "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
            "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
            "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625}
        }
    elif category == "Temperature":
        conversion_dict = {
            "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
            "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
            "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
        }
    elif category == "Volume":
        conversion_dict = {
            "Liters": {"Milliliters": 1000, "Cubic Meters": 0.001, "Gallons": 0.264172},
            "Milliliters": {"Liters": 0.001, "Cubic Meters": 0.000001, "Gallons": 0.000264172},
            "Cubic Meters": {"Liters": 1000, "Milliliters": 1000000, "Gallons": 264.172},
            "Gallons": {"Liters": 3.78541, "Milliliters": 3785.41, "Cubic Meters": 0.00378541}
        }
    elif category == "Speed":
        conversion_dict = {
            "Meters per second": {"Kilometers per hour": 3.6, "Miles per hour": 2.23694},
            "Kilometers per hour": {"Meters per second": 0.277778, "Miles per hour": 0.621371},
            "Miles per hour": {"Meters per second": 0.44704, "Kilometers per hour": 1.60934}
        }
    
    from_unit = st.selectbox("From Unit", list(conversion_dict.keys()))
    to_unit = st.selectbox("To Unit", list(conversion_dict.keys()))
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        if category == "Temperature":
            result = conversion_dict[from_unit][to_unit](value)
        else:
            result = convert_units(value, from_unit, to_unit, conversion_dict)
        
        if result is not None:
            st.markdown(f"<div class='stAlert'>{value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
        else:
            st.error("Invalid conversion")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
