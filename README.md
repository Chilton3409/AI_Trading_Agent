# AI_Trading_Agent
# AI Stock Trading Assistant (Alpaca/Gemini Integration)

An automated Python trading system that uses the Alpaca API for trade execution. It uses the Google Gemini (Meta AI) API for real-time news sentiment analysis to make autonomous trading decisions.

---

## 🚀 Project Overview

This project uses an event-driven trading strategy. It scans the market for top movers. It analyzes news articles using AI sentiment analysis. The system identifies top picks and executes buy orders via the Alpaca trading platform.

The project shows the integration of financial APIs, AI decision-making, and asynchronous system design.

## ✨ Key Features

*   **AI-Driven Decisions:** Uses the Gemini/Meta AI API in `sentiment_analysis` and `ai_top_picks` to process news data and generate trade signals.
*   **Alpaca API Integration:** Retrieves account information, market movers, news, and candles. It also executes trade orders (`create_buy_order`).
*   **Asynchronous Processing:** Built using Python's `asyncio` to manage high-latency API calls efficiently.
*   **Portfolio Hypervisor:** A monitoring function provides a snapshot of the account's financial landscape (buying power, equity, daytrade count).
*   **Configuration Management:** Securely manages API keys and trading parameters using environment variables.

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Libraries:** `alpaca-py`, `python-dotenv`, `asyncio`, `re`, `logging`
*   **AI/ML:** Google Gemini (via `meta_ai_api`) for NLP/Sentiment Analysis
*   **API:** REST APIs (Alpaca Trading, Meta AI)

## ⚙️ Installation & Setup

### Prerequisites

1.  **Python 3.8+** installed.
2.  Accounts with Alpaca and the Meta AI API (Google Gemini).

### Steps

1.  **Clone the repository:**
    ```bash
    git clone github.com
    cd YourRepoName
    ```

2.  **Install dependencies:**
    *(You will need a `requirements.txt` file listing all libraries used, e.g., alpaca-py, requests, python-dotenv)*
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure environment variables:**
    Create a file named `.env` in the root directory and add your credentials:
    ```
    API_KEY="your_alpaca_api_key"
    API_SECRET="your_alpaca_api_secret"
    META_AI_TOKEN="your_gemini_api_key"
    ```

4.  **Run the application:**
    *(Provide the command you use to start your main script, e.g.)*
    ```bash
    python main_alpaca_system.py
    ```

## 🧠 Architectural Highlights

The system uses an asynchronous, object-oriented design:

*   **`AITradingSystem` Class:** Manages all application state, parameters, and orchestrates the trading loop.
*   **`AlpacaBotLink` (External Service):** A client abstraction layer for all API communication.
*   **Decision Flow:** The system moves from data ingestion (`get_market_movers`, `get_news`, `get_candles`) to AI analysis (`sentiment_analysis`, `ai_top_picks`) before triggering execution (`create_buy_order`).

