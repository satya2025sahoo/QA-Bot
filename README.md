Here's a visually appealing version of your `README.md` file in Markdown:

---

# 🧠 Chat-Style QA Bot

Welcome to the **Chat-style QA Bot**, a document-based question-answering application that leverages **LlamaIndex**, **ChromaDB**, and **Google Gemini** models for document embeddings and language understanding. It provides accurate, AI-generated responses based on the content of the uploaded document, which can be easily deployed with Docker and features an intuitive interface powered by **Streamlit**.

---

## 🚀 Features

- **Document Upload**: Supports PDF and TXT document uploads.
- **AI-Powered QA**: Provides AI-generated answers based on document content.
- **Contextual Responses**: Retrieves relevant document segments to give context.
- **Powered by Google Generative AI**: Utilizes Google Gemini models for language understanding.

---

## 🛠️ Setup Instructions

### Prerequisites

Ensure the following dependencies are installed before setting up the project:

- Python 3.11.9
- Docker (for containerization)
- Google Cloud credentials with access to the **Generative AI API**

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Configure Google API Credentials

Ensure you have a valid Google Cloud project and **Generative AI API** key. Set up your environment variables using the JSON credentials file:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
```

### Step 3: Install Dependencies

Make sure `pip` is installed, then run:

```bash
pip install -r requirements.txt
```

### Step 4: Running Locally

Start the application locally with:

```bash
streamlit run app.py
```

### Step 5: Running with Docker

Prefer to run the app inside a Docker container? Follow these steps:

1. **Build the Docker image**:

    ```bash
    docker build -t chat-style-qa-bot .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -p 8501:8501 chat-style-qa-bot
    ```

Access the app at `http://localhost:8501`.

---

## 💡 Usage Instructions

1. **Upload Document**: Upload a PDF or TXT file through the app interface.
2. **Ask Questions**: Type your questions into the chatbox, and the bot will respond based on the document's content.
3. **Chat History**: View your queries and the bot’s answers along with relevant document segments.

---

## 📂 File Structure

```bash
├── app.py              # Main application file for Streamlit interface
├── Backend.py          # Core logic for document processing and LLM interactions
├── Dockerfile          # Docker configuration file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔑 Environment Variables

- **GOOGLE_APPLICATION_CREDENTIALS**: Path to your JSON key file for Google Cloud authentication.
- **GENAI_API_KEY**: Your API key for Google Generative AI.

---

## 📝 License

This project is licensed under the **MIT License**. Check the `LICENSE` file for more details.

---

## 🤝 Contributing

We welcome all kinds of contributions! If you would like to contribute:

1. **Fork the repository**.
2. **Create a branch**: `git checkout -b feature/AmazingFeature`.
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`.
4. **Push to the branch**: `git push origin feature/AmazingFeature`.
5. **Open a pull request**.

---

Happy coding! 💻✨

---

Let me know if you'd like to add or tweak anything else!
