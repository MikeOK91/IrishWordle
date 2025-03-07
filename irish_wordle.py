import random
import streamlit as st
from gtts import gTTS
from io import BytesIO

# Comprehensive Irish words dictionary with translations, example sentences, and grammar tips
irish_words = {
    "madra": {"translation": "dog", "sentence": "Tá madra agam.", "english_sentence": "I have a dog.", "grammar": "'Madra' is a masculine noun."},
    "uisce": {"translation": "water", "sentence": "Ólann sí uisce.", "english_sentence": "She drinks water.", "grammar": "'Uisce' is always singular."},
    "teach": {"translation": "house", "sentence": "Tá an teach mór.", "english_sentence": "The house is big.", "grammar": "'Teach' becomes 'tí' in genitive."},
    "solas": {"translation": "light", "sentence": "Tá an solas geal.", "english_sentence": "The light is bright.", "grammar": "'Solas' is masculine."},
    "bosca": {"translation": "box", "sentence": "Tá bosca ar an mbord.", "english_sentence": "There is a box on the table.", "grammar": "'Bosca' takes 'mbosca' after 'ar an'."},
    "bord": {"translation": "table", "sentence": "Tá an leabhar ar an mbord.", "english_sentence": "The book is on the table.", "grammar": "'Bord' becomes 'mbord' after preposition 'ar an'."},
    "siopa": {"translation": "shop", "sentence": "Tá siopa nua sa bhaile.", "english_sentence": "There's a new shop in town.", "grammar": "'Siopa' is masculine."},
    "bróga": {"translation": "shoes", "sentence": "Cheannaigh mé bróga nua.", "english_sentence": "I bought new shoes.", "grammar": "Plural of 'bróg' (shoe)."},
    "peann": {"translation": "pen", "sentence": "Tá peann agam.", "english_sentence": "I have a pen.", "grammar": "'Peann' is masculine."},
    "tirim": {"translation": "dry", "sentence": "Tá an aimsir tirim inniu.", "english_sentence": "The weather is dry today.", "grammar": "Adjective."},
    "milis": {"translation": "sweet", "sentence": "Tá an cáca milis.", "english_sentence": "The cake is sweet.", "grammar": "Adjective follows noun."},
    "gaoth": {"translation": "wind", "sentence": "Tá an ghaoth láidir.", "english_sentence": "The wind is strong.", "grammar": "Feminine noun, takes lenition."},
    "crann": {"translation": "tree", "sentence": "Tá crann sa ghairdín.", "english_sentence": "There is a tree in the garden.", "grammar": "Masculine noun."},
    "grian": {"translation": "sun", "sentence": "Tá an ghrian ag taitneamh.", "english_sentence": "The sun is shining.", "grammar": "Feminine noun, takes lenition."},
    "beoir": {"translation": "beer", "sentence": "Ólann sé beoir.", "english_sentence": "He drinks beer.", "grammar": "Feminine noun."},
    "iasca": {"translation": "fish", "sentence": "Ithim iasca go minic.", "english_sentence": "I eat fish often.", "grammar": "Plural form of 'iasc'."},
    "geata": {"translation": "gate", "sentence": "Dún an geata, le do thoil.", "english_sentence": "Close the gate, please.", "grammar": "Masculine noun."},
}

# Function to reset the game
def reset_game():
    st.session_state.word, details = random.choice(list(irish_words.items()))
    st.session_state.word_to_guess = st.session_state.word
    st.session_state.translation = details["translation"]
    st.session_state.sentence = details["sentence"]
    st.session_state.english_sentence = details["english_sentence"]
    st.session_state.grammar = details["grammar"]
    st.session_state.attempts = 6
    st.session_state.previous_guesses = []

# Initialize session state
if 'word_to_guess' not in st.session_state:
    reset_game()

st.title("☘️ Irish Wordle ☘️")
st.write("Tomhais an focal! (5 litreacha). Tá 6 iarracht agat.")

# Display previous guesses
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
            st.info(f"📚 Grammar Tip: {st.session_state.grammar}")
            sound_file = BytesIO()
            tts = gTTS(st.session_state.word_to_guess, lang='ga')
            tts.write_to_fp(sound_file)
            st.audio(sound_file, format='audio/mp3')
            st.info(f"📖 {st.session_state.sentence} ({st.session_state.english_sentence})")
            st.session_state.attempts = 0
        else:
            if st.session_state.attempts == 2:
                sentence_with_blank = st.session_state.sentence.replace(st.session_state.word_to_guess, "_____", 1)
                st.info(f"📖 Sampla: {sentence_with_blank}")
            if st.session_state.attempts == 1:
                st.info(f"📖 Translation: {st.session_state.english_sentence}")

            if st.session_state.attempts <= 0:
                st.error(f"😔 Ádh mór an chéad uair eile! Bhí an focal ceart: '{st.session_state.word_to_guess}' ({st.session_state.translation})")
                st.info(f"📖 Sampla: {st.session_state.sentence} ({st.session_state.english_sentence})")
                sound_file = BytesIO()
                tts = gTTS(st.session_state.word_to_guess, lang='ga')
                tts.write_to_fp(sound_file)
                st.audio(sound_file, format='audio/mp3')
            else:
                st.write(f"Tá {st.session_state.attempts} iarracht agat fós.")

if st.button("Cluiche Nua"):
    reset_game()
