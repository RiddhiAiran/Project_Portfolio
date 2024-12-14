import streamlit as st
import time

def display_with_delay(text, delay=2):
    """Utility function to display text with a delay."""
    with st.spinner(text):
        time.sleep(delay)

def treasure_island_game():
    """Interactive Treasure Island Game with suspense and streamlined code."""
    # Set up the app interface
    st.title("🏝️ Treasure Island Game 🪙")
    st.markdown(
        """
        Welcome to the **Treasure Island Adventure Game**! 🗺️
        
        Your mission is to find the treasure. Make your choices wisely, as your adventure could end abruptly!
        """
    )

    # Display the initial story
    st.subheader("You're at a crossroad. Where do you want to go?")
    road = st.radio("Choose a direction:", ("Left", "Right"))

    if road == "Left":
        display_with_delay("You turn left and walk down a dusty path...")
        st.subheader("You've come to a lake. There is an island in the middle of the lake.")
        lake = st.radio("What will you do?", ("Wait for a boat", "Swim across"))

        if lake == "Wait for a boat":
            display_with_delay("You decide to wait... Minutes turn into hours...")
            st.subheader("You have arrived at the island unharmed. There is a house with 3 doors.")
            door = st.selectbox("Choose a door color:", ("Red", "Yellow", "Blue"))

            if door == "Yellow":
                display_with_delay("You open the yellow door slowly...")
                st.balloons()
                st.success("🎉 Congrats! You found the treasure!")
            elif door == "Red":
                display_with_delay("You open the red door and flames engulf you...")
                st.error("🔥 Burned by fire! Game Over.")
            elif door == "Blue":
                display_with_delay("You open the blue door and hear a growl...")
                st.error("🐾 Eaten by beasts! Game Over.")
            else:
                st.error("Game Over.")
        else:
            display_with_delay("You jump into the lake and start swimming...")
            st.error("🐟 Attacked by trout! Game Over.")
    else:
        display_with_delay("You turn right and take a step forward...")
        st.error("💀 Fell into a hole! Game Over.")

# Run the app
if __name__ == "__main__":
    treasure_island_game()
