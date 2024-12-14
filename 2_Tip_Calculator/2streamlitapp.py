import streamlit as st

def tip_calculator():
    '''Generate Total Bill Amount Each Person will Pay Including Tip'''
    # Set up the app interface
    st.title("🧾 Tip Calculator 😇")
    st.markdown(
        """
        Welcome to the **Tip Calculator**! Easily calculate the total bill amount 
        and how much each person should pay, including the tip.
        """
    )

    # Collect user inputs
    bill = st.number_input("💵 What was the total bill? ($)", min_value=0.0, step=0.01, format="%.2f")
    tip = st.slider("📝 How much tip would you like to give? (%)", min_value=0, max_value=100, step=1, value=10)
    splitting = st.number_input("🧑‍🧑‍🧒‍🧒 How many people to split the bill?", min_value=1, step=1, value=1)

    # Calculate the results
    if st.button("Calculate"):
        if bill > 0 and splitting > 0:
            total_bill = bill + (bill * (tip / 100))
            each = total_bill / splitting
            st.success(f"💰 **Total Bill (with Tip):** ${total_bill:.2f}")
            st.info(f"👤 **Each Person Pays:** ${each:.2f}")
        else:
            st.error("❗ Please enter valid values for the bill and number of people.")

# Run the app
if __name__ == "__main__":
    tip_calculator()