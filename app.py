import streamlit as st
from textblob import TextBlob

st.title("🎭 Sentiment Analyzer")
st.write("Enter any text below to analyze its sentiment!")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if user_input:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0.1:
            st.success(f"✅ Positive — Polarity: {round(polarity, 2)}")
        elif polarity < -0.1:
            st.error(f"❌ Negative — Polarity: {round(polarity, 2)}")
        else:
            st.info(f"😐 Neutral — Polarity: {round(polarity, 2)}")

        st.write(f"📊 Subjectivity: {round(subjectivity, 2)} (0 = factual, 1 = opinion)")

        st.divider()
        st.write(f"📝 Word Count: {len(user_input.split())}")
        st.write(f"🔤 Character Count: {len(user_input)}")

    else:
        st.warning("⚠️ Please enter some text first!")
        