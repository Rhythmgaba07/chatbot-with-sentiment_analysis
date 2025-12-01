# src/chatbot.py

from src.sentiment import SentimentAnalyzer


class Chatbot:
    """
    Simple chatbot with:
    - conversation history
    - message-level sentiment (Tier 2)
    - conversation-level sentiment summary (Tier 1)
    """

    def __init__(self, model_name="vader"):
        
        self.sentiment = SentimentAnalyzer(model_name=model_name)
        self.conversation_history = []
        self.message_sentiments = []
        # Sentiment analyzer (supports VADER or HF model)
        self.sentiment = SentimentAnalyzer(model_name=model_name)

    def reply(self, user_message: str):
        result = self.process_user_message(user_message)
        return result["bot_reply"], result["sentiment"]


    def get_bot_response(self, user_message: str) -> str:
        """
        Very simple rule-based bot response logic.
        """

        msg = user_message.lower()

        if any(word in msg for word in ["hello", "hi", "hey"]):
            return "Hello! How can I help you today?"

        if "help" in msg:
            return "Sure, tell me what's troubling you."

        if any(word in msg for word in ["sad", "upset", "angry", "bad"]):
            return "I'm sorry you're feeling this way. Want to talk more?"

        if "thank" in msg:
            return "You're welcome! Happy to help."

        if "bye" in msg:
            return "Goodbye! Take care."

        return "I understand. Please continue."

    def process_user_message(self, message: str) -> dict:
        """
        Handle:
        - Saving user messages
        - Message-level sentiment (Tier 2)
        - Generating bot response
        """

        # Save user message
        self.conversation_history.append(message)

        # Analyze sentiment
        sentiment_result = self.sentiment.analyze_message(message)
        self.message_sentiments.append(sentiment_result["compound"])

        # Generate reply
        reply = self.get_bot_response(message)

        # Save bot reply to conversation history
        self.conversation_history.append(reply)

        return {
            "user_message": message,
            "sentiment": sentiment_result,
            "bot_reply": reply
        }

    def finalize_conversation_report(self) -> dict:
        """
        End of chat:
        - Full conversation sentiment
        - Mood trend across messages
        """

        overall = self.sentiment.analyze_conversation(self.conversation_history)
        trend = self.sentiment.mood_trend(self.message_sentiments)

        return {
            "overall_sentiment": overall,
            "mood_trend": trend
        }
