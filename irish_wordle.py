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
    "crann": {"translation": "tree", "sentence": "Tá crann mór sa ghairdín.", "english_sentence": "There is a tree in the garden.", "grammar": "Masculine noun."},
    "milis": {"translation": "sweet", "sentence": "Tá milseán milis agam.", "english_sentence": "I have a sweet candy.", "grammar": "Adjective follows noun."},
    "brise": {"translation": "break", "sentence": "Briseann sé an cupán.", "english_sentence": "He breaks the cup.", "grammar": "'Brise' is a verb."},
    "feoil": {"translation": "meat", "sentence": "Ithim feoil.", "english_sentence": "I eat meat.", "grammar": "'Feoil' is a feminine noun."},
    "cluas": {"translation": "ear", "sentence": "Tá pian i mo chluas.", "english_sentence": "I have pain in my ear.", "grammar": "Feminine noun."},
"sróna": {"translation": "nose", "sentence": "Tá a sróna fuar.", "english_sentence": "His nose is cold.", "grammar": "Masculine noun."},
"croía": {"translation": "heart", "sentence": "Tá grá i mo chroía.", "english_sentence": "There is love in my heart.", "grammar": "Masculine noun, 'croí' takes 'croí' in nominative."},
"rogha": {"translation": "choice", "sentence": "Is é seo mo rogha.", "english_sentence": "This is my choice.", "grammar": "Feminine noun."},
"leaba": {"translation": "bed", "sentence": "Tá sí sa leaba fós.", "english_sentence": "She is still in bed.", "grammar": "Feminine noun."},
"méara": {"translation": "fingers", "sentence": "Tá mo mhéara fuar.", "english_sentence": "My fingers are cold.", "grammar": "Plural of 'méar' (finger)."},
"luath": {"translation": "early", "sentence": "Tá sé ró-luath.", "english_sentence": "It is too early.", "grammar": "Adjective."},
"amach": {"translation": "out", "sentence": "Téim amach gach lá.", "english_sentence": "I go out every day.", "grammar": "Adverb indicating direction."},
"tuath": {"translation": "north", "sentence": "Tá mé ag dul ó thuaidh.", "english_sentence": "I am going north.", "grammar": "'Tuath' becomes 'thuaidh' after 'ó'."},
"dearg": {"translation": "red", "sentence": "Tá an carr dearg.", "english_sentence": "The car is red.", "grammar": "Adjective follows noun."},
"dubha": {"translation": "black", "sentence": "Tá bróga dubha aige.", "english_sentence": "He has black shoes.", "grammar": "Plural adjective follows noun."},
"glasa": {"translation": "green", "sentence": "Tá súile glasa aici.", "english_sentence": "She has green eyes.", "grammar": "Plural adjective follows noun."},

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

# (Rest of your game code remains unchanged here)
