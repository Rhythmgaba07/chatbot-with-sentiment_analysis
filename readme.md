Liapus AI – Chatbot with Sentiment Analysis
Overview

This project implements a sentiment-aware chatbot built using Python. It maintains the entire conversation history, evaluates the sentiment of each user message, and generates an overall emotional summary at the end of the interaction. The design follows modular, production-oriented principles and fulfills both Tier 1 and Tier 2 requirements as outlined in the assignment.

The chatbot is rule-based for response generation, while the sentiment evaluation is powered by the VADER sentiment analysis engine, making the system lightweight, interpretable, and easy to extend. This project was developed as part of the Liapus AI assignment.

Features
Tier 1 – Conversation-Level Sentiment Analysis (Mandatory)

Stores complete conversation history (user and bot messages).

Computes overall sentiment at the end of the session.

Provides a clear label indicating the emotional direction of the full conversation.

Tier 2 – Statement-Level Sentiment Analysis (Additional Credit)

Performs sentiment analysis for every individual user message.

Displays sentiment label and compound score immediately after each message.

Includes a mood-trend evaluation showing whether the user’s tone improved, declined, or remained stable throughout the interaction.

Additional Capabilities

Rule-based bot responses for greetings, emotional phrases, and general queries.

Modular structure (separate chatbot, sentiment logic, and main runner file).

Unit tests implemented using pytest.

Technologies Used

Python 3.10+

VADER Sentiment Analyzer (vaderSentiment) – lexicon-based sentiment evaluation

NLTK – used for VADER support

pytest – unit testing

Optional (not activated in the main build):

transformers and torch for future integration of transformer-based models

Installation and Setup
1. Clone the repository
git clone https://github.com/Rhythmgaba07/chatbot-with-sentiment_analysis
cd chatbot-with-sentiment_analysis

2. Create and activate a virtual environment
python -m venv venv


Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3. Install project dependencies
pip install -r requirements.txt

How to Run the Chatbot

Run the following command in the project directory:

python main.py


A sample interaction looks like this:

You: Hello
Bot: Hello! How can I help you today?
[Sentiment] Label: positive  Score: 0.440


Type exit or bye to end the chat.
At the end, a summary is automatically generated:

Overall Sentiment: positive  Score: 0.599
Mood Trend: User mood improved during conversation.

Sentiment Analysis Logic

The project uses VADER (Valence Aware Dictionary and sEntiment Reasoner) as its sentiment engine.
The logic is implemented in src/sentiment.py.

Per-Message Analysis (Tier 2)

Every user message is processed individually.

VADER returns a set of polarity scores.

A compound score determines the label:

≥ 0.05: Positive

≤ -0.05: Negative

Otherwise: Neutral

Conversation-Level Analysis (Tier 1)

All messages (user + bot) are concatenated into a single text.

VADER generates a combined sentiment score.

The final label represents the emotional direction of the overall conversation.

Mood Trend

Tracks the compound scores of each user message.

Compares the first and last sentiment score to determine the emotional shift.

This method is deterministic, explainable, and does not require model training.

Status of Tier 2 Implementation
Feature	Status
Statement-level sentiment evaluation	Completed
Displaying sentiment per message	Completed
Mood trend analysis	Completed
Transformer-based sentiment models (optional)	Not included
Unit Testing

Unit tests are located in the tests/ directory.

To run all tests:

pytest


A successful test run will show all test cases passing, such as:

5 passed in 0.44s


Testing verifies:

Chatbot response logic

Sentiment label boundaries

Conversation sentiment aggregation

Mood trend evaluation

Folder Structure
chatbot-with-sentiment_analysis/
│
├── src/
│   ├── chatbot.py          # Chatbot class and logic
│   └── sentiment.py        # Sentiment analysis module
│
├── tests/
│   └── test_chatbot.py     # Unit tests for chatbot and sentiment logic
│
├── main.py                 # Entry point for running the chatbot
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

Future Enhancements

The following improvements can be integrated:

Transformer-based sentiment analysis using HuggingFace models for higher accuracy.

Graphical user interface (Tkinter or modern web-based UI).

Visual mood-trend charts or sentiment intensity graphs.

Logging, exception handling, and analytics dashboards.

Conversation summarization using a natural language generation model.