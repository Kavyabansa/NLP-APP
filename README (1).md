# Multi-task NLP App 🤖

A Gradio-based Natural Language Processing application that performs two NLP tasks on user-provided text:

1. **Sentiment Analysis** — classifies text as positive or negative and displays the confidence score.
2. **Named Entity Recognition (NER)** — extracts named entities such as persons, organizations, and locations.

## Models Used

### Sentiment Analysis
- Model: `distilbert-base-uncased-finetuned-sst-2-english`
- Library: Hugging Face Transformers

### Named Entity Recognition
- Model: `dbmdz/bert-large-cased-finetuned-conll03-english`
- Aggregation strategy: `simple`
- Library: Hugging Face Transformers

## Tech Stack

- Python
- Gradio
- Hugging Face Transformers
- PyTorch

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Clone or download the project

```bash
git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY-FOLDER>
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Gradio will print a local URL in the terminal.

## Deploy on Hugging Face Spaces

This project is designed to run as a **Gradio Space**.

### Files to upload

Upload these files to your Hugging Face Space:

```text
app.py
requirements.txt
README.md
```

When creating the Space, choose:

- **SDK:** Gradio
- **Visibility:** Public or Private according to your requirement
- **Hardware:** CPU is sufficient for this application, although inference can be slower than GPU

Hugging Face will automatically install the dependencies from `requirements.txt` and run the Gradio application.

## How It Works

The application loads two pretrained Transformer pipelines when it starts:

```python
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)
```

and:

```python
ner_pipeline = pipeline(
    "ner",
    model="dbmdz/bert-large-cased-finetuned-conll03-english",
    aggregation_strategy="simple",
)
```

When a user enters text, the application sends the same text to both pipelines.

The sentiment result is displayed as:

```text
POSITIVE (98.52% confidence)
```

The NER result is displayed as entities with their detected entity type and confidence.

Example:

```text
Tim Cook                  → PER (99.80%)
Apple                     → ORG (99.70%)
San Francisco             → LOC (99.90%)
```

## Example Inputs

### Example 1

```text
Apple CEO Tim Cook announced iPhone 15 in San Francisco
```

### Example 2

```text
The movie was absolutely terrible, I hated every moment
```

### Example 3

```text
Elon Musk's Tesla reported record profits in the United States
```

## Notes

- The models are downloaded automatically from Hugging Face the first time the application starts.
- No local model files are required.
- The application automatically uses CUDA GPU when available and CPU otherwise.
- The original notebook used `share=True` for a temporary Gradio public link. For hosted deployment, `app.launch()` is used instead because the hosting platform provides the public URL.
- The NER model is relatively large, so the first startup can take some time while the model is downloaded and loaded.

## Original Notebook

This deployment version is based on the `week8_day6_nlp_app.ipynb` notebook.

## License

This project uses pretrained models from Hugging Face. Refer to the individual model pages for their respective licenses and usage conditions.
