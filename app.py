import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Predictive Maintenance System",
    page_icon="🛠️",
    layout="wide"
)

# Title
st.title("🛠️ Predictive Maintenance Prediction System")

st.write("""
Welcome to the Predictive Maintenance Dashboard.

This application predicts whether a machine is likely to fail using a trained Random Forest model.
""")

# Load model
model = joblib.load("outputs/best_random_forest_model.pkl")

st.header("📝 Enter Machine Details")

col1, col2 = st.columns(2)

# ---------------- LEFT COLUMN ----------------
with col1:

    type_map = {"L": 0, "M": 1, "H": 2}

    machine_type = st.selectbox("Machine Type",["L", "M", "H"])

    machine_type = type_map[machine_type]

    air_temperature = st.number_input(
        "Air Temperature (K)",
        value=300.0
    )

    process_temperature = st.number_input(
        "Process Temperature (K)",
        value=310.0
    )

    rotational_speed = st.number_input(
        "Rotational Speed (rpm)",
        value=1500
    )

    torque = st.number_input(
        "Torque (Nm)",
        value=40.0
    )

    tool_wear = st.number_input(
        "Tool Wear (min)",
        value=100
    )

    machine_age = st.number_input(
        "Machine Age (Years)",
        value=5
    )

    operating_hours = st.number_input(
        "Operating Hours",
        value=5000
    )

    days_since_last_maintenance = st.number_input(
        "Days Since Last Maintenance",
        value=30
    )

    maintenance_count = st.number_input(
        "Maintenance Count Last Year",
        value=3
    )

# ---------------- RIGHT COLUMN ----------------
with col2:

    energy = st.number_input(
        "Energy Consumption (kWh)",
        value=100.0
    )

    vibration = st.number_input(
        "Vibration Level (mm/s)",
        value=5.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        value=60.0
    )

    dust = st.number_input(
        "Ambient Dust Level (ug/m3)",
        value=30.0
    )

    maintenance_cost = st.number_input(
        "Maintenance Cost (USD)",
        value=500.0
    )

    st.subheader("Failure Indicators")

    twf = st.selectbox("TWF", [0, 1])
    hdf = st.selectbox("HDF", [0, 1])
    pwf = st.selectbox("PWF", [0, 1])
    osf = st.selectbox("OSF", [0, 1])
    rnf = st.selectbox("RNF", [0, 1])

# ---------------- ENGINEERED FEATURES ----------------
temp_diff = process_temperature - air_temperature
power = torque * rotational_speed
stress_index = torque * tool_wear
import pandas as pd

if st.button("🔍 Predict Machine Failure"):
    st.subheader("Calculated Features")

    st.write(f"Temperature Difference : {temp_diff:.2f}")
    st.write(f"Power : {power:.2f}")
    st.write(f"Stress Index : {stress_index:.2f}")

    # Create DataFrame with the same feature order used during training
    input_data = pd.DataFrame({
        "Type": [machine_type],
        "Air temperature [K]": [air_temperature],
        "Process temperature [K]": [process_temperature],
        "Rotational speed [rpm]": [rotational_speed],
        "Torque [Nm]": [torque],
        "Tool wear [min]": [tool_wear],
        "TWF": [twf],
        "HDF": [hdf],
        "PWF": [pwf],
        "OSF": [osf],
        "RNF": [rnf],
        "Machine_Age_Years": [machine_age],
        "Operating_Hours": [operating_hours],
        "Days_Since_Last_Maintenance": [days_since_last_maintenance],
        "Maintenance_Count_Last_Year": [maintenance_count],
        "Energy_Consumption_kWh": [energy],
        "Vibration_Level_mm_s": [vibration],
        "Humidity_Percent": [humidity],
        "Ambient_Dust_Level_ug_m3": [dust],
        "Maintenance_Cost_USD": [maintenance_cost],
        "temp_diff": [temp_diff],
        "power": [power],
        "stress_index": [stress_index]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    

    # 👇 ADD HERE
    if probability[1] > 0.7:
        st.error("High Failure Risk 🔴")
    elif probability[1] > 0.3:
        st.warning("Medium Risk of Failure 🟡")
    else:
        st.success("Low Risk of Failure 🟢")

    st.subheader("Prediction Result")


    if prediction == 1:
        st.error("⚠️ Machine Failure Predicted")
    else:
        st.success("✅ No Machine Failure Predicted")

    st.subheader("Prediction Probability")
    st.write(f"Failure Probability: **{probability[1]*100:.2f}%**")
    st.write(f"No Failure Probability: **{probability[0]*100:.2f}%**")