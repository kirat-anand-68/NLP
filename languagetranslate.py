import streamlit as st
from deep_translator import GoogleTranslator

# ---------- Page Configuration ----------
st.set_page_config(page_title="🌐 Universal Language Translator", page_icon="🌍", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: #e0e0e0;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: 700;
            color: #4FC3F7;
            margin-bottom: 0.3rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1rem;
            color: #9e9e9e;
            margin-bottom: 2rem;
        }
        textarea, .stSelectbox > div {
            background-color: #1e1e1e !important;
            border: 1px solid #4FC3F7 !important;
            color: white !important;
        }
        .stButton>button {
            background-color: #4FC3F7;
            color: black;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #29B6F6;
            transform: scale(1.05);
        }
        .result-box {
            background-color: #1e1e1e;
            padding: 1.2rem;
            border-radius: 10px;
            border: 1px solid #4FC3F7;
            margin-top: 1rem;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- App Title ----------
st.markdown('<div class="title">🌐 Universal Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text between ANY two languages instantly</div>', unsafe_allow_html=True)

# ---------- Input Section ----------
text_to_translate = st.text_area("📝 Enter text to translate:", height=120, placeholder="Type or paste text here...")

# List of popular languages for selection
languages = [
    "auto", "english", "hindi", "french", "spanish", "german", "russian", "japanese",
    "chinese (simplified)", "italian", "arabic", "portuguese", "korean", "turkish"
]

col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox("🌍 Source Language:", languages, index=0)
with col2:
    target_language = st.selectbox("🎯 Target Language:", languages, index=2)

# ---------- Translation Logic ----------
if st.button("Translate"):
    if text_to_translate.strip():
        try:
            translator = GoogleTranslator(source=source_language, target=target_language)
            translated_text = translator.translate(text_to_translate)
            st.markdown("<h4 style='color:#4FC3F7;'>✅ Translated Text:</h4>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-box'>{translated_text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"⚠️ Translation failed: {e}")
    else:
        st.warning("⚠️ Please enter text to translate.")
