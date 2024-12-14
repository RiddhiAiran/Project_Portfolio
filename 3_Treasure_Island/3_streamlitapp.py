import streamlit as st
import time

def display_with_delay(text, delay=2):
    """Utility function to display text with a delay."""
    st.write(text)
    time.sleep(delay)

def play_game():
    """Main logic for the Treasure Island game."""
    if "stage" not in st.session_state:
        st.session_state.stage = "start"

    if st.session_state.stage == "start":
        st.subheader("You're at a crossroad. Where do you want to go?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Go Left"):
                st.session_state.stage = "lake"
                st.experimental_rerun()
        with col2:
            if st.button("Go Right"):
                display_with_delay("You turn right and take a step forward...")
                st.error("💀 Fell into a hole! Game Over.")
                st.session_state.stage = "game_over"

    elif st.session_state.stage == "lake":
        st.subheader("You've come to a lake. There is an island in the middle of the lake.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Wait for a boat"):
                st.session_state.stage = "house"
                st.experimental_rerun()
        with col2:
            if st.button("Swim across"):
                display_with_delay("You jump into the lake and start swimming...")
                st.error("🐟 Attacked by trout! Game Over.")
                st.session_state.stage = "game_over"

    elif st.session_state.stage == "house":
        st.subheader("You have arrived at the island unharmed. There is a house with 3 doors.")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Open Red Door"):
                display_with_delay("You open the red door and flames engulf you...")
                st.error("🔥 Burned by fire! Game Over.")
                st.session_state.stage = "game_over"
        with col2:
            if st.button("Open Yellow Door"):
                display_with_delay("You open the yellow door slowly...")
                st.balloons()
                st.success("🎉 Congrats! You found the treasure!")
                st.session_state.stage = "game_over"
        with col3:
            if st.button("Open Blue Door"):
                display_with_delay("You open the blue door and hear a growl...")
                st.error("🐾 Eaten by beasts! Game Over.")
                st.session_state.stage = "game_over"

    elif st.session_state.stage == "game_over":
        st.subheader("Game Over!")
        if st.button("Restart the Game"):
            st.session_state.stage = "start"
            st.experimental_rerun()

def treasure_island_game():
    """Interactive Treasure Island Game with a start button."""
    st.title("🏝️ Treasure Island Game 🪙")
    st.markdown(
        """
        Welcome to the **Treasure Island Adventure Game**! 🗺️
        
        Your mission is to find the treasure. Make your choices wisely, as your adventure could end abruptly!
        """
    )

    if "start_game" not in st.session_state:
        st.session_state.start_game = False

    if st.session_state.start_game:
        play_game()
    else:
        if st.button("Start the Game"):
            st.session_state.start_game = True
            st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    treasure_island_game()
