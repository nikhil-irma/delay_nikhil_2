import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------

filename = "logi.sav"
loaded_model = joblib.load(filename)


# -----------------------------------
# COLUMN NAMES
# -----------------------------------

columns = [
    "Delivery_Distance",
    "Traffic_Congestion",
    "Weather_Condition",
    "Delivery_Slot",
    "Driver_Experience",
    "Num_Stops",
    "Vehicle_Age",
    "Road_Condition_Score",
    "Package_Weight",
    "Fuel_Efficiency",
    "Warehouse_Processing_Time"
]


# -----------------------------------
# STREAMLIT APP
# -----------------------------------

st.title("🚚 Delivery Delay Prediction")

st.write("Enter the delivery details below to predict whether a significant delivery delay is expected.")


# -----------------------------------
# USER INPUTS
# -----------------------------------

Delivery_Distance = st.number_input(
    "Delivery Distance (in km)",
    min_value=0.0,
    value=10.0
)

Traffic_Congestion = st.number_input(
    "Traffic Congestion Level (1-5)",
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

Weather_Condition = st.number_input(
    "Weather Condition (1-5)",
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

Delivery_Slot = st.number_input(
    "Delivery Slot (1-based index)",
    min_value=1,
    value=1,
    step=1
)

Driver_Experience = st.number_input(
    "Driver Experience (in years)",
    min_value=0.0,
    value=2.0
)

Num_Stops = st.number_input(
    "Number of Stops",
    min_value=0,
    value=1,
    step=1
)

Vehicle_Age = st.number_input(
    "Vehicle Age (in years)",
    min_value=0.0,
    value=3.0
)

Road_Condition_Score = st.number_input(
    "Road Condition Score (1-5)",
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

Package_Weight = st.number_input(
    "Package Weight (in kg)",
    min_value=0.0,
    value=5.0
)

Fuel_Efficiency = st.number_input(
    "Fuel Efficiency (in km/liter)",
    min_value=0.0,
    value=15.0
)

Warehouse_Processing_Time = st.number_input(
    "Warehouse Processing Time (in minutes)",
    min_value=0.0,
    value=30.0
)


# -----------------------------------
# CREATE INPUT DATAFRAME
# -----------------------------------

input_data = pd.DataFrame(
    [[
        Delivery_Distance,
        Traffic_Congestion,
        Weather_Condition,
        Delivery_Slot,
        Driver_Experience,
        Num_Stops,
        Vehicle_Age,
        Road_Condition_Score,
        Package_Weight,
        Fuel_Efficiency,
        Warehouse_Processing_Time
    ]],
    columns=columns
)


# -----------------------------------
# PREDICTION
# -----------------------------------

if st.button("🔮 Predict Delivery Delay"):

    try:

        prediction = loaded_model.predict(input_data)

        if prediction[0] == 0:

            st.success(
                "✅ Predicted Delivery Delay: 0\n\n"
                "No significant delay expected."
            )

        else:

            st.error(
                "⚠️ Predicted Delivery Delay: 1\n\n"
                "Delivery delay expected."
            )

    except Exception as e:

        st.error("An error occurred while making the prediction.")
        st.write(e)
