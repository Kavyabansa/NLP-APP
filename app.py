import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Multi-task NLP App", page_icon="🤖")

st.title("🤖 Multi-task NLP App")
st.write("Analyze text for sentiment and named entities.")

@st.cache_resource
def load_models():
    sentiment = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        device=-1,
    )
    ner = pipeline(
        "ner",
        model="dbmdz/bert-large-cased-finetuned-conll03-english",
        aggregation_strategy="simple",
        device=-1,
    )
    return sentiment, ner

with st.spinner("Loading NLP models..."):
    sentiment_pipeline, ner_pipeline = load_models()

examples = [
    "Apple CEO Tim Cook announced iPhone 15 in San Francisco",
    "The movie was absolutely terrible, I hated every moment",
    "Elon Musk's Tesla reported record profits in the United States",
]

text = st.text_area(
    "Input Text",
    height=140,
    placeholder="Type any text here — news headline, review, sentence...",
)

selected = st.selectbox("Or choose an example", ["-- Select an example --"] + examples)
if selected != "-- Select an example --":
    text = selected

if st.button("Analyze Text", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            sentiment = sentiment_pipeline(text)[0]
            entities = ner_pipeline(text)

        st.subheader("Sentiment Analysis")
        st.write(f"**{sentiment['label']}** ({sentiment['score']:.2%} confidence)")

        st.subheader("Named Entities")
        if entities:
            st.table([
                {
                    "Entity": e["word"],
                    "Type": e["entity_group"],
                    "Confidence": f"{e['score']:.2%}",
                }
                for e in entities
            ])
        else:
            st.info("No entities found.")
