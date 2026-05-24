# 🧠 Behavior Detection Agent

An intelligent, real-time AI agent built using **Chainlit** and **Python** to analyze user or system behavior patterns, detect anomalies, and stream real-time interaction feedback. This agent acts as an automated observer, helping developers or analysts monitor activities and understand usage behaviors dynamically.

## 🚀 Features

- **Real-Time Interactive Chat:** Power by Chainlit for streaming responses and high-fidelity interaction.
- **Behavior & Anomaly Analysis:** Automatically evaluates input sequences or system logs to identify atypical patterns or behavior signals.
- **Interactive UI Elements:** Uses Chainlit's action buttons, loaders, and card displays to present behavior reports.
- **Extensible Architecture:** Easily swap the underlying LLM (OpenAI, Gemini, Anthropic) or modify the behavior detection heuristic rules.

## 🛠️ Tech Stack

- **Framework:** [Chainlit](https://github.com/Chainlit/chainlit)
- **Language:** Python 3.10+
- **AI Integration:** OpenAI / Google Gemini API (via standard LangChain or direct API wrappers)

## 📋 Prerequisites

Ensure you have Python 3.10 or higher installed, along with your chosen AI platform API credentials.

## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/abdulmannan991/Behavior-Detection-Agent.git
   cd Behavior-Detection-Agent
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not present, install core packages: `pip install chainlit python-dotenv openai google-generativeai`)*

4. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   # OR
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🎮 How to Run

Launch the Chainlit application using the command line:

```bash
chainlit run app.py -w
```
The `-w` flag enables hot-reloading. The application will automatically open in your default browser at `http://localhost:8000`.

## 📈 How It Works

1. **Input Stage:** The user enters a log sequence, user actions, or chats naturally with the agent.
2. **Analysis Stage:** The agent parses the inputs, checks for known anomalous patterns, and passes the context to the AI model.
3. **Feedback Stage:** The agent prints step-by-step reasoning using Chainlit's nested step messages and outputs a structured behavior summary.
