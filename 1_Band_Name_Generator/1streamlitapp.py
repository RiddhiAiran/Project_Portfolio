import streamlit as st

def band_name_generator():
    """Generate a band name based on user inputs."""
    # Set up the app interface
    st.title("🎸 Band Name Generator 🎶")
    st.markdown(
        """
        Welcome to the **Band Name Generator**! Let's help you come up with a catchy band name.
        
        Just provide the following details below:
        """
    )

    # Collect user inputs
    city = st.text_input("🏙️ What's the name of the city you grew up in?", "")
    pet = st.text_input("🐾 What's your pet's name?", "")

    # Generate and display the band name if inputs are provided
    if st.button("Generate Band Name"):
        if city and pet:
            band_name = f"The {city.title()} {pet.title()}"
            st.success(f"✨ Your Band Name Could Be: **{band_name}** ✨")
        else:
            st.error("❗ Please fill in both fields to generate your band name.")

# Run the app
if __name__ == "__main__":
    band_name_generator()