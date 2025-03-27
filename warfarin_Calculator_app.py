import streamlit as st

def warfarin_dose_adjustment(current_inr, target_inr_min, target_inr_max, current_dose):
    dose_adjustment = 0
    if current_inr < target_inr_min:
        if current_inr < target_inr_min - 0.5:
            dose_adjustment = 0.15  # Increase dose by 15%
        else:
            dose_adjustment = 0.10  # Increase dose by 10%
    elif current_inr > target_inr_max:
        if current_inr > target_inr_max + 0.5:
            dose_adjustment = -0.15  # Decrease dose by 15%
        else:
            dose_adjustment = -0.10  # Decrease dose by 10%

    new_dose = current_dose * (1 + dose_adjustment)
    follow_up = "Recheck INR in 4-7 days." if abs(dose_adjustment) > 0.10 else "Recheck INR in 1-2 weeks."
    
    return round(new_dose, 2), dose_adjustment * 100, follow_up

st.title("💊 Warfarin Dose Adjustment Calculator")

current_inr = st.number_input("Current INR", min_value=0.0, max_value=10.0, step=0.1, value=2.0)
target_inr_min = st.number_input("Target INR (Minimum)", min_value=0.0, max_value=10.0, step=0.1, value=2.0)
target_inr_max = st.number_input("Target INR (Maximum)", min_value=0.0, max_value=10.0, step=0.1, value=3.0)
current_dose = st.number_input("Current Dose (mg)", min_value=0.0, max_value=50.0, step=0.1, value=5.0)

if st.button("Calculate New Dose"):
    new_dose, dose_adjustment, follow_up = warfarin_dose_adjustment(current_inr, target_inr_min, target_inr_max, current_dose)
    st.write(f"### 📌 Recommended New Dose: {new_dose} mg per day")
    st.write(f"### 📌 Dose Adjustment: {dose_adjustment:.1f}%")
    st.write(f"### 📌 Follow-Up Recommendation: {follow_up}")
