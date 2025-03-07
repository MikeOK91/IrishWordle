import random
import streamlit as st

# Expanded list of strictly 5-letter Irish words with translations
irish_words = {
    "madra": "dog", "uisce": "water", "teach": "house", "solas": "light", "bosca": "box",
    "bord": "table", "fuair": "found", "focal": "word", "siopa": "shop", "bróga": "shoes",
    "ceist": "question", "obair": "work", "peann": "pen", "tirim": "dry", "milis": "sweet",
    "crann": "tree", "scama": "cloud", "dearg": "red", "dubha": "black", "glasa": "green",
    "gaoth": "wind", "móran": "many", "beaga": "small", "luath": "early", "amach": "out",
    "tuath": "north", "cluas": "ear", "sróna": "nose", "croía": "heart", "rogha": "choice",
    "scoil": "school", "leaba": "bed", "ardán": "stage", "geata": "gate", "méara": "fingers",
    "beoir": "beer", "caora": "sheep", "iasca": "fish", "grian": "sun", "cósta": "coast", "ainmh": "animal", "bádóg": "boat", "brise": "break", "cáise": "cheese", "cloch": "stone",
"damhsa": "dance", "dráma": "drama", "éasca": "easy", "fáisc": "squeeze", "feoil": "meat",
"geall": "promise", "leann": "ale", "maith": "good", "neart": "power", "ólann": "drink",
"pláta": "plate", "ráite": "said", "ríoga": "royal", "seang": "slim", "tobar": "well",
"urlár": "floor", "féach": "look", "múine": "teach", "léigh": "read", "scríb": "write",
"seomr": "room", "breis": "extra", "brion": "dream", "páirc": "field", "dorás": "door"

}

# Function to reset the game
def reset_game():
    st.session_state.word_to_guess, st.session_state.translation = random.choice(list(irish_words.items()))
    st.session_state.attempts = 6
    st.session_state.previous_guesses = []

# Initialize session state
if 'word_to_guess' not in st.session_state:
    reset_game()

st.title("☘️ Irish Wordle ☘️")
st.write("Tomhais an focal! (5 litreacha). Tá 6 iarracht agat.")

# Display previous guesses
if 'previous_guesses' in st.session_state:
    for past_guess in st.session_state.previous_guesses:
        st.write(past_guess)

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
        guess_feedback = f"{guess.upper()} - {feedback}"
        st.session_state.previous_guesses.append(guess_feedback)
        st.write(guess_feedback)

        if guess == st.session_state.word_to_guess:
            st.success("🎉 Comhghairdeas! D’éirigh leat an focal a aimsiú! 🎉")
            st.session_state.attempts = 0
        else:
            if st.session_state.attempts == 1:
                st.info(f"📝 Leid: {st.session_state.translation}")

            if st.session_state.attempts <= 0:
                st.error(f"😔 Ádh mór an chéad uair eile! Bhí an focal ceart: '{st.session_state.word_to_guess}' ({st.session_state.translation})")
            else:
                st.write(f"Tá {st.session_state.attempts} iarracht agat fós.")

if st.button("Cluiche Nua"):
    reset_game()
