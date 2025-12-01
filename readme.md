Liapus AI Chatbot with Sentiment Analysis
Project Overview

This project implements a Python-based chatbot capable of performing sentiment analysis on user inputs. The chatbot maintains full conversation history, evaluates sentiment for each user message, and summarizes the overall conversation mood. It is modular, production-ready, and designed for Tier 1 and Tier 2 implementation.

Features

Tier 1 – Conversation-Level Sentiment Analysis (Mandatory)

Maintains full conversation history (user + bot messages).

Provides overall sentiment at the end of the conversation.

Output indicates general emotional direction.

Tier 2 – Statement-Level Sentiment Analysis (Additional Credit)

Evaluates sentiment for each user message individually.

Displays message sentiment with label and score.

Optional enhancement: summarizes mood trend across the conversation.

Simple rule-based chatbot responses for greetings, help requests, emotional messages, thanks, and exit commands.

Technologies Used

Python 3.10+ – primary programming language

VADER Sentiment Analyzer (vaderSentiment) – performs sentiment analysis without model training

NLTK – supports VADER sentiment lexicon

Optional Libraries for Future Enhancements:

transformers & torch – for potential integration of transformer-based sentiment models

pytest – for unit testing

Installation & Setup

Clone the repository:

git clone https://github.com/Rhythmgaba07/chatbot-with-sentiment_analysis
cd chatbot-with-sentiment_analysis


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt

How to Run

Run the main script:

python main.py


Chat with the bot by typing messages:

🤖 Liapus AI Chatbot | Sentiment-Aware
Type 'exit' to quit.

You: Hello
Bot: Hello! How can I help you today?
[Sentiment] Label: positive  Score: 0.440


Type exit or bye to end the conversation.

At the end, a conversation summary with overall sentiment and mood trend is displayed.

Sentiment Logic Explanation

VADER (Valence Aware Dictionary and sEntiment Reasoner) is used for sentiment analysis.

Per-message analysis (Tier 2):

Each user message is scored for compound sentiment and labeled as positive, negative, or neutral.

Conversation-level analysis (Tier 1):

All messages (user + bot) are concatenated.

The overall compound score determines the general sentiment.

Mood trend:

Compares the first and last user message sentiment to determine if the mood improved, worsened, or remained stable.

Note: This approach does not require training a model; VADER is a pre-built lexicon-based sentiment analyzer.

Status of Tier 2 Implementation
Feature	Status
Statement-level sentiment evaluation	✅ Complete
Display sentiment for each message	✅ Complete
Mood trend summarization across conversation	✅ Complete
Optional transformer-based analysis	⚠ Not added
Example Output
You: Your service disappoints me
Bot: I understand. Please continue.
[Sentiment] Label: negative  Score: -0.382

You: Last experience was better
Bot: I understand. Please continue.
[Sentiment] Label: positive  Score: 0.440

You: exit
Bot: Goodbye! Take care.

📊 Conversation Summary:
Overall Sentiment: positive  Score: 0.599
Mood Trend: User mood improved during conversation.

Folder Structure
chatbot-with-sentiment_analysis/
│
├── src/
│   ├── chatbot.py          # Chatbot class
│   └── sentiment.py        # Sentiment analysis logic
│
├── main.py                 # Main script to run the chatbot
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

Future Enhancements / Optional Features

We can Integrate transformer-based sentiment models (HuggingFace) for more accurate analysis.

We can Add GUI interface (Tkinter or web app) for interactive use.

We can Add unit tests using pytest for automated validation.

We can Include emoji-based mood visualization or sentiment trend graphs.