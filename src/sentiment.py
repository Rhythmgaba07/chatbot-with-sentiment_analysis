# src/sentiment.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self, model_name="vader"):
        """
        model_name is kept for extensibility (HF models etc.)
        but default is 'vader'
        """
        self.model_name = model_name

        # Initialize VADER analyzer
        if model_name == "vader":
            self.analyzer = SentimentIntensityAnalyzer()
        else:
            raise ValueError("Unsupported model. Use model_name='vader'.")

    def analyze_message(self, text: str) -> dict:
        """
        Analyze sentiment for a single message.
        Used for Tier 2.
        """
        scores = self.analyzer.polarity_scores(text)

        # Determine label
        compound = scores["compound"]
        if compound >= 0.05:
            label = "positive"
        elif compound <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        return {
            "label": label,
            "compound": compound,
            "scores": scores
        }

    def analyze_conversation(self, messages: list) -> dict:
        """
        Checks overall conversation-level sentiment (Tier 1)
        Includes both user + bot messages.
        """

        full_text = " ".join(messages)
        scores = self.analyzer.polarity_scores(full_text)

        compound = scores["compound"]
        if compound >= 0.05:
            label = "positive"
        elif compound <= -0.05:
            label = "negative"
        else:
            label = "neutral"

        return {
            "label": label,
            "compound": compound,
            "scores": scores
        }

    def mood_trend(self, message_compounds: list) -> str:
        """
        Bonus: Shows if mood is improving or worsening over time.
        """

        if len(message_compounds) < 2:
            return "Not enough data to calculate trend."

        start = message_compounds[0]
        end = message_compounds[-1]

        if end > start:
            return "User mood improved during conversation."
        elif end < start:
            return "User mood worsened during conversation."
        else:
            return "User mood remained stable."
