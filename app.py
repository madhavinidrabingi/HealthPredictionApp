import streamlit as st
from datetime import date

from database import (
    create_table,
    add_patient,
    view_patients,
    update_remarks,
    delete_patient
)

# Create Database Table
create_table()

st.title("Health Prediction Application")

st.header("Patient Information")

name = st.text_input("Full Name")

dob = st.date_input("Date of Birth")

email = st.text_input("Email Address")

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

# CREATE + PREDICTION
if st.button("Predict Health Condition"):

    if not name:
        st.error("Please enter Full Name")

    elif "@" not in email:
        st.error("Please enter valid Email Address")

    elif dob > date.today():
        st.error("Date of Birth cannot be in future")

    else:

        # Prediction Logic

        if glucose > 140:
            remarks = "High Diabetes Risk"

        elif cholesterol > 240:
            remarks = "High Heart Disease Risk"

        elif haemoglobin < 12:
            remarks = "Possible Anaemia Risk"

        else:
            remarks = "Normal Risk"

        add_patient(
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success("Prediction Completed")

        st.subheader("Remarks")
        st.write(remarks)

        st.success("Patient record saved successfully")


# READ
st.header("All Patient Records")

if st.button("View Records"):

    records = view_patients()

    if records:
        st.table(records)

    else:
        st.warning("No records found")


# UPDATE
st.header("Update Patient Remarks")

update_id = st.number_input(
    "Patient ID to Update",
    min_value=1,
    step=1
)

new_remarks = st.text_input(
    "New Remarks"
)

if st.button("Update Record"):

    update_remarks(
        update_id,
        new_remarks
    )

    st.success("Record Updated Successfully")


# DELETE
st.header("Delete Patient Record")

delete_id = st.number_input(
    "Patient ID to Delete",
    min_value=1,
    step=1,
    key="delete"
)

if st.button("Delete Record"):

    delete_patient(delete_id)

    st.success("Record Deleted Successfully")