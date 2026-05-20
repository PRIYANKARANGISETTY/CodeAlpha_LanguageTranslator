import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #BBBBBB;
        margin-bottom: 30px;
    }

    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 50px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1E1E1E;
        color: white;
        font-size: 20px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌍 AI Language Translator</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Translate text instantly between multiple languages</div>',
    unsafe_allow_html=True
)

# Text Input
text = st.text_area("✍ Enter Text", height=150)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

# Dropdowns
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", languages.keys())

with col2:
    target = st.selectbox("Target Language", languages.keys())

# Translate Button
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text")

    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success("Translation Successful ✅")

            st.markdown(
                f'<div class="result-box">{translated}</div>',
                unsafe_allow_html=True
            )

            st.code(translated)

        except Exception as e:
            st.error("Translation Failed ❌")