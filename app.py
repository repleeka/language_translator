import streamlit as st
from deep_translator import GoogleTranslator

def translate_text(text, src, dest):
    try:
        translator = GoogleTranslator(source=src, target=dest)
        return translator.translate(text)
    except Exception as e:
        st.error(f"Translation error: {str(e)}")
        return None

st.title("Language Translator")

# Available languages
languages = GoogleTranslator().get_supported_languages()

# User selects source and target languages
src_lang = st.selectbox("Select source language:", languages, index=languages.index("english"))
dest_lang = st.selectbox("Select target language:", languages, index=languages.index("french"))

# Input text area
input_text = st.text_area("Enter text to translate:", "Hello, how are you?")

if st.button("Translate"):
    if input_text:
        with st.spinner("Translating..."):
            translated_text = translate_text(input_text, src_lang, dest_lang)
        if translated_text:
            st.success("Translation complete!")
            st.write("Translated text:")
            st.write(translated_text)
    else:
        st.warning("Please enter some text to translate.")
