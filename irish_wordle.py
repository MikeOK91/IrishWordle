import streamlit as st
import random

# Title and instructions
st.title("☘️ Irish Wordle ☘️")
st.write("Tomhais an focal Gaeilge! (5 litreacha, 6 iarracht)")

# Word list with translations
irish_words = {
    "madra": "dog", "uisce": "water", "teach": "house", "solas": "light", "bosca": "box",
    "bord": "table", "fuair": "found", "focal": "word", "siopa": "shop", "bróga": "shoes",
    "ceist": "question", "obair": "work", "peann": "pen", "tirim": "dry", "milis": "sweet",
    "crann": "tree", "scama": "cloud", "dearg": "red", "dubha": "black", "glasa": "green",
    "gaoth": "wind", "móran": "many", "beaga": "small", "luath": "early", "amach": "out",
    "tuath": "north", "cluas": "ear", "sróna": "nose", "croía": "heart", "rogha": "choice",
    "scoil": "school", "leaba": "bed", "ardán": "stage", "geata": "gate", "méara": "fingers",
    "beoir": "beer", "caora": "sheep", "iasca": "fish", "grian": "sun", "cósta": "coast"
}

# Keep chosen word between sessions
if 'word_to_guess' not in st.session_state:
    st.session_state.word_to_guess, st.session_state.translation = random.choice(list(irish_words.items()))
    st.session_state.attempts = 6
    st.session_state.guesses = []

# User input
guess = st.text_input("Scríobh do thuairim:").lower()

if st.button("Seol an buille faoi thuairim"):
    if len(guess) != 5:
        st.warning("⚠️ Caithfidh an focal a bheith 5 litreacha ar fad.")
    else:
        feedback = ""
        for i in range(5):
            if guess[i] == st.session_state.word_to_guess[i]:
                feedback += f"🟩{guess[i]}"
            elif guess[i] in st.session_state.word_to_guess:
                feedback += f"🟨{guess[i]}"
            else:
                feedback += f"⬛{guess[i]}"

        st.session_state.attempts -= 1
        st.session_state.setdefault('guesses_list', []).append(feedback)
        st.write(feedback)

        if guess == st.session_state.word_to_guess:
            st.success("🎉 Comhghairdeas! D’éirigh leat an focal a aimsiú! 🎉")
            st.balloons()
            st.stop()
        else:
            st.session_state.attempts -= 1
            st.warning(f"Tá {st.session_state.attempts} iarracht agat fós.")

        if st.session_state.attempts == 1:
            if st.checkbox("Ar mhaith leat leid?"):
                st.info(f"Leid: {st.session_state.translation}")

        if st.session_state.attempts <= 0:
            st.error(f"😔 Ádh mór an chéad uair eile! Bhí an focal ceart: '{st.session_state.word_to_guess}' ({st.session_state.translation})")
            st.stop()

st.write(f"Iarrachtaí fágtha: {st.session_state.attempts}")
