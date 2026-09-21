import gradio as gr
from transformers import pipeline
import torch

# Use GPU when available; otherwise fall back to CPU.
device = 0 if torch.cuda.is_available() else -1
print(f"Using GPU: {device == 0}")

# Load both NLP pipelines.
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    device=device,
)

ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple",
    device=device,
)

print("Both pipelines loaded!")


def analyze_text(text):
    # Handle empty input gracefully.
    if not text or not text.strip():
        return "Please enter some text.", "No entities found"

    # Sentiment
    sentiment = sentiment_pipeline(text)[0]
    sent_label = sentiment["label"]
    sent_score = sentiment["score"]

    # Named Entity Recognition
    entities = ner_pipeline(text)

    # Format sentiment output
    sentiment_output = f"{sent_label} ({sent_score:.2%} confidence)"

    # Format NER output
    if entities:
        ner_output = "\n".join(
            [
                f"{ent['word']:25s} → {ent['entity_group']} ({ent['score']:.2%})"
                for ent in entities
            ]
        )
    else:
        ner_output = "No entities found"

    return sentiment_output, ner_output


app = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Type any text here — news headline, review, sentence...",
        label="Input Text",
    ),
    outputs=[
        gr.Textbox(label="Sentiment Analysis"),
        gr.Textbox(label="Named Entities"),
    ],
    title="Multi-task NLP App",
    description=(
        "Analyzes any text for sentiment (positive/negative) and extracts "
        "named entities (persons, organizations, locations)."
    ),
    examples=[
        ["Apple CEO Tim Cook announced iPhone 15 in San Francisco"],
        ["The movie was absolutely terrible, I hated every moment"],
        ["Elon Musk's Tesla reported record profits in the United States"],
    ],
)

if __name__ == "__main__":
    app.launch()
