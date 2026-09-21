# 🤖 Multi-Task NLP Analyzer

An interactive **Natural Language Processing (NLP) web application** built with **Python, Streamlit, Hugging Face Transformers, and PyTorch**.

The application performs two NLP tasks on user-provided text:

* 😊 **Sentiment Analysis** — detects whether the text is positive or negative.
* 🏷️ **Named Entity Recognition (NER)** — identifies people, organizations, locations, and other named entities.

## 🚀 Live Demo

🌐 **Try the application:**
https://kavyabansa-nlp-app-app-uahuk2.streamlit.app/

---

## ✨ Features

### 😊 Sentiment Analysis

The application analyzes the emotional polarity of the input text and returns:

* `POSITIVE`
* `NEGATIVE`
* Confidence score

### 🏷️ Named Entity Recognition

The application identifies important entities within the text and displays:

* Entity name
* Entity type
* Confidence score

Example entity types include:

* 👤 `PERSON`
* 🏢 `ORGANIZATION`
* 📍 `LOCATION`

---

## 🧪 Example Inputs

Try these examples in the application:

```text
Apple CEO Tim Cook announced iPhone 15 in San Francisco.
```

```text
The movie was absolutely terrible, I hated every moment.
```

```text
Elon Musk's Tesla reported record profits in the United States.
```

---

## 🧠 NLP Models

### Sentiment Analysis

**Model:**

`distilbert-base-uncased-finetuned-sst-2-english`

A pre-trained DistilBERT model used for binary sentiment classification.

### Named Entity Recognition

**Model:**

`dbmdz/bert-large-cased-finetuned-conll03-english`

A BERT-based model used for Named Entity Recognition.

The application uses Hugging Face's `pipeline()` API to perform inference.

---

## 🏗️ How It Works

```text
             User Input
                 │
                 ▼
        ┌─────────────────┐
        │    Streamlit    │
        │   Web Interface │
        └────────┬────────┘
                 │
          ┌──────┴──────┐
          ▼             ▼
   Sentiment Model   NER Model
          │             │
          ▼             ▼
   Positive/Negative   Entities
   + Confidence       + Confidence
          │             │
          └──────┬──────┘
                 ▼
          Results Display
```

---

## 🛠️ Technologies Used

| Technology                   | Purpose                      |
| ---------------------------- | ---------------------------- |
| 🐍 Python                    | Application development      |
| 🎈 Streamlit                 | Web interface and deployment |
| 🤗 Hugging Face Transformers | NLP model inference          |
| 🔥 PyTorch                   | Deep learning framework      |
| 🧠 DistilBERT                | Sentiment analysis           |
| 🏷️ BERT                     | Named Entity Recognition     |

---

## 📂 Project Structure

```text
nlp-app/
│
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

### `app.py`

Contains the Streamlit application, model loading, text processing, and result display.

### `requirements.txt`

Contains the Python packages required to run the application.

### `runtime.txt`

Specifies the Python version used for deployment.

### `README.md`

Project documentation and setup instructions.

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Kavyabansa/nlp-app.git
cd nlp-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment workflow:

```text
GitHub Repository
       │
       ▼
Streamlit Community Cloud
       │
       ▼
Install requirements
       │
       ▼
Run app.py
       │
       ▼
Live Web Application
```

---

## 🔄 Application Workflow

When the user clicks **Analyze Text**:

1. The input text is sent to the sentiment-analysis model.
2. The model predicts the sentiment.
3. A confidence score is generated.
4. The text is passed to the NER model.
5. Named entities are extracted.
6. Entity types and confidence scores are displayed in the application.

---

## 📸 Example

### Input

```text
Apple CEO Tim Cook announced iPhone 15 in San Francisco.
```

### Output

```text
Sentiment Analysis
POSITIVE

Named Entities

Tim Cook       → PERSON
Apple          → ORGANIZATION
San Francisco  → LOCATION
```

The exact predictions and confidence scores depend on the input text and model inference.

---

## 🎯 Project Objective

The objective of this project is to demonstrate how **pre-trained Transformer-based NLP models** can be integrated into an interactive web application.

The project combines multiple NLP tasks into a single application and demonstrates the complete workflow from:

```text
NLP Models
    ↓
Python
    ↓
Streamlit Application
    ↓
GitHub
    ↓
Cloud Deployment
    ↓
Live Web App
```

---

## 🔮 Future Improvements

Possible future enhancements include:

* 📊 Sentiment visualization and charts
* 🌍 Multilingual NLP support
* 📝 Text summarization
* ❓ Question answering
* 📈 Additional text analytics
* 💾 Downloadable analysis reports
* 🎨 Improved UI/UX
* ⚡ Faster model loading and inference
* 📱 Better mobile responsiveness

---

## 👨‍💻 Author

**Kavya Bansal**

B.Tech — Artificial Intelligence

---

## 🙌 Acknowledgements

This project uses open-source technologies and pre-trained models from:

* Hugging Face Transformers
* PyTorch
* Streamlit

---

## 📄 License

This project is created for **educational and demonstration purposes**.
